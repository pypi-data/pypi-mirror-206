from functools import wraps
import inspect
import os
import sys
import logging
import logging.handlers
import datetime

from aws_embedded_metrics.sinks.stdout_sink import StdoutSink, Sink
from aws_embedded_metrics.logger.metrics_logger import MetricsLogger
from aws_embedded_metrics.logger.metrics_context import MetricsContext
from aws_embedded_metrics.environment.local_environment import LocalEnvironment

from amazon_sagemaker_jupyter_scheduler.error_util import ErrorMatcher
from amazon_sagemaker_jupyter_scheduler.app_metadata import (
    get_aws_account_id,
    get_domain_id,
    get_user_profile_name,
)

HOME_DIR = os.path.expanduser("~")
LOG_FILE_PATH = os.path.join(HOME_DIR, ".sagemaker")
os.makedirs(LOG_FILE_PATH, exist_ok=True)
LOG_FILE_NAME = "sagemaker-scheduler.api.log"

logger = logging.getLogger("sagemaker-scheduler-api")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(LOG_FILE_PATH, LOG_FILE_NAME))
logger.addHandler(file_handler)


class LogFileSink(StdoutSink):
    def accept(self, context: MetricsContext) -> None:
        for serialized_content in self.serializer.serialize(context):
            if serialized_content:
                logger.info(serialized_content)

    @staticmethod
    def name() -> str:
        return "LogFileSink"


class LogFileEnvironment(LocalEnvironment):
    def get_sink(self) -> Sink:
        return LogFileSink()


async def resolve_environment():
    return LogFileEnvironment()


def async_with_metrics(operation):
    def decorate(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            error = fault = 0
            context = MetricsContext().empty()
            context.namespace = "SagemakerStudioScheduler"
            context.put_dimensions({"Operation": operation})
            context.set_property("AccountId", get_aws_account_id())
            context.set_property("UserProfileName", get_user_profile_name())
            context.set_property("DomainId", get_domain_id())
            context.should_use_default_dimensions = False
            metrics_logger = MetricsLogger(resolve_environment, context)
            if "metrics" in inspect.signature(func).parameters:
                kwargs["metrics"] = metrics_logger
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                em = ErrorMatcher()
                # TODO: Improve on the faults
                if em.is_fault(e):
                    fault = 1
                else:
                    error = 1
                # log the scrubbed error of any customer information
                raise e
            finally:
                context.put_metric("Error", error, "Count")
                context.put_metric("Fault", fault, "Count")
                elapsed = datetime.datetime.now() - start_time
                context.put_metric(
                    "Latency", int(elapsed.total_seconds() * 1000), "Milliseconds"
                )
                await metrics_logger.flush()

        return wrapper

    return decorate


def get_operational_logger(name="sagemaker-scheduler", log_base_directory=LOG_FILE_PATH, also_write_to_stdout=True):
    os.makedirs(log_base_directory, exist_ok=True)

    default_logger = logging.getLogger(name)
    default_logger.handlers.clear()
    default_logger.setLevel(logging.INFO)

    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_base_directory, f'{name}.log'),
        maxBytes=1024 * 1000 * 20,
        backupCount=5)

    stream_handler = logging.StreamHandler(stream=sys.stdout)

    file_handler.setFormatter(logging.Formatter('{"__timestamp__": "%(asctime)s", "Name": "%(name)s", "Level": "%(levelname)s", "Message": "%(message)s"}'))
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    default_logger.addHandler(file_handler)

    if also_write_to_stdout:
        default_logger.addHandler(stream_handler)

    return default_logger

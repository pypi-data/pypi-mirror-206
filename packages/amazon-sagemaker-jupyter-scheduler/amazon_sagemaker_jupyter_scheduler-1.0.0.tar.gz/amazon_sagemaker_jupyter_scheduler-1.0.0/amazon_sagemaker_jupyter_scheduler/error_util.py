import botocore.exceptions
from tornado import web
from jupyter_scheduler.exceptions import SchedulerError


class SageMakerSchedulerError(SchedulerError):
    @staticmethod
    def from_boto_error(boto_error: botocore.exceptions.ClientError):
        return SageMakerSchedulerError(
            f"{boto_error.response['Error']['Code']}: {boto_error.response['Error']['Message']}"
        )

    @staticmethod
    def from_runtime_error(error):
        return SageMakerSchedulerError(f"RuntimeError: {str(error)}")

    @staticmethod
    def from_no_credentials_error(error):
        return SageMakerSchedulerError(f"NoCredentialsError: {str(error)}")


class ErrorMatcher:
    def is_training_job_status_validation_error(
        self,
        error_response: botocore.exceptions.ClientError,
    ) -> bool:
        """
        Returns True if the botocore ClientError indicates that the SageMaker Training Job is in a disallowed status for the
        requested operation.
        :param error_response:
        :return:
        """
        # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html
        return (
            error_response.response["Error"]["Code"] == "ValidationException"
            and "The request was rejected because the training job is in status"
            in error_response.response["Error"]["Message"]
        )

    def is_expired_token_error(self, error):
        return (
            isinstance(error, botocore.exceptions.ClientError)
            and error.response["Error"]["Code"] == "ExpiredTokenException"
        )


    def is_fault(self, error):
        if isinstance(error, botocore.exceptions.ClientError) and error.response[
            "Error"
        ]["Code"] in ["AccessDenied"]:
            return False
        return True


class ErrorConverter:
    def boto_error_to_web_error(self, error: botocore.exceptions.ClientError):
        if not isinstance(error, botocore.exceptions.ClientError):
            raise RuntimeError(
                f"Error is not an instance of botocore.exceptions.ClientError: {error}"
            )

        return web.HTTPError(
            error.response["ResponseMetadata"]["HTTPStatusCode"],
            f"{error.response['Error']['Code']}: {error.response['Error']['Message']}",
        )


class ErrorFactory:
    def internal_error(self, error: BaseException):
        return web.HTTPError(500, str(error))

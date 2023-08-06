import botocore.exceptions

from amazon_sagemaker_jupyter_scheduler.error_util import ErrorMatcher


def test_training_job_validation_error():
    error = botocore.exceptions.ClientError(
        {
            "Error": {
                "Code": "ValidationException",
                "Message": "The request was rejected because the training job is in status Failed",
            }
        },
        "StopTrainingJob",
    )

    assert ErrorMatcher().is_training_job_status_validation_error(error)

from aws_services.s3.s3_constants import check_dict as s3_check_dict
class AWSServices:
    S3 = "s3"
    KINESIS_STREAMS = "Kinesis Stream"
    KINESIS_FIREHOSE = "Kinesis Firehose"
    GLUE = "Glue"
    RDS = "RDS"
    EMR = "EMR"
    API_GATEWAY = "Api Gateway"
    LAMBDA = "Lambda"
    FARGATE = "Fargate"
    SQS = "SQS"
    SNS = "SNS"
    REDSHIFT = "Redshift"
    SES="SES"
    DYNAMODB = "Dynamodb"

class ResultStatus:
    PASSED = "Passed"
    FAILED = "Failed"
    UNKNOWN = "Unknown"
    DISABLED = "Disabled"

class Type:
    SECURITY_CHECK = "SecurityCheck"
    BEST_PRACTICES = "BestPractices"
    ACC_SECURITY_CHECK = "AccountSecurityCheck"
    ACC_BEST_PRACTICES = "AccountBestPractices"

overall_check_dict = {
    AWSServices.S3: s3_check_dict,
}

class Paths:
    CONFIG_FILE_PATH = "../../../config.json"

class Generic:
    MAX_RETRIES = 3
    REGION_NAME = ""
    REQUIRED_TAGS = []

from aws_services.s3.s3_service import S3
from common.constants import application_constants as constants


def initialize_members():
    instantiate_members = {
        constants.AWSServices.S3: S3(),
    }
    return instantiate_members

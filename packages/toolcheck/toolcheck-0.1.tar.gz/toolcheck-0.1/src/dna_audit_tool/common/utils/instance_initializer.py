from dna_audit_tool.aws_services.dynamodb.dynamodb_service import DynamoDB
from dna_audit_tool.aws_services.redshift.redshift_service import Redshift
from dna_audit_tool.aws_services.s3.s3_service import S3
from dna_audit_tool.aws_services.kinesis_firehose.kinesis_firehose_service import KinesisFirehose
from dna_audit_tool.aws_services.glue.glue_service import Glue
from dna_audit_tool.aws_services.rds.rds_service import RDS
from dna_audit_tool.aws_services.kinesis_stream.kinesis_stream_service import KinesisStream
from dna_audit_tool.aws_services.emr.emr_service import EMR
from dna_audit_tool.aws_services.api_gateway.api_gateway_service import APIGateway
from dna_audit_tool.aws_services.dat_lambda.lambda_service import DatLambda
from dna_audit_tool.aws_services.fargate.fargate_service import Fargate
from dna_audit_tool.aws_services.sqs.sqs_service import SQS
from dna_audit_tool.common.constants import application_constants as constants


def initialize_members():
    instantiate_members = {
        constants.AWSServices.S3: S3(),
        constants.AWSServices.GLUE: Glue(),
        constants.AWSServices.RDS: RDS(),
        constants.AWSServices.KINESIS_FIREHOSE: KinesisFirehose(),
        constants.AWSServices.KINESIS_STREAMS: KinesisStream(),
        constants.AWSServices.EMR: EMR(),
        constants.AWSServices.API_GATEWAY: APIGateway(),
        constants.AWSServices.LAMBDA: DatLambda(),
        constants.AWSServices.FARGATE: Fargate(),
        constants.AWSServices.SQS: SQS(),
        constants.AWSServices.REDSHIFT: Redshift(),
        constants.AWSServices.DYNAMODB: DynamoDB(),
    }
    return instantiate_members

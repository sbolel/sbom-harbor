
"""This Stack is used to set up shared resources
that the other stacks use when deploying the application"""

from os import path
from constructs import Construct
from aws_cdk import (
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_events as eventbridge,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    RemovalPolicy,
    Stack,
)
from deploy.constants import (
    S3_BUCKET_ID,
    S3_BUCKET_NAME,
    SHARED_RESOURCE_STACK_ID,
)
from deploy.constructs import (
    SBOMTeamTokenTable,
    SBOMTeamTable,
    SBOMTeamMemberTable
)
from deploy.constructs.harbor_teams_table import HarborTeamsTable
from deploy.util import SBOMApiVpc
from deploy.util import DynamoTableManager

from cyclonedx.constants import EVENT_BUS_NAME


class SBOMSharedResourceStack(Stack):

    """This Stack is used to set up shared resources
    that the other stacks use when deploying the application"""

    def __init__(
        self,
        scope: Construct,
        **kwargs,
    ) -> None:

        # Run the constructor of the Stack superclass.
        super().__init__(scope, SHARED_RESOURCE_STACK_ID, **kwargs)

        # Create the VPC
        vpc = SBOMApiVpc(self)
        self.vpc = vpc.get_vpc()

        # Create the S3 Bucket to put the BOMs in
        self.s3_bucket = s3.Bucket(
            self,
            S3_BUCKET_ID,
            auto_delete_objects=True,
            bucket_name=S3_BUCKET_NAME,
            public_read_access=False,
            removal_policy=RemovalPolicy.DESTROY,
            event_bridge_enabled=True,
        )

        self.event_bus = eventbridge.EventBus(
            self, EVENT_BUS_NAME,
            event_bus_name=EVENT_BUS_NAME,
        )

        __cwd = path.dirname(__file__)

        team_table: dynamodb.Table = SBOMTeamTable(self).get_construct()
        team_member_table: dynamodb.Table = SBOMTeamMemberTable(self).get_construct()
        team_token_table: dynamodb.Table = SBOMTeamTokenTable(self).get_construct()
        harbor_teams_table: dynamodb.Table = HarborTeamsTable(self).get_construct()

        self.table_manager = DynamoTableManager(
            team_table,
            team_member_table,
            team_token_table,
            harbor_teams_table,
        )

    def get_vpc(self) -> ec2.Vpc:

        """Gets the VPC"""

        return self.vpc

    def get_s3_bucket(self) -> s3.Bucket:

        """Gets the S3 Bucket"""

        return self.s3_bucket

    def get_dynamo_table_manager(self) -> DynamoTableManager:

        """Gets the table manager for DynamoDB"""

        return self.table_manager

    def get_event_bus(self) -> eventbridge.EventBus:

        """Gets the Harbor's Event Bus"""

        return self.event_bus
from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_dynamodb as dynamodb,
    aws_applicationautoscaling as autoscale,
)

from cyclonedx.constants import (
    HARBOR_TEAMS_TABLE_ID,
    HARBOR_TEAMS_TABLE_NAME,
    HARBOR_TEAMS_TABLE_PARTITION_KEY,
    HARBOR_TEAMS_TABLE_SORT_KEY,
)


class HarborTeamsTable(Construct):

    """
     The Teams Management Table
    """

    def __init__(
        self,
        scope: Construct,
    ):
        super().__init__(scope, HARBOR_TEAMS_TABLE_NAME)

        self.construct = dynamodb.Table(
            self, HARBOR_TEAMS_TABLE_ID,
            table_name=HARBOR_TEAMS_TABLE_NAME,
            billing_mode=dynamodb.BillingMode.PROVISIONED,
            removal_policy=RemovalPolicy.DESTROY,
            partition_key=dynamodb.Attribute(
                name=HARBOR_TEAMS_TABLE_PARTITION_KEY,
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name=HARBOR_TEAMS_TABLE_SORT_KEY,
                type=dynamodb.AttributeType.STRING,
            ),
        )

        # Set up scaling
        read_scaling = self.construct.auto_scale_read_capacity(
            min_capacity=1,
            max_capacity=50,
        )

        read_scaling.scale_on_utilization(
            target_utilization_percent=50
        )

        read_scaling.scale_on_schedule(
            "ScaleUpInTheMorning",
            schedule=autoscale.Schedule.cron(
                hour="8",
                minute="0",
            ),
            min_capacity=20
        )

        read_scaling.scale_on_schedule(
            "ScaleDownAtNight",
            schedule=autoscale.Schedule.cron(
                hour="20",
                minute="0",
            ),
            max_capacity=20
        )

    def get_construct(self) -> dynamodb.Table:

        """ Return the underlying CDK Defined L3 Construct """

        return self.construct

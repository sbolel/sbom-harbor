"""
-> Handler and associated policies are required for
-> authorization when uploading and SBOM.
"""

import datetime
from json import dumps

import boto3

from cyclonedx.db.harbor_db_client import HarborDBClient
from cyclonedx.exceptions.database_exception import DatabaseError
from cyclonedx.handlers.common import _extract_id_from_path
from cyclonedx.model.team import Team
from cyclonedx.handlers.common import (
    allow_policy,
    deny_policy,
    print_values,
)


def api_key_authorizer_handler(event: dict, context: dict = None):

    """
    -> This is the handler used when uploading an SBOM.
    """

    print_values(event, context)

    try:
        # Extract the Method ARN and the token from the event
        method_arn: str = event["methodArn"]
        token: str = event["authorizationToken"]
        team_id: str = _extract_id_from_path("team", event)

        resource = boto3.resource("dynamodb")
        team: Team = HarborDBClient(resource).get(
            Team(team_id=team_id),
            recurse=True,
        )
    except KeyError as ke:
        return {
            "statusCode": 400,
            "isBase64Encoded": False,
            "body": dumps({"error": f"Unable to find key: {ke}"}),
        }
    except DatabaseError as de:
        return {
            "statusCode": 400,
            "isBase64Encoded": False,
            "body": dumps({"error": f"Missing team {de}"}),
        }

    # Set the policy to default Deny
    policy: dict = deny_policy()

    # Go through the tokens the team has
    for token_obj in team.tokens:

        # Make sure the token is enabled
        if token_obj.token == token and token_obj.enabled:
            now = datetime.datetime.now().timestamp()
            expires = token_obj.expires

            # Make sure the token is not expired
            if now < float(expires):
                policy = allow_policy(method_arn, "")

    # If the token exists, is enabled and not expired, then allow
    return policy
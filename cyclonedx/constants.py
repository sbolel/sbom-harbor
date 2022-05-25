""" Constants to be used throughout the system"""

DT_API_PORT = 8080
APP_PORT = 433

ENRICHMENT_ID = "ENRICHMENTID"

DT_DEFAULT_ADMIN_PWD = "admin"
ENRICHMENT_ID_SQS_KEY = "enrichmentid"
FINDINGS_SQS_KEY = "findings_key"
DT_QUEUE_URL_EV = "DT_QUEUE_URL"
SBOM_BUCKET_NAME_KEY = "sbom_bucket"
SBOM_S3_KEY = "sbom_s3_key"
DT_API_KEY = "DT_API_KEY"
DT_API_BASE = "DT_API_BASE"
DT_ROOT_PWD = "DT_ROOT_PWD"

EMPTY_VALUE = "EMPTY"

APP_LOAD_BALANCER_ID = "AppLoadBalancer-ID"
APP_LOAD_BALANCER_LISTENER_ID = "AppLoadBalancer-Target-ID"
APP_LOAD_BALANCER_TARGET_ID = "AppLoadBalancer-Target-ID"

DT_LOAD_BALANCER_ID = "DT-LB-ID"
DT_LOAD_BALANCER_LISTENER_ID = "DT-LB-LISTENER-ID"
DT_LOAD_BALANCER_TARGET_ID = "DT-LB-TARGET-ID"

ALLOW_DT_PORT_SG = f"ALLOW_{DT_API_PORT}_SG"

USER_POOL_NAME_KEY = "USER_POOL_NAME"
USER_POOL_CLIENT_ID_KEY = "USER_POOL_CLIENT_ID"

# DynamoDB
TEAM_TABLE_NAME = "SbomTeamTable"
TEAM_TABLE_ID = f"{TEAM_TABLE_NAME}Id"

# DynamoDB
TEAM_MEMBER_TABLE_NAME = "SbomTeamMemberTable"
TEAM_MEMBER_TABLE_ID = f"{TEAM_MEMBER_TABLE_NAME}Id"

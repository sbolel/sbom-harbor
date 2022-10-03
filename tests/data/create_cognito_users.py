
import boto3

client = boto3.client('cognito-idp')


def test_create_cognito_users():

    usernames = [
        "sbomadmin", "quinn", "quinton",
        "quison", "heather", "bill", "martha",
        "fred", "maria", "sam", "linda"
    ]

    response = client.list_user_pools(
        MaxResults=5
    )

    user_pool = response["UserPools"][0]
    user_pool_id: str = user_pool["Id"]

    print(user_pool)

    for username in usernames:

        email_username = f"{username}@aquia.io"

        teams = "dawn-patrol,dusk-patrol" if username == 'sbomadmin' else "dawn-patrol"

        try:
            client.admin_delete_user(
                UserPoolId=user_pool_id,
                Username=email_username,
            )
        except Exception:
            ...

        client.admin_create_user(
            UserPoolId=user_pool_id,
            Username=email_username,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email_username
                }, {
                    'Name': 'custom:teams',
                    'Value': teams
                }
            ],
            TemporaryPassword='AbC123P@55!',
            ForceAliasCreation=True,
            MessageAction='SUPPRESS',
            DesiredDeliveryMediums=['EMAIL']
        )

        client.admin_set_user_password(
            UserPoolId=user_pool_id,
            Username=email_username,
            Password='L0g1nTe5tP@55!',
            Permanent=True,
        )

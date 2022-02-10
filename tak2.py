import boto3
client = boto3.client('secretsmanager')

print(client.list_secrets())
response = client.get_secret_value(
    SecretId='',
    )

print(responce)
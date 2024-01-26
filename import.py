import boto3

iam = boto3.client('iam')

def create_user(iam , username):

    response = iam.create_user(
        UserName= username
    )


create_user(iam, 'ramar')
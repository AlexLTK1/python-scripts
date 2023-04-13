import boto3

cloudformation = boto3.client('cloudformation')

response = cloudformation.create_stack(
    StackName='my-stack',
    TemplateURL='https://my-bucket.s3.amazonaws.com/my-template.yml',
    Parameters=[
        {
            'ParameterKey': 'InstanceType',
            'ParameterValue': 't2.micro'
        },
        {
            'ParameterKey': 'KeyName',
            'ParameterValue': 'my-key'
        }
    ],
    Capabilities=[
        'CAPABILITY_IAM',
    ]
)

print(response)
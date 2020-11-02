import boto3
sns = boto3.client("sns")

def handler(event, context):
    try:
        data = sns.publish(
            Message="gvhdaf",
            TopicArn="arn:aws:sns:us-east-1:263248768798:ktopic",
            MessageStructure="String",
            MessageAttributes={}
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}

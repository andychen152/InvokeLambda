import boto3
import datetime

def reverseString(data):
    return data[::-1]

def lambda_handler(event, context):
    
    
    data = "this is a test"
    dataReverse = reverseString(data)
    
    S3BUCKET = "apigatewayinvokelambda2632018"
    S3BUCKETREVERSE = "apigatewayinvokelambda2632018reverse"
    
    s3_client = boto3.client('s3')
    s3_client.put_object(Body=data, Bucket=S3BUCKET, Key=str(datetime.datetime.now())+'.txt', ContentType='text/csv', ContentEncoding='utf-8') 
    s3_client.put_object(Body=dataReverse, Bucket=S3BUCKETREVERSE, Key=str(datetime.datetime.now())+'.txt', ContentType='text/csv', ContentEncoding='utf-8')
    
    return 'success'

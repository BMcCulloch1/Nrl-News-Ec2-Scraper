import json
import boto3

def upload_json_to_s3(data, bucket_name, key_name):
    
    json_string = json.dumps(data, indent = 2)
    
    s3 = boto3.client("s3")

    s3.put_object(
        Bucket = bucket_name,
        Key = key_name,
        Body = json_string,
        ContentType = 'application/json'
    )
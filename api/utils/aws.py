import boto3

def uploadfile(file,filename):
    s3_client = boto3.client("s3")
    s3_client.upload_fileobj(file,"toogle-storage",""+filename)

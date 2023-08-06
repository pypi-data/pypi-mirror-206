import boto3

s3 = boto3.client('s3')  # Create an S3 client

bucket_name = 'trial-report'  # specify the S3 bucket you want to download from


# Download the file
def download_from_s3(file_name, local_file_name):
    s3.download_file(bucket_name, file_name, local_file_name)  # 3rd argument is the local file name


# Re-upload the file to the same s3 bucket
def upload_to_s3(local_file_name, foreign_file_name):
    s3.upload_file(local_file_name, bucket_name, foreign_file_name)  # local file name, bucket, foreign name

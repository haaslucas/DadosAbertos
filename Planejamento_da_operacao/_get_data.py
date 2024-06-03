import boto3
from botocore import UNSIGNED
from botocore.client import Config
import os
import requests

# Set up the S3 client for anonymous access
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED), region_name='sa-east-1')

bucket_name = 'ons-aws-prod-opendata'
prefix = ''  # Specify the prefix if you want to filter the objects

# List objects in the S3 bucket
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

# Create a directory to store the downloaded files
download_directory = 'downloaded_files'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Function to download a file using the public URL
def download_file_public_url(bucket_name, key, download_path):
    url = f'https://{bucket_name}.s3.sa-east-1.amazonaws.com/{key}'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f'Downloaded {key} to {download_path} via public URL')
    else:
        print(f'Failed to download {key} via public URL. Status code: {response.status_code}')

# Download each object
if 'Contents' in response:
    for obj in response['Contents']:
        key = obj['Key']
        download_path = os.path.join(download_directory, key)

        # Ensure the directory exists
        if not os.path.exists(os.path.dirname(download_path)):
            os.makedirs(os.path.dirname(download_path))

        # Attempt to download the file
        try:
            s3.download_file(bucket_name, key, download_path)
            print(f'Downloaded {key} to {download_path}')
        except Exception as e:
            print(f'Error downloading {key} via boto3: {e}')
            # Attempt to download via public URL as fallback
            download_file_public_url(bucket_name, key, download_path)
else:
    print('No objects found in the bucket.')

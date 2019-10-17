import logging
import boto3
from botocore.exceptions import ClientError
from django.contrib.sites.shortcuts import get_current_site
from requests import request

from Fundoo import settings


def upload_file(image, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = image.name
    bucket = 'sachin0273'
    # Upload the file
    s3 = boto3.client('s3')
    s3.upload_fileobj(image, bucket, object_name)
    file_url = 'http://127.0.0.1:8000'+'/S3read/'+bucket+'/'+object_name+'/'
    print(file_url)
    return file_url

import logging
import boto3
from botocore.exceptions import ClientError
from django.contrib.sites.shortcuts import get_current_site
from requests import request

from Fundoo import settings


class S3:
    """Upload a file to an S3 bucket or delete"""

    def upload_file(self, image, object_name):
        """

        :param image: File to upload
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False

        """
        # If S3 object_name was not specified, use file_name
        try:
            bucket = 'sachin0273'
            # Upload the file
            s3 = boto3.client('s3')
            s3.upload_fileobj(image, bucket, object_name)
            file_url = 'http://127.0.0.1:8000' + '/S3read/' + bucket + '/' + object_name + '/'
            print(file_url)
            return file_url
        except Exception:
            return False

    def delete_file(self, image_key):
        s3 = boto3.client('s3')
        try:
            response = s3.delete_object(
                Bucket='sachin0273',
                Key=image_key,
            )
            return response
        except Exception:
            return False


if __name__ == '__main__':
    gg = S3()
    ty = gg.delete_file('@@@@')
    print(ty)

import logging
import boto3
from botocore.exceptions import ClientError


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
    client = boto3.client('sts')
    s3.upload_fileobj(image, bucket, object_name)
    gg = client.get_federation_token(DurationSeconds=3600,
                                     Name='bob',
                                     Policy='{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Action":"s3:*",'
                                            '"sts:GetFederationToken","Resource": '
                                            '"arn:aws:s3:uap-south-1:457221949031:federated-user/Bob"}]}')

    file_url = '%s/%s/%s' % (s3.meta.endpoint_url, bucket, object_name)
    print(gg)
    print(file_url)
    print('sucess')
    return file_url

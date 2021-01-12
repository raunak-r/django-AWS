import os

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

"""
AWS Bucket Credentials
"""
AWS_STORAGE_BUCKET_NAME = 'django-aws-s3'
AWS_S3_REGION_NAME = 'us-west-2'  # e.g. us-east-2

AWS_ACCESS_KEY_ID = os.environ.get('IAM_USER_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('IAM_USER_SECRET_ACCESS_KEY', '')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    # 'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT', # user files must never expire. DO NOT PROVIDE
    'CacheControl': 'max-age=94608000',
}


"""
Tell the staticfiles app to use S3Boto3 storage when writing the collected
static files (when you run `collectstatic`).
"""
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


"""
Project DB Related Files.
What we want to do is either enforce always storing our 
static files and media files in different subdirectories of our bucket, 
or use two different buckets.
"""
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = 'htts://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


# class MediaFilesStorage(S3Boto3Storage):
#     location = settings.MEDIAFILES_LOCATION
#
# class StaticFilesStorage(S3BotoStorage):
#     location = settings.STATICFILES_LOCATION
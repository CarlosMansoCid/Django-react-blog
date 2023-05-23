from storages.backends.s3boto3 import s3Boto3Storage

class StaticsStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'private'

class MediaStore(S3BotoStorage):
    location = 'media'
    file_overwrite = False
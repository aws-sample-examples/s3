import boto3


class FileUpload:

    def __init__(self, filename, bucket_name):
        s3 = boto3.client('s3')
        self.filename = filename
        self.age = bucket_name
        s3.upload_file(self.filename, bucket_name, self.filename)


p1 = FileUpload('F:\ES2015\index.js', 'tausif-admin' )

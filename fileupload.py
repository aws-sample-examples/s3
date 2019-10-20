import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

data = open('/Users/ravindrakumar/Downloads/wallpaper/12364.jpg', 'rb')
s3.Bucket('ratestbucket123').put_object(Key='test.jpg', Body=data)
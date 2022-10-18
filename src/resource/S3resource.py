import boto3


def get_bucket_all():
    s3 = boto3.resource('s3')
    bucketall = s3.buckets.all()
    for bucket in bucketall:
        print(bucket.name)

def get_key_all(bucket):
    """
    最終更新日時が取得できない。
    上位APIのresourceではなく、下位APIのclientを使ってみる
    """
    s3 = boto3.resource('s3')
    objects = s3.Bucket(bucket).objects.filter()
    for object in objects:
        print(object)

if __name__ == '__main__':
    get_key_all('alexa-image-eto')
import boto3




def get_key_all(bucket):

    s3 = boto3.resource('s3').meta.client
    bucket_name = bucket

    # list all in the bucket
    max_keys = 300
    response = s3.list_objects(Bucket=bucket_name, MaxKeys=max_keys)

    print('list all in the bucket')

    while True:
        print('IsTruncated=%r' % response.get('IsTruncated'))
        print('Marker=%s' % response.get('Marker'))
        print('NextMarker=%s' % response.get('NextMarker'))

        print('Object List')
        for content in response.get('Contents'):
            print(content.get('LastModified'))
            # print(' Name=%s, Size=%d, Owner=%s' % \
            #       (content.get('Key'), content.get('Size'), content.get('Owner').get('ID')))

        if response.get('IsTruncated'):
            response = s3.list_objects(Bucket=bucket_name, MaxKeys=max_keys,
                                       Marker=response.get('NextMarker'))
        else:
            break

    # top level folders and files in the bucket
    delimiter = '/'
    max_keys = 300


if __name__ == '__main__':
    get_key_all('alexa-image-eto')
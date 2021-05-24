#!/usr/bin/python
import boto.s3.connection
#access_key = 'Q0NR1HSL1JQJLXY8LOLF'
#secret_key = 'eOkVtFjQjgTjJn12CcxFOIe4CDdVTW0nErJoiLso'

access_key = "93F21L9GJADQJ75XZI5A"
secret_key = "XHvAHF2aC3zPNNKxVDfzqvkcoUEUPqXXECDe65uP"
conn = boto.connect_s3(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    host = '192.168.100.6', port= 80,
    is_secure=False,
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

# 创建bucket
#bucket = conn.create_bucket('s3-bucket-ai')

# 列出bucket
for bucket in conn.get_all_buckets():
        print("{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
))

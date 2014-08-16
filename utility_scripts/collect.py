import numpy
import pandas

from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.s3.connection import S3Connection

conn = S3Connection()
bucket_name = 'alakazam'
bucket = conn.get_bucket(bucket_name) 

for l in bucket.list():
  print l
  l.get_contents_to_filename('./dynamo_archive_file')


import json
import io
from minio import Minio

class MinioUploader:
    def __init__(self):
        self.minio_client = Minio(
                    "localhost:9000",
                    access_key="minioadmin",
                    secret_key="minioadmin",
                    secure=False
                )
        self.bucket_name = "gecho-bang-bucket"
        self.create_bucket()

    def create_bucket(self):
        if not self.minio_client.bucket_exists(self.bucket_name):
            self.minio_client.make_bucket(self.bucket_name)
            policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"AWS": ["*"]},
                        "Action": ["s3:GetObject", "s3:PutObject"],
                        "Resource": ["arn:aws:s3:::%s/*" % self.bucket_name]
                    }
                ]
            }
            self.minio_client.set_bucket_policy(self.bucket_name, json.dumps(policy))



    def upload_file(self, file_name, file_content):
        file_size = len(file_content)
        file_stream = io.BytesIO(file_content)
        self.minio_client.put_object(self.bucket_name, file_name, file_stream, file_size)
        file_url = self.minio_client.presigned_get_object(self.bucket_name, file_name)
        return file_url

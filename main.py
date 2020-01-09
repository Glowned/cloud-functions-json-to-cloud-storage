# coding: utf8

from google.cloud import storage
import os
import json

MY_BUCKET = "test-bucket"

def upload_to_gcs(bucket_name, blob_text, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(blob_text,content_type="application/octet-stream")

    print('File Uploaded to '+destination_blob_name)


def main(request): #For Google Cloud Functions only
    my_json = {"key":"value"}
    my_text = json.dumps(my_json)
    upload_from_string(MY_BUCKET,my_text,"Path/Of/Destination.json")    


import pymongo
import pandas as pd
from google.cloud import storage
import json

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["testdb"]
collection = db["testcol"]

# Extract data
data = list(collection.find())

# Transform data using pandas
df = pd.DataFrame(data)

# Clean data if necessary
# df = df.dropna()

# Convert DataFrame to CSV
df.to_csv('data/data.csv', index=False)

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Set your variables
bucket_name = 'your-gcs-bucket-name'
source_file_name = 'data/data.csv'
destination_blob_name = 'data/data.csv'

upload_to_gcs(bucket_name, source_file_name, destination_blob_name)

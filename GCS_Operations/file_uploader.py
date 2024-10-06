import os
from google.cloud import storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Service accounts\myfirstproject2912-4a276a62bdee.json"
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to a specified path in a Google Cloud Storage bucket."""
    try:
        # Initialize a GCS client
        storage_client = storage.Client()

        # Get the bucket
        bucket = storage_client.bucket(bucket_name)

        # Create a blob object from the file
        blob = bucket.blob(destination_blob_name)

        # Upload the file
        blob.upload_from_filename(source_file_name)

        print(f"{source_file_name} uploaded as {destination_blob_name} in bucket '{bucket_name}'.")

    except Exception as e:
        print(f"Error uploading {source_file_name}: {e}")

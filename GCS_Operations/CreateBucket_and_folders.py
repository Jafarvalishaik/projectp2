import os
from google.cloud import storage

def create_bucket_and_folders(bucket_name, folders):
    """Creates a GCS bucket and multiple folders."""
    try:
        # Initialize a GCS client
        storage_client = storage.Client()  # Will use the credentials set in the environment variable
    except Exception as e:
        print(f"Error initializing GCS client: {e}")
        return

    # Create the bucket
    try:
        bucket = storage_client.create_bucket(bucket_name)  # Creates the bucket
        print(f"Bucket '{bucket.name}' created.")
    except Exception as e:
        print(f"Error creating bucket: {e}")
        return

    # Create folders
    for folder in folders:
        blob = bucket.blob(f"{folder}/")  # Append a slash to create a "folder"
        try:
            blob.upload_from_string('')  # Upload an empty string to create the folder
            print(f"Folder '{folder}' created in bucket '{bucket.name}'.")
        except Exception as e:
            print(f"Error creating folder '{folder}': {e}")
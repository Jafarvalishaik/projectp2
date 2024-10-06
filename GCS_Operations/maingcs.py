import os
from CreateBucket_and_folders import create_bucket_and_folders
from file_uploader import upload_to_gcs

if __name__ == "__main__":
    # Configuration
    bucket_name = "p2projectjafar"  # Replace with your desired bucket name
    folders_to_create = [
        "uncleaned_folder",
        "cleaned_folder",
        
    ]

    # Create the bucket and folders
    create_bucket_and_folders(bucket_name, folders_to_create)

    # List of files and their corresponding folders
    files_to_upload = {
        r"C:\Users\jafar\OneDrive\Documents\P2 PROJECT FINAL\GCS_Operations\DataFiles\E-Commerce_data.csv": "uncleaned_folder",
        r"C:\Users\jafar\OneDrive\Documents\P2 PROJECT FINAL\GCS_Operations\DataFiles\cleaned_dataframe.csv": "cleaned_folder",
        # Add more files and folders as needed
    }

    # Loop through each file and upload it to the corresponding folder
    for source_file_name, folder_name in files_to_upload.items():
        # Construct the destination blob name
        destination_blob_name = f"{folder_name}/{os.path.basename(source_file_name)}"

        # Upload the file
        upload_to_gcs(bucket_name, source_file_name, destination_blob_name)

from google.cloud import bigquery

def load_data_to_bigquery(bucket_name, folder_name, file_name, dataset_id, table_id):
    """Loads CSV data from Google Cloud Storage to BigQuery."""
    client = bigquery.Client()

    # Define the URI of the GCS file
    uri = f"gs://{bucket_name}/{folder_name}/{file_name}"

    # Configure the load job
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Skip the header row
        autodetect=True,
    )

    # Load the data into BigQuery
    load_job = client.load_table_from_uri(
        uri, f"{dataset_id}.{table_id}", job_config=job_config
    )

    # Wait for the job to complete
    load_job.result()

    print(f"Loaded {load_job.output_rows} rows into {dataset_id}.{table_id}.")

if __name__ == "__main__":
    bucket_name = "your-bucket-name"  # Replace with your bucket name
    folder_name = "your_folder"  # The folder name in GCS
    file_name = "cleaned_dataframe.csv"  # Path to the CSV file in the folder
    dataset_id = "your_project_id.ecommerce_data"  # Replace with your project ID and dataset name
    table_id = "ecommerce_transactions"  # Replace with your desired table name

    load_data_to_bigquery(bucket_name, folder_name, file_name, dataset_id, table_id)

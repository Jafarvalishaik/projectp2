import os
from google.cloud import bigquery
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Service accounts\myfirstproject2912-4a276a62bdee.json"
def create_dataset(dataset_id):
    
    """Creates a new dataset in BigQuery."""
    client = bigquery.Client()
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"  # Specify your location
    try:
        dataset = client.create_dataset(dataset)  # API request
        print(f"Dataset {dataset.dataset_id} created.")
    except Exception as e:
        print(f"Failed to create dataset {dataset_id}: {e}")

if __name__ == "__main__":
    dataset_id = "ecommerce_data"  # Replace with your project ID and desired dataset name
    create_dataset(dataset_id)

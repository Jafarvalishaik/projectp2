from create_dataset import create_dataset
from create_table import create_table
from load_to_bq import load_data_to_bigquery
from configbq import bucket_name, folder_name, file_name

if __name__ == "__main__":
    # Dataset and table information
    project_id = "myfirstproject2912"  # Use underscores instead of periods/hyphens
    dataset_id = f"{project_id}.ecommerce_data"  # Valid dataset ID
    table_id = "ecommerce_transactions"  # Valid table ID


    # Create dataset
    create_dataset(dataset_id)

    # Create table
    create_table(dataset_id, table_id)

    # Load data
    load_data_to_bigquery(bucket_name, folder_name, file_name, dataset_id, table_id)

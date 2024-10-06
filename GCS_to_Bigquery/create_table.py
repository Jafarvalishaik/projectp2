from google.cloud import bigquery

def create_table(dataset_id, table_id):
    """Creates a new table in the specified dataset."""
    client = bigquery.Client()

    # Define the schema for the table
    schema = [
        bigquery.SchemaField("order_id", "STRING"),
        bigquery.SchemaField("customer_id", "STRING"),
        bigquery.SchemaField("customer_name", "STRING"),
        bigquery.SchemaField("product_id", "STRING"),
        bigquery.SchemaField("product_name", "STRING"),
        bigquery.SchemaField("product_category", "STRING"),
        bigquery.SchemaField("product_type", "STRING"),
        bigquery.SchemaField("qty", "INTEGER"),
        bigquery.SchemaField("price", "FLOAT"),
        bigquery.SchemaField("datetime", "TIMESTAMP"),
        bigquery.SchemaField("country", "STRING"),
        bigquery.SchemaField("city", "STRING"),
        bigquery.SchemaField("ecommerce_website_name", "STRING"),
        bigquery.SchemaField("payment_txn_id", "STRING"),
        bigquery.SchemaField("payment_txn_success", "STRING"),
        bigquery.SchemaField("failure_reason", "STRING"),
    ]

    table_ref = client.dataset(dataset_id).table(table_id)

    table = bigquery.Table(table_ref, schema=schema)

    try:
        table = client.create_table(table)  # API request
        print(f"Table {table.table_id} created in dataset {dataset_id}.")
    except Exception as e:
        print(f"Failed to create table {table_id}: {e}")

if __name__ == "__main__":
    dataset_id = "ecommerce_data"  # Replace with your project ID and dataset name
    table_id = "ecommerce_transactions"  # Replace with your desired table name
    create_table(dataset_id, table_id)

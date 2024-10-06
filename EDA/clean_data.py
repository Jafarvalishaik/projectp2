import pandas as pd
import numpy as np


def identify_rogue_records(df):
    """Performs EDA to identify rogue records in the dataset."""
    
    # Check for missing values
    print("Missing Values by Column:\n", df.isnull().sum())

    # Detect unreasonable high values in 'price' and 'qty'
    high_price_qty = df[(df['price'] > 5000) | (df['qty'] > 1000)]
    print("\nUnreasonably High Price or Quantity:\n", high_price_qty)

    # Analyze failure reasons
    failure_reason_counts = df['failure_reason'].value_counts()
    print("\nFailure Reason Counts:\n", failure_reason_counts)

def clean_rogue_data(df):
    """Cleans only the rogue columns (price, qty) and the failure_reason column."""
    
    # Ensure 'price' and 'qty' are numeric, handling invalid entries
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    # Cap high price and qty values (treat extreme values as rogue data)
    df['price'] = df['price'].clip(upper=5000)  # Cap price at 5000
    df['qty'] = df['qty'].clip(upper=1000)  # Cap quantity at 1000

    # Fill missing values in 'failure_reason'
    df['failure_reason'] = df['failure_reason'].fillna('N/A')

    # Handle rogue 'failure_reason' entries
    df['failure_reason'] = df.apply(
        lambda row: "Unknown" if row['failure_reason'] == '' else row['failure_reason'], 
        axis=1
    )

    return df

if __name__ == "__main__":
    # Load the data
    df = pd.read_csv('E-Commerce_data.csv')

    # Perform EDA and identify rogue records
    identify_rogue_records(df)

    # Clean the data focusing on rogue columns and failure reason
    cleaned_df = clean_rogue_data(df)

    # Save cleaned data to a new CSV file
    cleaned_df.to_csv('E-Commerce_data_cleaned.csv', index=False)
    print("\nData cleaning complete. Cleaned data saved to 'E-Commerce_data_cleaned.csv'.")

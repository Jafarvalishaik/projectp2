# scripts/load_data.py
import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    # Load the CSV file
    csv_data = load_data(r'C:\Users\jafar\OneDrive\Documents\P2 PROJECT FINAL\Generating Data\E-Commerce_data.csv')
    
    # Print basic information about the dataset
    print("\nData Info:")
    print(csv_data.info())

    # View the first few rows of the dataset
    print("\nFirst Few Rows:")
    print(csv_data.head())

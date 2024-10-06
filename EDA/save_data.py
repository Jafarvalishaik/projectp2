# scripts/save_data.py
import pandas as pd

def save_data(updated_data, file_path):
    """Save the cleaned data to a new CSV file."""
    updated_data.to_csv(file_path, index=False)
    print(f"\nData cleansing completed. Cleaned data saved to '{file_path}'")

if __name__ == "__main__":
    from clean_data import clean_rogue_data
    from load_data import load_data

    # Load the data
    csv_data = load_data(r'C:\Users\jafar\OneDrive\Documents\P2 PROJECT FINAL\Generating Data\E-Commerce_data.csv')

    # Clean the data
    cleaned_data = clean_rogue_data(csv_data)

    # Save the cleaned data
    save_data(cleaned_data, r'C:\Users\jafar\OneDrive\Documents\P2 PROJECT FINAL\EDA\cleaned_dataframe.csv')

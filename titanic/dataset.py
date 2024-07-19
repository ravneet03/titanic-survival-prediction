import pandas as pd
import os

# Define data paths
RAW_DATA_PATH = '/home/ravneet-singh/machine-learning/titanic-survival-prediction/data/raw/titanic.csv'
PROCESSED_DATA_PATH = '/home/ravneet-singh/machine-learning/titanic-survival-prediction/data/processed/titanic_processed.csv'

def load_and_process_data():
    # Debug print statements
    print(f"Current working directory: {os.getcwd()}")
    print(f"RAW_DATA_PATH exists: {os.path.exists(RAW_DATA_PATH)}")
    print(f"PROCESSED_DATA_PATH directory exists: {os.path.exists(os.path.dirname(PROCESSED_DATA_PATH))}")

    # Check if the raw data file exists
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"File not found: {RAW_DATA_PATH}")

    # Load raw data
    data = pd.read_csv(RAW_DATA_PATH)
    
    # Basic preprocessing
    data = data.drop(['Name', 'Ticket', 'Cabin'], axis=1)
    data = data.dropna(subset=['Age', 'Embarked'])

    # Ensure the processed directory exists
    processed_dir = os.path.dirname(PROCESSED_DATA_PATH)
    os.makedirs(processed_dir, exist_ok=True)

    # Save processed data
    data.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Processed data saved to {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    load_and_process_data()

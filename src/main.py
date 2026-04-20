from processor import process_data
from validator import validate
from db_loader import load_to_db
from logger import log

def run_pipeline():
    file_path = "data/raw/data.csv"

    for chunk in process_data(file_path):
        try:
            valid_data = validate(chunk)
            load_to_db(valid_data)
            log(f"Processed chunk of size {len(chunk)}")
        except Exception as e:
            log(f"Error: {str(e)}")


if __name__ == "__main__":
    run_pipeline()



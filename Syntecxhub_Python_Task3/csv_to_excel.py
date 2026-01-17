import pandas as pd
import argparse
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def convert_csv_to_excel(input_file, output_file):
    try:
        csv_path = Path(input_file)
        if not csv_path.exists():
            logging.error("Input CSV file does not exist.")
            sys.exit(1)

        logging.info("Reading CSV file...")
        df = pd.read_csv(csv_path)

        logging.info("Cleaning missing values...")
        df.fillna("N/A", inplace=True)

        logging.info("Normalizing column names...")
        df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

        logging.info("Saving to Excel...")
        df.to_excel(output_file, index=False)

        logging.info(f"Successfully converted to {output_file}")

    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV to Excel Converter")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output Excel file (.xlsx)")

    args = parser.parse_args()
    convert_csv_to_excel(args.input, args.output)

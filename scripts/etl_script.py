
import os
import pandas as pd
import pymysql

from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv


# Load database credentials
PROJECT_DIR = Path.home() / "airflow_project"
load_dotenv(PROJECT_DIR / ".env")


# MySQL configuration
MYSQL_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": 3306
}


# Extract data from MySQL
def extract_data():

    connection = pymysql.connect(**MYSQL_CONFIG)

    query = "SELECT * FROM sample_data"

    try:
        df = pd.read_sql_query(query, connection)
        print("Data extracted successfully!")
        return df

    finally:
        connection.close()


# Transform data
def transform_data(df):

    df_transformed = df[df["age"] > 30].copy()

    print("Data transformation completed!")

    return df_transformed


# Write data to CSV file
def write_data_to_file(df, output_directory):

    os.makedirs(output_directory, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"etl_output_{timestamp}.csv"

    file_path = os.path.join(output_directory, file_name)

    df.to_csv(file_path, index=False)

    print(f"File successfully created: {file_path}")


# Execute complete ETL process
def run_etl():

    print("ETL process started!")

    df = extract_data()

    df_transformed = transform_data(df)

    output_directory = PROJECT_DIR / "output"

    write_data_to_file(df_transformed, output_directory)

    print("ETL process completed successfully!")


if __name__ == "__main__":
    run_etl()

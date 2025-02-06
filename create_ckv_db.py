'''import pandas as pd
import sqlite3
import os

# Define database name and path (modify as needed)
database_name = "ckv_ingestion.db"

# Function to create a table from a CSV file
def create_table_from_csv(csv_file, table_name, conn):
  """
  This function reads a CSV file and creates a table with the same name in the database.

  Args:
      csv_file (str): Path to the CSV file.
      table_name (str): Name for the table in the database.
      conn (sqlite3.Connection): Connection object to the database.
  """
  df = pd.read_csv(csv_file)
  df.to_sql(table_name, conn, index=False)  # Save DataFrame to database table

# Connect to the database
conn = sqlite3.connect(database_name)

# Loop through all CSV files (modify the filepaths as needed)
for i in range(1, 29):  # Assuming 28 CSV files (change range accordingly)
  csv_file = f"data_{i}.csv"  # Replace with your actual CSV filenames
  table_name = f"table_{i}"  # Replace with desired table names (optional)
  create_table_from_csv(csv_file, table_name, conn)

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Database '{database_name}' created successfully with tables from CSV files.")
'''



'''import pandas as pd
import sqlite3
import os

# Database name
db_name = "ckv_data.db"

# Connect to the database
conn = sqlite3.connect(db_name)

# Get all CSV files in the FFM folder
csv_files = [f for f in os.listdir("20240331") if f.endswith(".csv")]

# Loop through each CSV file
for filename in csv_files:
  # Read the CSV file
  df = pd.read_csv(os.path.join("20240331", filename))

  # Extract table name from filename (assuming filenames match table names)
  table_name = os.path.splitext(filename)[0]

  # Create table in the database
  df.to_sql(table_name, conn, index=False)

  print(f"Table '{table_name}' created from '{filename}'.")

# Close the connection
conn.close()

print(f"Database '{db_name}' created successfully.")'''



#create db from csv files


import os
import pandas as pd
import sqlite3
import codecs
import sys

# Directory containing CSV files
directory = '20233112'

# Create a SQLite database (or connect to it if it exists)
conn = sqlite3.connect('ckv23.db')
cursor = conn.cursor()

# Iterate through all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        table_name = os.path.splitext(filename)[0]  # Use the file name without extension as table name
        
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path, sep = ';', encoding='ISO-8859-1', low_memory=False)
            
            # Write the DataFrame to a SQL table
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f'Table {table_name} created successfully.')
        except Exception as e:
            print(f'Error processing file {filename}: {e}')

# Close the database connection
conn.close()

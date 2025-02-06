import sqlite3

def find_wck_in_tables(db_file):
  """
  This function connects to a database, iterates through tables, and searches for "WCK" in columns.

  Args:
      db_file (str): Path to the database file (e.g., "ckv.db").
  """
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()
  
  # Get all table names
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
  table_names = [row[0] for row in cursor.fetchall()]

  for table_name in table_names:
    # Get column names for the current table
    cursor.execute(f"PRAGMA table_info('{table_name}')")
    column_names = [row[1] for row in cursor.fetchall()]

    # Search for "WCK" in each column
    for column_name in column_names:
      query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%POS_600123%'"
      cursor.execute(query)
      if cursor.fetchone():
        print(f"Value found in column '{column_name}' of table '{table_name}'.")

  conn.close()

# Example usage
db_file = "ckv24.db"
find_wck_in_tables(db_file)


'''import sqlite3

# Connect to the database
conn = sqlite3.connect('BXR.db')

# Get a cursor object
cursor = conn.cursor()

# Get the column names from the table "ASAP"
cursor.execute("PRAGMA table_info('ASAP')")

# Print the column names
print("Columns in table ASAP:")
for row in cursor.fetchall():
    print(row[1])  # Access the column name at index 1

# Close the connection
conn.close()'''

import sqlite3

# Connect to the database
conn = sqlite3.connect('ckv.db')

# Get a cursor object
cursor = conn.cursor()

# Get the column names from the table "ASAP"
cursor.execute("PRAGMA table_info('L2_LOAN_DEPOSIT')")

# Print the column names
print("Columns in table ASAP:")
for row in cursor.fetchall():
    print(row[1])  # Access the column name at index 1

# Close the connection
conn.close()

import pandas as pd
import sqlite3

'''def get_unique_rca_values(db_engine1, db_engine2, table_name):
  """
  Fetches unique RCA values from two tables with the same name from different databases.

  Args:
    db_engine1: SQLAlchemy engine for the first database.
    db_engine2: SQLAlchemy engine for the second database.
    table_name: The name of the table in both databases.

  Returns:
    A list of unique RCA values from both tables.
  """

  # Query the first database
  query1 = f"SELECT DISTINCT RCA FROM {table_name}"
  df1 = pd.read_sql_query(query1, db_engine1)

  # Query the second database
  query2 = f"SELECT DISTINCT RCA FROM {table_name}"
  df2 = pd.read_sql_query(query2, db_engine2)

  # Combine the results and remove duplicates
  combined_df = pd.concat([df1, df2], ignore_index=True)
  unique_rca_values = combined_df['RCA'].unique().tolist()

  return unique_rca_values

# Example usage:
# Replace with your actual database connection strings and table name
db_engine1 = sqlalchemy.create_engine('your_database_connection_string1')
db_engine2 = sqlalchemy.create_engine('your_database_connection_string2')
table_name = 'GEL'

unique_rcas = get_unique_rca_values(db_engine1, db_engine2, table_name)
print(unique_rcas)'''


import sqlite3

def list_different_values(db1, db2):
  """Lists the different values found from the RCA column in two GEL tables from different databases.
  Args:
    db1_path: Path to the first database file.
    db2_path: Path to the second database file.
  """
  # Connect to both databases
  conn1 = sqlite3.connect(db1)
  conn2 = sqlite3.connect(db2)

  # Create cursors
  cur1 = conn1.cursor()
  cur2 = conn2.cursor()

  # Fetch all distinct RCA values from both tables
  cur1.execute("SELECT IDE_GL_REF, RCA_AMOUNT FROM L2_GEL_AMOUNT")
  data1 = cur1.fetchall()
  #cur1.execute("SELECT DISTINCT IDE_GL_REF FROM L2_GEL_AMOUNT")
  #rca_values1 = set(sorted(cur1.fetchall()))
  #print(rca_values1)
  cur2.execute("SELECT IDE_GL_REF, RCA_AMOUNT FROM L2_GEL_AMOUNT")
  data2 = cur2.fetchall()
  #rca_values2 = set(sorted(cur2.fetchall()))

  # Find the difference between the two sets
  #different_values = rca_values1 ^ rca_values2

  # Print the different values
  '''for value in different_values:
    print(value)'''
# Create dictionaries for efficient lookup
  '''dict1 = {row[0]: row[1] for row in data1}
  dict2 = {row[0]: row[1] for row in data2}
  # Find common IDE values with matching RCA
  common_ide = []
  for ide, rca1 in dict1.items():
    if ide in dict2 and dict2[ide] == rca1:
      common_ide.append(ide)
      # Print the common IDE values
  print(common_ide)'''


  # Close connections
  
# Create dictionaries for efficient lookup
  dict1 = {row[0]: row[1] for row in data1}
  dict2 = {row[0]: row[1] for row in data2}

  non_matching_values = []
  total_rca1 = 0
  total_rca2 = 0
# Find non-matching IDE values with different RCA
  for ide, rca1 in dict1.items():
        if ide in dict2 and dict1[ide] == dict2[ide]:
            print(f"IDE: {ide}, RCA1: {rca1}, RCA2: {dict2[ide]}")
            total_rca1 += rca1
            total_rca2 += dict2[ide]
        elif ide not in dict2:
            print(f"IDE: {ide}, RCA1: {rca1}, RCA2: None")
            total_rca1 += rca1

  for ide, rca2 in dict2.items():
        if ide not in dict1:
            print(f"IDE: {ide}, RCA1: None, RCA2: {rca2}")
            total_rca2 += rca2

  #working when GEL are the same, but diff RCA amounts
  '''for ide, rca1 in dict1.items():
    #if ide in dict2 and rca1 != dict2[ide]:
    if ide in dict2 and rca1 != dict2[ide]:   #when they are the same
      rca2 = dict2[ide]
      print(f"IDE: {ide}, RCA1: {rca1}, RCA2: {rca2}")
      total_rca1 += rca1
      total_rca2 += rca2'''
  

  print(f"Total RCA1: {total_rca1}")
  print(f"Total RCA2: {total_rca2}")
  conn1.close()
  conn2.close()
# Example usage:
db1 = "ckv23.db"
db2 = "ckv24.db"
list_different_values(db1, db2)


  # Find common IDE values with diff RCA
''' total_rca1 = 0
 total_rca2 = 0
    for ide, rca1 in dict1.items():
        if ide in dict2 and rca1 != dict2[ide]:
        rca2 = dict2[ide]
        print(f"IDE: {ide}, RCA1: {rca1}, RCA2: {rca2}")
        total_rca1 += rca1
        total_rca2 += rca2

  print(f"Total RCA1: {total_rca1}")
  print(f"Total RCA2: {total_rca2}")
  for ide, rca1 in dict1.items():
    if ide in dict2 and dict2[ide] == rca1:
      common_ide.append(ide)
      # Print the common IDE values
  print(common_ide)'''


# Find common IDE values with different RCA values --- working ok
'''total_rca1 = 0
  total_rca2 = 0
  for ide, rca1 in dict1.items():
    if ide in dict2 and rca1 != dict2[ide]:
      rca2 = dict2[ide]
      print(f"IDE: {ide}, RCA1: {rca1}, RCA2: {rca2}")
      total_rca1 += rca1
      total_rca2 += rca2

  print(f"Total RCA1: {total_rca1}")
  print(f"Total RCA2: {total_rca2}")'''   
# Find common IDE values with different RCA values
''' common_ide = set(dict1.keys()) & set(dict2.keys())
  for ide, rca1 in dict1.items():
    if ide in dict2 and rca1 != dict2[ide]:
      print(f"IDE: {ide}, RCA1: {rca1}, RCA2: {dict2[ide]}")
      total_rca1 += rca1
      total_rca2 += rca2
  print(f"Total RCA1: {total_rca1}")
  print(f"Total RCA2: {total_rca2}")'''









#compare values from IDE_GL_REF in the 2 files L2_GEL_AMOUNT from diff tables
#only when they have the same value inside RCA_AMOUNT
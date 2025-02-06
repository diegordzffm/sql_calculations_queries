import pyodbc
import sqlite3
import pandas as pd

def query_database(sql_query):

  server = 'xxxxx'
  database = 'xxxxx'
  username = 'xxxxx'
  password = 'xxxxxxx!'

  conn_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

  conn1 = sqlite3.connect(conn_string)
  conn2 = sqlite3.connect(conn_string)
  # Execute the first SQL query and create a DataFrame

  # Fetch all distinct RCA values from both tables
  #sql1 = conn.execute("SELECT contract_id FROM [RegRep].[dbo].[RegAllocDetailed_FINREP_BE_DP_5_1] WHERE lot_id = 956 AND BAS = Assets AND PUR = Credit for Consumption")
  cur1 = conn1.cursor()
  cur2 = conn2.cursor()
  
  sql1 = cur1.execute(sql_query)
  results = cur1.fetchall()


  '''data1 = cur1.fetchall()
  cur2.execute("SELECT contract_id FROM RegAllocDetailed_FINREP_BE_DP_5_1")
  data2 = cur2.fetchall()'''
  #df1 = pd.read_sql_query(sql1, conn1)
  #df2 = pd.read_sql_query(sql2, conn2)

  #cursor1 = conn.cursor()
  #cursor1.execute(sql_query)
  #results = cursor1.fetchall()
  #return results
  
  conn_string.close()

# Example usage
sql_query = "SELECT TOP 1000 * FROM RegAllocDetailed_SCHEMA_A_TER_2022_01_01 WHERE 1 = 1 AND sheet_name = '0010'AND row_name = '1125'"
#sql_query = "Use GO SELECT contract_id FROM RegAllocDetailed_FINREP_BE_DP_5_1 WHERE lot_id = '956' AND BAS = 'Assets' AND PUR = 'Credit for Consumption'"
results = query_database(sql_query)



'POS_600123', 'POS_600162', 'POS_600342' 'POS_600386', 'POS_600388', 'POS_600395', 'POS_600595', 'POS_600849', 'POS_602546', 'POS_602749', 'POS_603128', 'POS_92363', 'POS_93916')
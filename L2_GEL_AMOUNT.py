#check data inside L2_GEL_AMOUNT
#python code to check the IDE_GL_REF rows from the 2 diff rep dates
#missing
'''
'''
import sqlite3

def sql_statement(db_name):
  """Sums the values in the 'Assets' column of the 'LGT' table in the specified database file.
  Args:
    db_file: The path to the database file.
  Returns:
    The sum of the 'Assets' column, or None if an error occurs.
  """

  try:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    '''f1 = cursor.execute("SELECT SUM(RCA_AMOUNT) FROM L2_GEL_AMOUNT")
    f2 = cursor.execute("SELECT COUNT(RCA_AMOUNT) FROM L2_GEL_AMOUNT")
    f3 = cursor.execute("SELECT COUNT(IDE_GL_REF) FROM L2_GEL_AMOUNT")
    f4 = cursor.execute("SELECT COUNT(IDE_POSITION_REF) FROM L2_PRL_AMOUNT")
    f5 = cursor.execute("SELECT COUNT(RCA_AMOUNT) FROM L2_PRL_AMOUNT")
    f6 = cursor.execute("SELECT SUM(RCA_AMOUNT) FROM L2_PRL_AMOUNT")
    f7 = cursor.execute("SELECT SUM(RCA_AMOUNT) FROM L2_GEL_AMOUNT")
    f1 = cursor.execute("SELECT COUNT(RCA_AMOUNT) FROM L2_GEL_AMOUNT")
    f9 = cursor.execute("SELECT SUM(RCA_AMOUNT) FROM L2_GEL_AMOUNT")'''
    #f1 = cursor.execute("SELECT SUM(RCA_AMOUNT) FROM L2_GEL_AMOUNT")
    f1 = cursor.execute("SELECT COUNT(IDE_GL_REF) FROM L2_GEL_AMOUNT")
    #f1 = cursor.execute("SELECT COUNT(RCA_AMOUNT) FROM L2_GEL_AMOUNT")
    result = f1.fetchone()
    conn.close()
    return result[0] if result else None
  except sqlite3.Error as e:
    print(f"Error accessing database: {e}")
    return None
  
    
    #print(f"Total RCA2: {total_rca2}")

db_name = "ckv23.db"

result = sql_statement(db_name)
print(result)




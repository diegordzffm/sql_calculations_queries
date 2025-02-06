import sqlite3

def compare_ide_values(db1, db2):

  conn1 = sqlite3.connect(db1)
  conn2 = sqlite3.connect(db2)

  cur1 = conn1.cursor()
  cur2 = conn2.cursor()

  cur1.execute("SELECT IDE_GL_REF, RCA_AMOUNT FROM L2_GEL_AMOUNT")
  data1 = cur1.fetchall()

  cur2.execute("SELECT IDE_GL_REF, RCA_AMOUNT FROM L2_GEL_AMOUNT")
  data2 = cur2.fetchall()

  ide_set1 = set(row[0] for row in data1)
  ide_set2 = set(row[0] for row in data2)

  # Find IDE values in database 1 but not in database 2
  only_in_db1 = ide_set1 - ide_set2

  # Find IDE values in database 2 but not in database 1
  only_in_db2 = ide_set2 - ide_set1

  # Create dictionaries to store RCA values for each IDE
  rca_dict1 = {row[0]: row[1] for row in data1}
  rca_dict2 = {row[0]: row[1] for row in data2}

  # Print IDE values and corresponding RCA values
 # print("IDE values only in database 1:")
  #for ide in only_in_db1:
    #print(f"IDE: {ide}, RCA1: {rca_dict1[ide]}")

  #print("\nIDE values only in database 2:")
  #for ide in only_in_db2:
    #print(f"IDE: {ide}, RCA2: {rca_dict2[ide]}")

  # Calculate total RCA for each database
  #total_rca1_values = len(rca_dict1) 
  #total_rca12_values = len(rca_dict2) 
  #total_rca1 = sum(rca_dict1.values())    
  #total_rca2 = sum(rca_dict2.values())

  print(f"\nTotal RCA in database 1: {len(rca_dict1)}")
  print(f"Total RCA in database 2: {len(rca_dict2)}")
  print(f"Total db: {len(data1)}")
  print(f"Total db: {len(data2)}")

  conn1.close()
  conn2.close()


db1 = "ckv23.db"
db2 = "ckv24.db"
compare_ide_values(db1, db2)
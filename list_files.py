import os
import MySQLdb
from MySQLdb import  Error
os.chdir("/home/nilmadhab/Desktop/nlp_project/project/samples")
db = MySQLdb.connect("localhost","root","25011994","nlp" )

cursor = db.cursor()


for file in os.listdir("."):
	sql = """INSERT INTO list_docs(name) 
 	VALUES ('"""+file+"""')"""
	print sql
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except Error as error:
	   # Rollback in case there is any error
	   print error
	   db.rollback()
	print file




# disconnect from server
db.close()
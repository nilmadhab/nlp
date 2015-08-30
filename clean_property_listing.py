
import MySQLdb

db = MySQLdb.connect("localhost","root","25011994","nlp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

from bs4 import BeautifulSoup
import urllib2

sql = "select * from property_listing";

cursor.execute(sql)

data = cursor.fetchall()

# print the rows
for row in data :
	#print row[1]
	#file_name = row[1].split(".")[0]
	#print file_name
	#arr.append(file_name)
	row_id = row[0]
	proprty_type = row[2]
	proprty_type = proprty_type.replace("Property Type",'').strip(' \t\n\r')
	#print row_id,proprty_type
	sql =  " UPDATE `property_listing` SET `property_type`='"+ proprty_type + "' WHERE id = "+ str(row_id)+" "
	print sql
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
   
	#print row

	#break;

#print arr


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
	document_name = row[1]
	proprty_type = row[2]
	#Building Type,Community Name
	building_type = row[3]
	storeys = row[4]
	title = row[5]
	community_name = row[6] 
	land_size_length = row[7] 
	parking_type = row[11]

	document_name = document_name.replace(".html",'')
	proprty_type = proprty_type.replace("Property Type",'').strip(' \t\n\r')
	building_type = building_type.replace("Building Type",'').strip(' \t\n\r')
	community_name = community_name.replace("Community Name",'').strip(' \t\n\r')
	title = title.replace("Title",'').strip(' \t\n\r')
	storeys = storeys.replace("Storeys",'').strip(' \t\n\r')
	parking_type = parking_type.replace("Parking Type",'').strip(' \t\n\r')
	land_size_length = land_size_length.replace("Land Size",'').strip(' \t\n\r')
	#print row_id,proprty_type
	sql =  " UPDATE `property_listing` SET `property_type`='"+ proprty_type + "'\
	,`building_type`='"+ building_type + "',`document_name`='"+ document_name + "',`storeys`='"+ storeys + "' \
	 ,`title`='"+ title + "',`parking_type`='"+ parking_type + "' \
	 ,`land_size_length`='"+ land_size_length + "',`community_name`='"+ community_name + "'  WHERE id = "+ str(row_id)+" "
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

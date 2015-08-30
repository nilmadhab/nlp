
import MySQLdb

db = MySQLdb.connect("localhost","root","25011994","nlp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

from bs4 import BeautifulSoup
import urllib2

sql = "select * from property_details";

cursor.execute(sql)

data = cursor.fetchall()

# print the rows
for row in data :
	row_id = row[0]
	document_name = row[1]
	amenities_nearby = row[2]
	features = row[3]
	parking_type = row[4]
	total_parking_space = row[5]

	document_name = document_name.replace(".html",'')
	amenities_nearby = amenities_nearby.replace("Amenities Nearby",'').strip(' \t\n\r')
	features = features.replace("Features",'').strip(' \t\n\r')
	parking_type = parking_type.replace("Parking Type",'').strip(' \t\n\r')
	total_parking_space = total_parking_space.replace("Total Parking Spaces",'').strip(' \t\n\r')
   
	sql =  " UPDATE `property_details` SET `amenities_nearby`='"+ amenities_nearby + "'\
	,`features`='"+ features + "',`parking_type`='"+ parking_type + "' \
	,`total_parking_space`='"+ total_parking_space + "'  WHERE id = "+ str(row_id)+" "

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

#print arr

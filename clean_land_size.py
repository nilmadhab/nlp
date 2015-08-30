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
	row_id = row[0]
	land_size_length = row[7]
	land_size_length_unit = ''
	land_size_width = ''
	land_size_width_unit = ''

	if land_size_length.find("x") != -1:
		land_size_length = land_size_length.split('x')[0].strip()
		land_size_width = land_size_length.split('x')[1].strip()
		land_size_length_unit = land_size_width.split()[1]
		land_size_width_unit = land_size_length_unit


	sql =  " UPDATE `property_listing` SET `land_size_length`='"+ land_size_length + "'\
	,`land_size_length_unit`='"+ land_size_length_unit + "',`land_size_width`='"+ land_size_width + "'\
	,`land_size_width_unit`='"+ land_size_width_unit + "'  WHERE id = "+ str(row_id)+" "
	
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
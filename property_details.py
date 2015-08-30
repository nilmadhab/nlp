#arr = ["V1124248","V1124383","V1124747","V1124792","V1124814","V1125023"]
#arr = ["V1125886","W2946072","W3093246","W3124013","W3199234","W3209997"]
arr = []
import re
import MySQLdb

db = MySQLdb.connect("localhost","root","25011994","nlp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

from bs4 import BeautifulSoup
import urllib2

sql = "select * from list_docs";

cursor.execute(sql)

data = cursor.fetchall()

# print the rows
for row in data :
	#print row[1]
	file_name = row[1].split(".")[0]
	print file_name
	arr.append(file_name)
print arr

for x in arr:
	document = x+".html"
	url = "file:///home/nilmadhab/Desktop/nlp_project/pdfminer/output/"+document

	print url
	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content)
	#divs = soup.find_all("div");

	#print divs[1].text;

	spans = soup.find_all("span");

	document_name = x+".pdf"
	amenities_nearby = ''
	features = ''
	parking_type = ''
	total_parking_space = ''
	

	i = 0;
	found = False
	while(i < len(spans) ):
		#print i
		#print spans[i].text
		stri = spans[i].text
		if stri.find("Amenities Nearby") != -1:
			amenities_nearby = stri
		if re.compile("^Features").search(stri):
			features = stri
		if stri.find("Parking Type") != -1:
			parking_type = stri
		if stri.find("Total Parking") != -1:
			total_parking_space = stri
		
		
		


		i+=1
	
	
	

	#print property_type,community_name,parking_type
	#14
	# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO `property_details`(`document_name`, `amenities_nearby`, `features`, `parking_type`, `total_parking_space`) 
	                             VALUES ('"""+document_name+"""','"""+amenities_nearby+"""','"""+features+"""','"""+parking_type+"""','"""+total_parking_space+"""')"""
	
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	#break

	# disconnect from server
	

	#break

db.close()


#print soup.prettify()

#soup.find("div", { "class" : "test" },recursive=False)



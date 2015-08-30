arr = []
import MySQLdb

exception = ['11758','131776','152912','155317','342920']

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
	if  x in exception:
		continue
	document = x+".html"
	url = "file:///home/nilmadhab/Desktop/nlp_project/pdfminer/output/"+document

	print url
	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content)
	#divs = soup.find_all("div");

	#print divs[1].text;

	spans = soup.find_all("span");
	document_name = x+".pdf"
	walk_score = ''
	dependence = ''
	i = 0;
	found = False
	while(i < len(spans) ):
		stri = spans[i].text
		if stri.find("Walk Score") != -1:
			dependence = spans[i+1].text
			walk_score = spans[i+2].text
		

		i += 1

	# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO `property_score`(`document_name`, `walk_score`, `dependence`) 
	                             VALUES ('"""+document_name+"""','"""+walk_score+"""','"""+dependence+"""')"""
	
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()



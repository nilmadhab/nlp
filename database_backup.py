#arr = ["V1124248","V1124383","V1124747","V1124792","V1124814","V1125023"]
#arr = ["V1125886","W2946072","W3093246","W3124013","W3199234","W3209997"]
arr = []
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


	i = 1;
	found = False
	while(i < len(spans) ):
		print i
		print spans[i].text
		stri = spans[i].text
		if stri.find("$") != -1:
			found = True
			number = i
			break
		print "\n"
		i+=1
	if(found == False):
		continue;
	
	number -=1
	location = spans[number].text;
	price = spans[number+1].text;
	listing_id = spans[number+2].text;

	print location,price,listing_id
	#14
	# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO info(location,document,price,listing_id,street_address,city,province) 
	 VALUES ('"""+location+"""','"""+document+"""','"""+price+"""','"""+listing_id+"""','','','')"""
	print sql
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# disconnect from server
	

	#break

db.close()


#print soup.prettify()

#soup.find("div", { "class" : "test" },recursive=False)



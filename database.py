arr = ["V1124248","V1124248","V1124383","V1124747","V1124792","V1124814","V1125023"]
import MySQLdb

db = MySQLdb.connect("localhost","root","25011994","nlp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

from bs4 import BeautifulSoup
import urllib2
document = "V1125602.html"
url = "file:///home/nilmadhab/Desktop/nlp_project/pdfminer/output/V1125602.html"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

#print soup.prettify()

#soup.find("div", { "class" : "test" },recursive=False)

divs = soup.find_all("div");

print divs[1].text;

spans = soup.find_all("span");


i = 1;

while(i < 30):
	print i
	print spans[i].text
	stri = spans[i].text
	if stri.find("$") != -1:
		number = i
		break
	print "\n"
	i+=1
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
db.close()


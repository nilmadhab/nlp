#arr = ["V1124248","V1124383","V1124747","V1124792","V1124814","V1125023"]
#arr = ["V1125886","W2946072","W3093246","W3124013","W3199234","W3209997"]
arr = []
import MySQLdb

db = MySQLdb.connect("localhost","root","25011994","nlp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

from bs4 import BeautifulSoup
import urllib2
import re
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


	i = 0;
	price = ''
	listing_id = ''
	found = False
	while(i < len(spans)-1): 
		#print i,"nil"
		i+=1;

		stri = spans[i].text
		#i-=1;
		if stri.find("$") != -1 and found == False:
			location = spans[i-1].text;
			price = spans[i].text;
			found = 1;

        if stri.find("Listing ID") != -1:
        	listing_id = spans[i].text;
        	g = re.compile('(?<=:)\W*\s*[A-Za-z0-9]+').search(unicode(listing_id)).group(0)
	        g = re.sub('\W+','',g)
	        listing_id = g
        
        

	price = price.strip()

	location = location.strip()
	i_post = location.rfind(' ')
	postcode = location[(i_post+1):].strip()#POSTAL_CODE
	location = location[:i_post].strip()


	i_province = location.rfind(',')
	province = location[i_province+1:].strip()#PROVINCE
	location = location[:i_province].strip()


	i_city = location.rfind(',')
	city = location[i_city+1:].strip()#CITY
	location = location[:i_city].strip()
	street = location#STREET

	#print street,'\n',city,'\n',province,'\n',postcode,'\n',price,'\n',listing_id

		
	sql = """INSERT INTO location(document_name,price,listing_id,street_address,city,province,postal_code) 
	 VALUES ('"""+document+"""','"""+price+"""','"""+listing_id+"""','"""+street+"""','"""+city+"""','"""+province+"""','"""+postcode+"""')"""
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



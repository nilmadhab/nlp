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
#print arr

for x in arr:
        document = x+".html"
        try:
            url = "file:///home/nilmadhab/Desktop/nlp_project/new_html/"+document
            content = urllib2.urlopen(url).read()
        except:
            continue



        #print url
        

        soup = BeautifulSoup(content, "html.parser")
        #divs = soup.find_all("div");

        #print divs[1].text;

        spans = soup.find_all("p");

        document_name = x+".pdf"
        description = ''
        

        i = 0;
        found = False
        print len(spans)
        print spans[0].text
        while(i < len(spans) ):
            #print i
            #print spans[i].text
            stri = spans[i].text
            #print stri
            if stri.find("Description") != -1:
                    k = i+1
                    span = spans[k].text
                    while(k < len(spans)-1 and span.find("Details") == -1):
                        description += span.strip() + ' '
                        k += 1
                        span = spans[k].text
                    break

            i+=1

        print "description"+description
        #break
        
        #Prepare SQL query to INSERT a record into the database.
        sql = """INSERT INTO `home_details`(`document_name`, `description`) 
                                                                 VALUES ('"""+document_name+"""','"""+description+"""')"""
        print sql
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()

        #break

        #disconnect from server
        

        #break

db.close()

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import urllib2
from bs4 import BeautifulSoup
import re

url = "file:///home/nilmadhab/Desktop/nlp_project/pdfminer/output/10090774.html" 
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
spans = soup.find_all("span");
i = 0;


STYLE=''
while(i < len(spans)):
    #print i
    #print spans[i].text
    stri = spans[i].text
    if stri.find("$") != -1:
        location = spans[i-1].text;
        price = spans[i].text;
        listing_id = spans[i+1].text;
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
   
 



    i+=1





#k= soup.find_all(text=re.compile('List'))
#k= soup.find_all(text=re.compile('\$'))



#k= soup.find_all(text=re.compile('Property.Type'))
#print k[0].parent.next_sibling.text






print street,'\n',city,'\n',province,'\n',postcode,'\n',price,'\n',listing_id
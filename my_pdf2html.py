from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = HTMLConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

txt = convert('DRAS_sample_v1_20150605/00390948.pdf',pages=[1,2,3]);
import re 
from bs4 import BeautifulSoup
import urllib2
soup = BeautifulSoup(txt)
for hidden in soup.find_all(style=re.compile('\w*invisible\w*')):
    hidden.decompose()
doc = 'op/my_output.html'
Html_file= open(doc,"w")
Html_file.write(soup.prettify().encode('utf8'))
Html_file.close()



url = "file:////home/sid95/Projects/nlp_proj/" + doc
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
spans = soup.find_all("span");
i = 1;
PROPERTY_TYPE=''
BUILDING_TYPE=''
STOREYS=''
LAND_SIZE =''
PARKING_TYPE=''
TITLE=''
AGE=''
COMMUNITY_TYPE=''
AMENITIES=''
FEATURES=''
PARKING_SPACE_TOTAL=''
BASEMENT_F =''
BASEMENT_T='' 
NO_BATHROOMS=''
BED_ABOVE_GRADE=''
BED_BELOW_GRADE=''
COOLING=''
EXTERIOR_FINISH=''
HEATING_FUEL=''
HEATING_FUEL=''
FIREPLACE_TYPE=''
FIREPLACE_FUEL=''

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
    stri = stri.lower().strip()
    try:
        data = spans[i].text.strip().split('\n').pop().strip()
        num_extract = re.search(r'\d+',data)
        if num_extract is None:
            num_extract=''
        else:
            num_extract=int(num_extract.group())
    except:
        print 'ignore'
    if re.compile(r'property[\S\s]{1,3}type').search(stri):
        PROPERTY_TYPE = data
        KKK=spans[i].text
        print spans[i].text.split('\n')
    elif stri.find("building type") != -1:
        BUILDING_TYPE = data
    elif stri.find("storeys") != -1:
        STOREYS = num_extract
    elif stri.find("land size")!=-1:
        LAND_SIZE = data
    elif stri.find("parking type")!=-1:
        PARKING_TYPE = data
    elif re.compile('title').search(stri):
        TITLE = data
    elif re.compile('age.of.building').search(stri):
        AGE = num_extract
    elif re.compile('built.in').search(stri):
        AGE = 2015 - num_extract
    elif re.compile('community.(name|type)').search(stri):
        COMMUNITY_TYPE =  data
    elif re.compile('amenities.nearby').search(stri):
        AMENITIES = data
    elif re.compile('^feature').search(stri):
        FEATURES = data
    elif re.compile('total.parking.spaces').search(stri):
        PARKING_SPACE_TOTAL = num_extract
    elif re.compile('basement.features').search(stri):
        BASEMENT_F = data
    elif re.compile('basement.type').search(stri):
        BASEMENT_T = data
    elif re.compile(r'bathrooms[\S\s]{1,3}(total)*$').search(stri):  
        NO_BATHROOMS = num_extract
    elif re.compile('bedrooms.above.grade').search(stri):  
        BED_ABOVE_GRADE = num_extract
    elif re.compile('bedrooms.below.grade').search(stri):  
        BED_BELOW_GRADE = num_extract
    elif re.compile('cooling').search(stri):  
        COOLING = data
    elif re.compile('exterior.finish').search(stri):  
        EXTERIOR_FINISH = data
    elif re.compile('heating.fuel').search(stri):
        HEATING_FUEL = data
    elif re.compile('heating.type').search(stri):
        HEATING_TYPE = data 
    elif re.compile('style').search(stri):
        STYLE = data 
    elif re.compile('fireplace.type').search(stri):
        FIREPLACE_TYPE = data 
    elif re.compile('fireplace.fuel').search(stri):
        FIREPLACE_FUEL = data 




    i+=1





#k= soup.find_all(text=re.compile('List'))
#k= soup.find_all(text=re.compile('\$'))



#k= soup.find_all(text=re.compile('Property.Type'))
#print k[0].parent.next_sibling.text






print street,'\n',city,'\n',province,'\n',postcode,'\n',price,'\n',listing_id
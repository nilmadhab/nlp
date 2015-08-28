from bs4 import BeautifulSoup
import urllib2

url = "file:///home/nilmadhab/Desktop/nlp_project/pdfminer/output/V1125447.html"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print soup.prettify()
# python will convert \n to os.linesep
import os
import MySQLdb
from MySQLdb import  Error
#os.chdir("/home/nilmadhab/Desktop/nlp_project/project/samples")
db = MySQLdb.connect("localhost","root","25011994","nlp" )

cursor = db.cursor()

sql = "select * from list_docs";

cursor.execute(sql)

data = cursor.fetchall()

# print the rows
for row in data :
	#print row[1]
	file_name = row[1].split(".")[0]
	print file_name
	line = 'pdf2txt.py -o  pdfminer/output/'+file_name+'.html  project/samples/'+file_name+'.pdf\n'
	f = open('shell.sh','a')
	f.write(line)
	f.close()
	print line

	#break;


#
#f.write('pdf2txt.py -o  pdfminer/output/dynamic.html  project/samples/10093137.pdf\n') 
# f = open('shell.txt','w')
# f.write(line)
# f.close()

db.close()
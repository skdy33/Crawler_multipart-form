from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import csv
import Crawler
from subpage import subpg

url1 = 'http://publichealth.lacounty.gov/phcommon/public/eh/rating/ratesearchaction.cfm'
crawler = Crawler.Crawler()

data = {'dba':'a','address':'','city':'','zipcode':'','type':'','score':'','sort':'dba','B1':'Submit'}
#page = crawler.Get(url1,data)
crawler.addHeader('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22')
crawler.addHeader('Referer', 'http://publichealth.lacounty.gov')

data1= {'dba':'','address':'','city':'','zipcode':'','type':'Restaurant','score':'','sort':'dba','B1':'Submit'}

page = crawler.Post(url1, data1,True)
c1=csv.writer(open("LA.csv","ab"))
i=len(list(csv.reader(open('LA.csv'))))
i=246
#print page 
start_value=1
list_to_write = []
list_to_print=[]

list_to_write.append(page)

regex = "<tr>([\w\W]*?)</tr>"
regex_td = "<td align=\"left\" valign=\"top\"\s*?>\s*?([^<>]*?)<br>[^<>]*?</td>"
regex_input="<input type=\"hidden\" name=\"dsiteid\" value=\"([\w\W]*?)\">"
matches = re.findall(regex, page, re.IGNORECASE)


if(matches):
	for match in matches:
			
			
			matches2 = re.findall(regex_td,match.strip())
			matches3 = re.findall(regex_input,match.strip())
			
			break
					   
			if(matches2):
				print "matches3:" ,matches3
				if not (matches3):
					print "Terrrible things happened"
					break
				
				#list_to_print.append(i)
				for match2 in matches2:
					list_to_print.append(match2.strip())
   
				list_to_print[0]=list_to_print[0]
				e=subpg()
				#add=e.parser(start_value,matches3)
				add=e.parser(start_value,matches3)
 
				
				#c1.writerow(list_to_print)
				print list_to_print
				#list_to_print=[]
				
				for item in add:
					list_to_print[4]=item[0]
					list_to_print[5]=item[1]
					#c1.writerow(list_to_print)
				list_to_print=[]
											
# rerun from start_value=4401
start_value=24701

while True:
	
	data1= {'score':'','row':'100','start':start_value,'dba':'','type':'Restaurant','city':'','zipcode':'','sort':'dba','surcheck':'no','address':'','alphalist':''}
	page = crawler.Post(url1, data1,True)
	start_value=start_value+100
	list_to_write.append(page)
	#print page
	matches = re.findall(regex, page, re.IGNORECASE)
	print "one more Jerry here"
	if(matches):
		for match in matches:
			matches2 = re.findall(regex_td,match.strip())
			matches3 = re.findall(regex_input,match.strip())
			
			
			if(matches2):
				print "matches3:" ,matches3
				if not (matches3):
					print "Terrrible things happened"
					break
				
				for match2 in matches2:
					list_to_print.append(match2.strip())
					#print list_to_print
				list_to_print[0]=list_to_print[0][1:-1]
				e=subpg()
				
				while True:
					try:
						add=e.parser(start_value,matches3)    
					except:
						continue
					break
				  
				c1.writerow(list_to_print)
				#list_to_print=[]
				print list_to_print
				
				for item in add:
					list_to_print[4]=item[0]
					list_to_print[5]=item[1]
					c1.writerow(list_to_print)
					print list_to_print
				list_to_print=[]
	i=i+1
	print "page:",i
	
	if(page.find('Next')== -1):    
		break


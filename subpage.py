from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import csv
import Crawler

 
class subpg:
  def parser(self, start_value,dsiteid):
    url1 = 'http://publichealth.lacounty.gov/phcommon/public/eh/rating/ratedetail.cfm'
    
    crawler = Crawler.Crawler()
    crawler.addHeader('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22')
    crawler.addHeader('Referer', 'http://publichealth.lacounty.gov/phcommon/public/eh/rating/ratesearchaction.cfm')
    crawler.addHeader('Cookie', '__utma=228353666.637471230.1393074196.1393480028.1393510444.7; __utmz=228353666.1393480028.6.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=228353666; style=null')
    
    sv=str(start_value)
    dd=str(dsiteid[0])
    
    data1= {'start':sv,'dsiteid':dd,'type':'Restaurant','city':'','address':'','zipcode':'','alphalist':'','surcheck':'no','sort':'dba','score':'','dba':''}
    #data1= {'start':'1','dsiteid':'0916113364','type':'Restaurant','city':'','address':'','zipcode':'','alphalist':'','surcheck':'no','sort':'dba','score':'','dba':''} 
    page = crawler.Post(url1, data1,True)
    c1=csv.writer(open("LA.csv","ab"))
    i=len(list(csv.reader(open('LA.csv'))))
    list_to_write = []
    list_to_write.append(page)
     
    regex =  "<tr>([\w\W]*?)</tr>"
    regex_1 = "<td align=\"left\" width=\"33%\" valign=\"top\"([\w\W]*?)</td>"
    regex_2 = "<td width=\"10%\" valign=\"top\"([\w\W]*?)</td>"
    regex_3 = "<td width=\"57%\" valign=\"top\"([\w\W]*?)</td>"
    regex_input="<input type=\"hidden\" name=\"dsiteid\" value=\"([\w\W]*?)\">"
    matches = re.findall(regex, page, re.IGNORECASE)
    #print len(matches)
    
    list_to_write=[]
    
    if(matches):
      for match in matches:
        matches2 = re.findall(regex_1,match.strip())
        matches3 = re.findall(regex_2,match.strip())
        matches4 = re.findall(regex_3,match.strip())
        if(matches2):
          #print match
          #print "match is above"
          temp=match.split('\n')
         
          t1 = temp[3][-16:-6]
          t2 = temp[6][-8:-6]
          t3 = temp[8][-3:-2]
          if(t2=='00'):
           t2='100'
          h=[t1,t2,t3]
          #print h
          list_to_write.append(h)
      return list_to_write

                  

import urllib2
import urllib
import re
from cookielib import CookieJar
import HTMLParser
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

class Crawler(object):
    cookiejar = ''
    req_opener = None
    customHeaders = []
    headerForPost = {}
    htmlparser = None
    def __init__(self):
        self.cookiejar= CookieJar()
        self.htmlparser = HTMLParser.HTMLParser()
        self.req_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiejar))
        self.req_opener.addheaders = []
        self.addHeader('User-Agent',"Google Chrome")
        
    def getHeaderForPost(self):
        return self.headerForPost
        
    def getCookies(self):
        cookie_value = ''
        for cookie in self.cookiejar:
            cookie_value = cookie_value + cookie.name + "=" + cookie.value +"; "
        return cookie_value
    def addHeader(self,name,value):
        try:
            self.req_opener.addheaders.index(name)
        except ValueError:            
            self.customHeaders.append((name,value))
        try:
            if(not(self.headerForPost.has_key(name))):
                self.headerForPost[name]=value
            else:
                self.headerForPost[name] = value
        except:
            print "Error"
    def addHeaders(self):
        self.req_opener.addheaders = []
        for headers in self.customHeaders:
            #print headers
            self.req_opener.addheaders.append(headers)
                
    def Get(self,url,data=None):        
        self.addHeaders()
        #print self.req_opener.addheaders
        response = self.req_opener.open(url,data)
        content = response.read()
        return content
#        print self.cookiejar
        #print content
    def Post(self,url,data=None,multipart=False):
        content = ''
        headers = self.getHeaderForPost()
        if(multipart == True):            
            register_openers()
            values, new_header = multipart_encode(data)
            for header_key in headers:
                new_header[header_key] = headers[header_key]
            
            request = urllib2.Request(url,values,new_header)
            self.cookiejar.add_cookie_header(request)
            content = urllib2.urlopen(request).read()
        else:
            values = urllib.urlencode(data)
            request = urllib2.Request(url,values,headers)
            self.cookiejar.add_cookie_header(request)
            content = urllib2.urlopen(request).read()
        return content


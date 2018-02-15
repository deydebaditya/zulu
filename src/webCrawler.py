import requests as request
from bs4 import BeautifulSoup as bs
import re

#queue for storing the visited links
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def zulu(start_url):
    q = Queue()
    q.enqueue(start_url)
    visited = set()
    listed = set()
    while(q.isEmpty() == False):
        url = q.dequeue()
        print("Popped: "+url)
        visited.add(url)
        source_code = request.get(url)
        plain_text = source_code.text

        formattedSource = bs(plain_text)
              
        for link in formattedSource.findAll('a'):               #if there are multiple <a> tags from which we want to extract href and text values.
                                                                #We use the find_All() method which returns a collection of elements
            if(link.get('href') is "#" or link.get('href') is "" or link.get('href') is " " or visited.__contains__(link.get('href')) or listed.__contains__(link.get('href'))):
                continue
            listed.add(link.get('href'))
            temp = link.get('href')
            #print(temp)
            if("mailto" in temp):
                continue
            if(("http" not in temp)):
                if("https" not in temp):
                    print('Not found URL')
                    q.enqueue(start_url + "/" + link.get('href'))
                    print("Crawled URL: " + start_url + "/" + link.get('href'))
            else:
                q.enqueue(link.get('href'))
                print("Crawled URL: " +link.get('href'))

def __main__():
    print('Welcome to ZULU!')
    print('I am an Alpha web crawler developed by Debaditya Dey...')
    print('He made me out of sheer excitement and frustration that he didn\'t code something cool for many days')
    print('I am just a 10 minute build, so I may crash sometimes!')
    print('Debaditya promises to make me better in the coming days')
    print('You are welcome to contribute and drop pull requests on his github repo')
    print('Till then, you can fiddle around and enjoy with me')
    print('###################################\n\n')
    start_url = str(input('Enter the full URL from which I should start crawling:'))
    zulu(start_url)

__main__()

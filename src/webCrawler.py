import requests as request
from bs4 import BeautifulSoup as bs

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
    while(q.isEmpty() == False):
        url = q.dequeue()
        source_code = request.get(url)
        plain_text = source_code.text
        formattedSource = bs(plain_text)
        for link in formattedSource.findAll('a'):
            href = start_url + "/"+ link.get('href')
            q.enqueue(href)
            print(href)

def __main__():
    print('Welcome to ZULU!')
    print('I am an Alpha web crawler developed by Debaditya Dey...')
    print('He made me out of sheer excitement and frustration that he didn\'t code something cool for many days')
    print('I am just a 10 minute build, so I may crash sometimes!')
    print('Debaditya promises to make e better in the coming days')
    print('You are welcome to contribute and drop pull requests on his github repo')
    print('Till then, then you can fiddle around and enjoy with me')
    print('###################################\n\n')
    start_url = str(input('Enter the full URL from which I should start crawling:'))
    zulu(start_url)

__main__()
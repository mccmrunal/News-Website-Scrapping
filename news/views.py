import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

desc = []
desc2 = []



def home(request):
    url = 'http://feeds.bbci.co.uk/news/rss.xml'
    resp = requests.get(url)

    soup = BeautifulSoup(resp.content,features= "xml")

    items = soup.findAll('item')

    newlis = dict()
    for item in items:
        newlis['story']  = (item.title.text)
        newlis['desc']   =(item.description.text)
        newlis['link']  =(item.link.text)
        desc.append(dict(newlis))

    return render(request, 'news/news.html', {'items':desc})

def hindustantimes(request):

    url  = 'https://www.hindustantimes.com/rss/topnews/rssfeed.xml'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    resp = requests.get(url,headers = agent)
    soup = BeautifulSoup(resp.content,features='xml')
    items  = soup.findAll('item')
    dict2 = dict()
    for item in items:
        dict2['story']  = (item.title.text)
        dict2['desc']   =(item.description.text)
        dict2['img']  =(item.find('media:content')['url'])
        desc2.append(dict(dict2))



    return render(request,'news/hindustan.html',{'items2':desc2})

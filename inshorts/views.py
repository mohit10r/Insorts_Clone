from django.shortcuts import render
import urllib.request
import bs4 as bs
from bs4 import BeautifulSoup
import re
from inshorts.models import Headline

headline1 = []
content1 = [] 


def read(request):
    """Scrap content and render news.html"""

    headline = []
    content = []
    image_url = []
    
    source = urllib.request.urlopen('https://inshorts.com/en/read').read()
    soup = bs.BeautifulSoup(source,'html.parser')



    for div in soup.find_all('div',{'class':'news-card-title news-right-box'}):
        headline.extend(div.find_all('span', {'itemprop' : 'headline'}))


    for div in soup.find_all('div',{'class':'news-card-content news-right-box'}):    
        content.extend(div.find_all('div',{'itemprop':'articleBody'}))

  

    for i in range(len(headline)):
        remove_html_tags_headline(str(headline[i]))

    for i in range(len(content)):
        remove_html_tags_content(str(content[i]))

    space30 = " "*30    

    res = [[i + space30 +  j] for i, j in zip(headline1, content1)]

    return render(request,'news.html',{'res':res})

def remove_html_tags_headline(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    headline1.append(re.sub(clean, '', text))

def remove_html_tags_content(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    content1.append(re.sub(clean, '', text))    









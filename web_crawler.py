from bs4 import * # To find the hyperlinks
import requests # To make http requests to a site
from argparse import * #To make a CLI
import os 
import re
import mail
from urllib.parse import urlparse 

parser=ArgumentParser()
parser.add_argument("url",help="Enter the URL you want to scrape")
parser.add_argument("depth",help="Enter the depth for search")
p=parser.parse_args()

'''The usearch function searches the html source code for
links and recursively searches further for links based on
given depth'''
l=[]

def usearch(u,depth):
    mail.harv(title,u)
    if depth==int(p.depth):
        return 0
    r=requests.get(u)
    soup=BeautifulSoup(r.content,'html.parser')
    links= soup.find_all('a')
    
    for link in links:
        link=link.get('href')
        if link!='#' and link!=None:
            l.append(link)
    for link in l:
        if ("https://" or "http://")not in link:
            link = p.url+link
            if link in l:
                continue
            f.write(link+"\n")
        else:
            if link in l:
                continue
            f.write(link+"\n")
            usearch(link,depth+1)


title=urlparse(p.url)
title=title.netloc
os.system("mkdir {}".format(title)) 
os.system("touch {}/domains.txt".format(title))
f= open("{}/domains.txt".format(title),"a")

usearch(p.url,0)

f.close()              

    

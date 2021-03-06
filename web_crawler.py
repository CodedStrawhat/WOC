from bs4 import * # To find the hyperlinks 
import requests # To make http requests to a site 
from argparse import * #To make a CLI 
import os 
import re 
import mail 
import contact
from urllib.parse import urlparse 

parser=ArgumentParser() 
parser.add_argument("url",help="Enter the URL you want to scrape") 
parser.add_argument("depth",help="Enter the depth for search") 
parser.add_argument("-e",action = 'store_true',help="Option for email harvesting") 
parser.add_argument("-c",action = 'store_true',help="Option for contact harvesting")
p=parser.parse_args() 

'''The usearch function searches the html source code for
links and recursively searches further for links based on
given depth'''

mails=set()
contacts=set()
n_w_c=set()
n_w_m=set()
l=[]
def usearch(u,depth):
    if p.e:
        mail.harv(u,fil_1,mails,n_w_m)
    if p.c:
        contact.harv(u,fil_2,contacts,n_w_c)
    if depth==int(p.depth):
        return 0
    r=requests.get(u)
    soup=BeautifulSoup(r.content,'html.parser')
    links= soup.find_all('a')
    for link in links:
        link=link.get('href')
        if link!='#' and link!=None:
            if ("https://" or "http://")not in link:
                link = p.url+link
            if link not in l:
                l.append(link)
    
    for link in l:
        f.write(link+"\n")
        usearch(link,depth+1)

title=urlparse(p.url)
title=title.netloc
os.system("mkdir {}".format(title)) 
os.system("touch {}/domains.txt".format(title))
f= open("{}/domains.txt".format(title),"a")
if p.e:
    os.system("touch {}/emails.txt".format(title))
    fil_1= open("{}/emails.txt".format(title),"a")
if p.c:
    os.system("touch {}/contacts.txt".format(title))
    fil_2= open("{}/contacts.txt".format(title),"a")
usearch(p.url,0)
f.close()
if p.e:
    fil_1.close()         
if p.c:
    fil_2.close()
    

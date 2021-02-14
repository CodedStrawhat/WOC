from bs4 import * # To find the hyperlinks
import requests # To make http requests to a site

url=input("Enter your url:")

def usearch(u):
    r=requests.get(u)
    soup=BeautifulSoup(r.content,'html.parser')
    links= soup.find_all('a')
    l=set()
    for link in links:
        link=link.get('href')
        if link!='#' and link!=None:
            l.add(link)
    for link in l:
        if ("https://" or "http://")not in link:
            print(u+link)
        else:
            print(link)
            usearch(link)
usearch(url)
                
    
    

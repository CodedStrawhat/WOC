from bs4 import * # To find the hyperlinks
import requests # To make http requests to a site
from argparse import * #To make a CLI



parser=ArgumentParser()
parser.add_argument("url",help="Enter the URL you want to scrape")
parser.add_argument("depth",help="Enter the depth for search")
p=parser.parse_args()

'''The usearch function searches the html source code for
links and recursively searches further for links based on
given depth'''

def usearch(u,depth):
    if depth==int(p.depth):
        return 0
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
            usearch(link,depth+1)
            
usearch(p.url,0)
                
    
    

import re 
import requests

def harv(u,fil_2):
    r=requests.get(u)
    reg=r"\+91\d{10}|\d{10}"
    l=set() 
    for match in re.finditer(reg, r.text):
        l.add(match.group())
    for i in l:
        fil_2.write(i+'\n')


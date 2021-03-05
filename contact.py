import re 
import requests

def harv(u,fil_2,l,no_write):
    r=requests.get(u)
    reg=r"\+91\d{10}|\d{10}"
    for match in re.finditer(reg, r.text):
        l.add(match.group())
    ld=l.difference(no_write)
    for i in ld:
        fil_2.write(i+'\n')
        no_write.add(i)        


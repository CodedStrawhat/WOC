import re 
import requests

def harv(u,fil_2,l,no_write):
    r=requests.get(u)
    reg=r"(\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14})|d{10}"
    for match in re.finditer(reg, r.text):
        l.add(match.group())
    ld=l.difference(no_write)
    for i in ld:
        fil_2.write(i+'\n')
        no_write.add(i)        


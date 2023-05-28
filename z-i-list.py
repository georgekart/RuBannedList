import numpy as np
import sys
import pandas as pd
import requests

url = "https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv"

c=pd.read_csv(url,delimiter=";",encoding='windows-1251',skiprows=1,header=None)
c = c.replace({np.nan:None})
data=c.values.tolist()

length=len(data)
#gets the length of the csv file

domain=[None]*length
IPs=[None]*length
for i in range(0,length):
    IPs[i]=data[i][0]
    domain[i]=data[i][1]
#creates the list of domain names and IPs    

dom=list(filter(None,domain))
IPfull=list(filter(None,IPs))
#removes the empty entries
IPconc=" ".join([str(item) for item in IPfull])
IPspaced=IPconc.replace('|',' ')
IPsplit=IPspaced.split(' ')
#adds IP entries with multiple addresses as an individual entry

du=np.unique(dom)
iu=np.unique(IPsplit)
#removes duplicates

with open('domains.txt', 'w') as f:
    for line in du:
        f.write(f"{line}\n")
        
with open('IPs.txt', 'w') as f:
    for line in iu:
        f.write(f"{line}\n")
#Writes domains to domains.txt and IPs to IPs.txt

for i in range(0,len(du)):
        if(du[i][0]=="*" and du[i][1]=="."):
            du[i]=du[i][2:]
        else:
            du[i]="full:"+du[i]
            
with open('category-banned-ru', 'w') as f:
    for line in du:
        f.write(f"{line}\n")
        
#Writes domain list to domainlist.txt

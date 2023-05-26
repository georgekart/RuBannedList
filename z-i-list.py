import csv
import numpy as np
import sys
import csv

csv.field_size_limit(sys.maxsize)

file = open("dump.csv","r",encoding='windows-1251')
data = list(csv.reader(file,delimiter=";"))
file.close()

length=len(list(data))
#gets the length of the csv file

domain=[None]*length
IPs=[None]*length
for i in range(1,length):
    IPs[i]=data[i][0]
    domain[i]=data[i][1]
#creates the list of domain names    

dom=list(filter(None,domain))
IPfull=list(filter(None,IPs))
#removes the empty domain list
IPconc=" ".join([str(item) for item in IPfull])
IPspaced=IPconc.replace('|',' ')
IPsplit=IPspaced.split(' ')


du=np.unique(dom)
iu=np.unique(IPsplit)
#removes duplicates

with open('domains.txt', 'w') as f:
    for line in du:
        f.write(f"{line}\n")
        
with open('IPs.txt', 'w') as f:
    for line in iu:
        f.write(f"{line}\n")
import numpy as np
import sys
import pandas as pd
import requests
import logging
import logging.handlers
import os
import urllib
import gzip

def create_lists():
    urllib.request.urlretrieve("https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv.gz","dump.csv.gz")
    with gzip.open('dump.csv.gz','rb') as dump:
        c=pd.read_csv(dump,delimiter=";",encoding='windows-1251',skiprows=1,header=None,usecols=[0,1])
        
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

    du2=du.copy()
    iu2=iu.copy()

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

        
    #Writes banned domain list to category-banned-ru

    for i in range(0,len(du2)):
            if(du2[i][0]=="*" and du2[i][1]=="."):
                du2[i]="DOMAIN-SUFFIX,"+du2[i][2:]
            else:
                du2[i]="DOMAIN,"+du2[i]

            
    for i in range(0,len(iu2)):
        iu2[i]="IP-ASN,"+iu2[i]  
              
    with open('ruvpn.conf', 'w') as f:
        for line in du2:
            f.write(f"{line}\n")

    with open('ruvpn', 'w') as f:
        for line in du2:
            f.write(f"{line}\n")
        for line in iu2:
            f.write(f"{line}\n")
            
    #Writes rule list to ruvpn.conf
    
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    create_lists()   

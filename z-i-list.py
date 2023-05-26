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

column=[None]*length
for i in range(1,length):
    column[i]=data[i][1]
#creates the list of domain names    

col=list(filter(None,column))
#removes the empty domain list

cu=np.unique(col)
#removes duplicates

with open('domains.txt', 'w') as f:
    for line in cu:
        f.write(f"{line}\n")
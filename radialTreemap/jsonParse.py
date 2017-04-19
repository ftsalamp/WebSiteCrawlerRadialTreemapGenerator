import json

with open('radial1.json') as data_file:    
    data = json.load(data_file)
newFile=open('radial.json','w')

for i in range(len(data)):
    if i is not 0:
        curLink = data[i]
        curLink["referer"] =curLink["referer"][2:]
        curLink["referer"] =curLink["referer"][:len(curLink["referer"])-1]
        data[i]=curLink
data[0]=""
temp=str(data)
temp=temp[5:]
temp="["+temp
newFile.write(temp)
newFile.close

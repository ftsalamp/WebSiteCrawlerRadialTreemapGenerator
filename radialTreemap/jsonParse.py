import json

with open('radial1.json') as data_file:    
    data = json.load(data_file)
newFile=open('radial.json','w')

for i in range(len(data)):
    if i is not 1:
        curLink = data[i]
        curLink["referer"] =curLink["referer"][2:]
        curLink["referer"] =curLink["referer"][:len(curLink["referer"])-1]
        data[i]=curLink
newFile.write(str(data))
newFile.close

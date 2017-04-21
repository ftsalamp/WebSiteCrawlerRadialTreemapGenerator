import json

with open('radial12.json') as data_file:    
    data = json.load(data_file)
newFile=open('radial1.json','w')
flag=0
if "web.archive.org" in data[0]["url"]:
    flag=-1
for i in range(len(data)):
    if i is not flag:
        curLink = data[i]
        curLink["referer"] =curLink["referer"][2:]
        curLink["referer"] =curLink["referer"][:len(curLink["referer"])-1]
        if flag==-1:
            if "https:"in curLink["referer"]:
                curLink["referer"]=curLink["referer"][43:]
            else:
                curLink["referer"]=curLink["referer"][42:]
            if "https:"in curLink["url"]:
                curLink["url"]=curLink["url"][43:]
            else:
                curLink["url"]=curLink["url"][42:]
        data[i]=curLink

if flag==0:
    data[0]=""
    temp=str(data)
    temp=temp[5:]
    temp="["+temp
else:
    temp=str(data)
newFile.write(temp)
newFile.close

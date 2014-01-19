import xmltodict,json,io
fileX = io.open("database.xml", 'r')
o = xmltodict.parse(fileX.read())
w=open("data.json","w")
w.write(json.dumps(o))

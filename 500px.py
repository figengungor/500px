import urllib, urllib2
link = raw_input("Enter the link: ")
name = raw_input("And name: ")
f = urllib.urlopen(link)
pageResource = f.read()
pattern="{\"size\":2048,\"url\":"
start = pageResource.find(pattern)+20
end = pageResource.find("\"", start+2)

imgLink = pageResource[start:end]

imgLink=imgLink.replace("\\", "")          
print(imgLink)

urllib.urlretrieve(imgLink, name+".jpg")

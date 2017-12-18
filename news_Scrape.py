from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import dryscrape
import time

url="http://gadgets.ndtv.com/?pfrom=home-header-globalnav"

sess = dryscrape.Session()
sess.visit(url)
time.sleep(5)
page_html = sess.body()
page_soup=soup(page_html,"html.parser")

containers1=page_soup.find_all('div',class_="thumb")
containers2=page_soup.find_all('div',class_="caption")

item1 =[]
item2=[]

for container in containers1:
	img=container.img["src"]
	item1.append(img)

for container in containers2:
	text=container.text
	item2.append(text)

for i in range(0,len(item1)):
        print (item1[i]+" : " + item2[i])
	
if len(item1)==len(item2):
	print ("All data Extracted")
else:
        print ("Not all found")

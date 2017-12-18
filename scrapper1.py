
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()

page_soup=soup(page_html,"html.parser")
containers=page_soup.find_all('div',class_="item-container")
filename="products.csv"
f= open(filename,"w")

headers="brand, product_name, Shipping\n"
f.write(headers)

for container in containers:
    brand=container.div.div.a.img["title"]
    title=container.find_all("a",class_="item-title")
    product_name=title[0].text
    shipping_container=container.find_all("li",class_="price-ship")
    shipping= shipping_container[0].text.strip()
    
    print ("Brand: " + brand)
    print ("Product:  " + product_name)
    print ("Shipping: " + shipping)
    f.write(brand +","+product_name.replace(",","|") + ","+shipping.replace(",","") +"\n" )
f.close()

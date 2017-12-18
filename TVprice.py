from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

def getdata(ch,pages,filename):
    filename=filename
    f=open(filename,"w")

    headers="Sr. No, Item,Price,Shipping Price\n"
    f.write(headers)
    c=0
    urls=[pages+2]
    urls[0]=""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    if ch==1:
        for i in range (1,pages+1):
            url="https://www.newegg.com/LCD-LED-Monitors/SubCategory/ID-20/Page-"+str(i)+"?Tid=160979&PageSize=36&order=BESTMATCH"
            urls.append(url)
            print (url)
    elif ch==2:
        for i in range (1,pages):
            url="https://www.newegg.com/Gaming-Keyboards/SubCategory/ID-3523/Page-"+str(i)+"?Tid=160908&PageSize=36&order=BESTMATCH"
            urls.append(url)
            print (url)

    
    for i in range(1,len(urls)):
        my_url=urls[i]
        print(my_url)

        uClient=requests.get(my_url,headers=headers)
        
        page_html=uClient.text
        
       
        page_soup=soup(page_html,"html.parser")
        print(page_soup)
        containers=page_soup.find_all("div",class_="item-container")
       
        for container in containers:
            print("inside Container")
            c+=1
            if container.a.img["alt"]:
                item=container.a.img["alt"].replace(","," ")
                item=item.replace(";","")
            else:
                item=container.div.div.a.img["alt"].replace(","," ")
                item=item.replace(";","")
                
            if container.find_all("li",class_="price-current"):
                price_block=container.find_all("li",class_="price-current")
                price = price_block[0].text.strip()
                price= price.replace("|","")
                price=price.strip()
            else:
                price="not specified"

                
            if container.find_all("li", class_="price-ship"):
                ship_block=container.find_all("li", class_="price-ship")
                ship = ship_block[0].text.strip()

            else:
                ship="not specified"

            print("Sr.No:" + str(c))
            print("Name: " + item.replace("\"","in"))
            print("Price: "+ price[0:7])
            print("Shipping"+ship)
            f.write(str(c).replace(","," ")+","+item.replace(","," ")+","+price[0:8].replace(",","")+","+ship+"\n")
    f.close()

def main():
    print ("__________________Welcome to Web Crawler 4.20____________")
    print ("\n"*4)
    print ("The Site being crawled here is www.newegg.com ")
    print ("\n"*2)
    print ("Choose the data you want to grab:")
    print ("1.TV")
    print ("2.Gaming KeyBoard")
    ch= int(input("Enter Your Choice: "))
    pages=int(input("pages would u like to scrape? "))
    filename=input("Enter a file name to get the data on: ")
    getdata(ch,pages,filename)



if __name__=='__main__':
    main()

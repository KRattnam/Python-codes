import urllib2

import bs4


def findItem(itemName):
    itemName.replace(" ", "+")
    link = 'http://www.flipkart.com/search/a/all?query= {0}&vertical=all&dd=0&autosuggest[as]=off&autosuggest[as-submittype]=entered&autosuggest[as-grouprank]=0&autosuggest[as-overallrank]=0&autosuggest[orig-query]=&autosuggest[as-shown]=off&Search=%C2%A0&otracker=start&_r=YSWdYULYzr4VBYklfpZRbw--&_l=pMHn9vNCOBi05LKC_PwHFQ--&ref=a2c6fadc-2e24-4412-be6a-ce02c9707310&selmitem=All+Categories'.format(
        itemName)
    r = urllib2.Request(link, headers={"User-Agent": "Python-urlli~"})
    try:
        response = urllib2.urlopen(r)
    except:
        print ("Internet connection error")
        return
    thePage = response.read()
    soup = bs4.BeautifulSoup(thePage)

    firstBlockSoup = soup.find('div', attrs={'class': 'product-unit'})
    if not firstBlockSoup:
        firstBlockSoup = soup.find('div', attrs={'class': 'size1of4 fk-medium-atom unit'})
        if not firstBlockSoup:
            print ("Item Not Found")
            

    print ("Item found")
    return


findItem("galaxy s advance")
findItem("Giordano Analog Watch")
findItem("nosuchitemfound")

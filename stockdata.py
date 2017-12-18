import urllib
import re

htmlfile=urllib.urlopen("https://finance.yahoo.com/quote/AAPL?p=AAPL")

htmltext = htmlfile.read()

regex = '<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)">(.+?)</span>'
pattern = re.compile(regex)

price = re.findall(pattern,htmltext)

print price

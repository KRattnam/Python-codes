import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker 

import tkinter as tk
from tkinter import ttk

import urllib
import json

import pandas as pd
import numpy as np



DatCounter = 9000

LARGE_FONT=("Helvatica",12)
NORM_FONT=("Helvatica",10)
SMALL_FONT=("Helvatica",8)

style.use("ggplot")
f = plt.figure()
#a = f.add_subplot(111)

excange="BTC-e"
programName="btce"
paneCount=1

resampleSize="15mins"
DataPace="tick"
candleWidth=0.008
topIndicator="none"
bottomIndicator="none"
middleIndicator="none"
chartLoad=True

darkColor="#183A54"
lightColor="#00A3E0"

EMAs=[]
SMA=[]

def tutorial():
    def leavemini(what):
        what.destory()
    def page2():
        tut.destroy()
        tut2=tk.Tk()

        def page3():
            tut2.destroy()
            tut3=tk.Tk()
            tut3.title("PArt 3!")
            label=ttk.Label(tut,text="part 3",font=NORM_FONT)
            label.pack(side="top", fill="x",pady=10)
            B1=ttk.Button(tut3,text="Done",command=tut3.destroy)
            B1.pack()
            tut3.mainloop()
        tut2.title("PArt 2!")
        label=ttk.Label(tut2,text="part 2",font=NORM_FONT)
        label.pack(side="top", fill="x",pady=10)
        B1=ttk.Button(tut2,text="Next Page",command=page3)
        B1.pack()
        tut2.mainloop()

    tut=tk.Tk()
    #tut.title("Tutorial")
    label=ttk.Label(tut,text="What do u need?",font=NORM_FONT)
    label.pack(side="top", fill="x",pady=10)

    B1=ttk.Button(tut,text="Overview of the app",command=page2)
    B1.pack()
    B2=ttk.Button(tut,text="How do i trade",command=lambda:popupmsg("Not yet completed"))
    B2.pack()
    B3=ttk.Button(tut,text="random question",command=lambda:popupmsg("Not yet completed"))
    B3.pack()
    
    
        


def loadChart(run):
    global chartLoad

    if run=="start":
        chartLoad=True
    elif run == "stop":
        chartLoad=False


def addMiddleIndicator(what):
    global middleIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("indicator in Tick data not available")
    if what !="none":
        if middleIndicator=="none":
            if what=="sma":
                midIQ=tk.Tk()
                midIQ.title("Periods?")
                labels= ttk.Label(midIQ, text="Choose how may sma?")
                labels.pack(side="top",fill="x",pady=10)

                e=ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator=[]
                    groups=[]
                    periods=(e.get())
                    groups.append("sma")
                    groups.append(int(periods))
                    middleIndicator.append(groups)
                    DatCounter=9000
                    print("middle indicator set to :",middleIndicator)
                    midIQ.destroy()

                
                b=ttk.Button(midIQ,text="Submit", command=callback)
                b.pack()
                tk.mainloop()

            if what=="ema":
                midIQ=tk.Tk()
                midIQ.title("Periods?")
                labels= ttk.Label(midIQ, text="Choose how may sma?")
                labels.pack(side="top",fill="x",pady=10)

                e=ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator=[]
                    groups=[]
                    periods=(e.get())
                    groups.append("ema")
                    groups.append(int(periods))
                    middleIndicator.append(groups)
                    DatCounter=9000
                    print("middle indicator set to :",middleIndicator)
                    midIQ.destroy()

                
                b=ttk.Button(midIQ,text="Submit", command=callback)
                b.pack()
        else:
            if what == "sma":
                midIQ=tk.Tk()
                midIQ.title("Periods?")
                labels= ttk.Label(midIQ, text="Choose how may sma?")
                labels.pack(side="top",fill="x",pady=10)

                e=ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    #middleIndicator=[]
                    periods=(e.get())
                    groups=[]
                    groups.append("sma")
                    groups.append(int(periods))
                    middleIndicator.append(groups)
                    DatCounter=9000
                    print("middle indicator set to :",middleIndicator)
                    midIQ.destroy()

                    
                b=ttk.Button(midIQ,text="Submit", command=callback)
                b.pack()
                tk.mainloop()

            if what=="ema":
                print ("entered else ema")
                midIQ=tk.Tk()
                midIQ.title("Periods?")
                labels= ttk.Label(midIQ, text="Choose how may sma?")
                labels.pack(side="top",fill="x",pady=10)

                e=ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    #middleIndicator=[]
                    periods=(e.get())
                    groups=[]
                    groups.append("ema")
                    groups.append(int(periods))
                    middleIndicator.append(groups)
                    DatCounter=9000
                    print("middle indicator set to :",middleIndicator)
                    midIQ.destroy()

                        
                b=ttk.Button(midIQ,text="Submit", command=callback)
                b.pack()
                tk.mainloop()
            
    else:
        middleIndicator=None


def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("indicator in Tick data not available")

    elif what=="none":
        topIndicator=what
        DatCounter=9000
        print ("none")
    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.title("Periods?")
        label=ttk.Label(rsiQ, text="Choose How many periods u want each rsi calculation to conside")
        label.pack(side="top",fill="x",pady=10)

        e=ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()
    
        def callback():

            global topIndicator
            global DatCounter

            periods = (e.get())
            group=[]
            group.append("rsi")
            group.append(periods)

            topIndicator=group
            DatCounter=9000
            print("Set top indicator to",group)
            rsiQ.destory()

        b=ttk.Button(rsiQ,text="Submit", command=callback)
        b.pack()
        b.mainloop()

    elif what=="macd":
        global topIndicator
        global DatCounter
        topIndictor="macd"
        DatCounter=9000


def changeTimeFrame(tf):
    global DataPace
    global DatCounter
    if tf == "7d" and resampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or large interval")
    else:
        DataPace=tf
        DatCounter=9000
        print (DataPace)
def changeSampleSize(size,width):
    global resampleSize
    global DatCounter
    global candleWidth

    if DataPace == "7d" and resampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or large interval")
    elif DataPace == "tick":
        popupmsg("you are currently using tick data not ohlc")
    else:
        resampleSize=size
        DatCounter=9000
        candleWidth=width
        
def changeExchange(toWhat,pn):
    global exchange
    global DatCounter
    global programName

    exchange= toWhat
    programName=pn
    DatCounter = 9000

    
def popupmsg(msg):
    popup=tk.Tk()
    label=ttk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side="top",fill="x",pady=10)
    B1=ttk.Button(popup,text="Ok",command=popup.destroy)
    B1.pack()
    popup.mainloop()


def animate(i):
    global refreshRate
    global DatCounter

    if chartLoad:
        if paneCount == 1:
            if DataPace == "tick":
                try:
                    a=plt.subplot2grid((6,4),(0,0),rowspan=5,colspan=4)
                    a2= plt.subplot2grid((6,4),(5,0),rowspan=1,colspan=4,sharex=a)
                        
                    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
                    data=urllib.request.urlopen(dataLink)
                    data = data.readall().decode("utf-8")
                    data=json.loads(data)
                    
                    data = data["btc_usd"]
                    data = pd.DataFrame(data)

                    data["datestamp"]=np.array(data['timestamp']).astype("datetime64[s]")
                    allDates=data["datestamp"].tolist()
                    
                    buys = data[(data['type']=="bid")]
                    #buys["datestamp"]=np.array(buys["timestamp"]).astype("datetime64[s]")
                    buyDates = (buys["datestamp"]).tolist() 
                    
                    sells= data[(data['type']=="ask")]
                    #sells["datestamp"]=np.array(sells["timestamp"]).astype("datetime64[s]")
                    sellDates = (sells["datestamp"]).tolist() 

                    volume=data["amount"]

                    a.clear()

                    a.plot_date(buyDates,buys["price"],lightColor,label="buys")
                    a.plot_date(sellDates, sells["price"],darkColor,label="sells")

                    a2.fill_between(allDates,0,volume,facecolor=darkColor)

                    a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                    a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:M:S" ))

                    a.legend(bbox_to_anchor=(0,1.02,1,.102),loc=3,
                             ncol=2,borderaxespad=0)
                    title="BTC-e BTCUSD Prices\n Last Price: "+str(data["price"][1999])
                    a.set_title(title)
                    print("hello")

                except Exception as e:
                    print("Failed because of: ",e)


    
class SeaofBTCapp(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        menubar=tk.Menu(container)
        filemenu=tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Save Setting",command=lambda:popupmsg("Not Supported yet"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice=tk.Menu(menubar,tearoff=1)

        exchangeChoice.add_command(label="BTC-e",
                                   command=lambda:changeExchange("BTC-e","btce"))
        exchangeChoice.add_command(label="Bitfinex",
                                   command=lambda:changeExchange("Bitfinex","bitfinex"))
        exchangeChoice.add_command(label="Bitstamp",
                                   command=lambda:changeExchange("Bitstamp","bitstamp"))
        exchangeChoice.add_command(label="Huobi",
                                   command=lambda:changeExchange("Huobi","huobi"))

        menubar.add_cascade(label="Exchange", menu=exchangeChoice)

        dataTf = tk.Menu(menubar,tearoff=1)
        dataTf.add_command(label="Tick",
                           command=lambda:changeTimeFrame('tick'))
        dataTf.add_command(label="1 Day",
                           command=lambda:changeTimeFrame('1d'))
        dataTf.add_command(label="3 Days",
                           command=lambda:changeTimeFrame('3d'))
        dataTf.add_command(label="7 Days",
                           command=lambda:changeTimeFrame('7d'))
        menubar.add_cascade(label="Data Time Frame", menu=dataTf)

        OHLCI=tk.Menu(menubar,tearoff=1)
        OHLCI.add_command(label="Tick",
                           command=lambda:changeSampleSize('tick'))
        OHLCI.add_command(label="1 Minute",
                           command=lambda:changeSampleSize('1Min',0.005))
        OHLCI.add_command(label="5 Minute",
                           command=lambda:changeSampleSize('5Min',0.003))
        OHLCI.add_command(label="15 Minute",
                           command=lambda:changeSampleSize('15Min',0.008))
        OHLCI.add_command(label="30 Minute",
                           command=lambda:changeSampleSize('30Min',0.016))
        OHLCI.add_command(label="1 Hour",
                           command=lambda:changeTimeFrame('1H',0.032))
        OHLCI.add_command(label="3 hour",
                           command=lambda:changeTimeFrame('3H',0.096))
        menubar.add_cascade(label="OHLC interval", menu=OHLCI)

        topIndi=tk.Menu(menubar,tearoff=1)
        topIndi.add_command(label="None",
                            command=lambda:addTopIndicator('none'))
        topIndi.add_command(label="RSI",
                            command=lambda:addTopIndicator('rsi'))
        topIndi.add_command(label="MACD",
                            command=lambda:addTopIndicator('macd'))
        menubar.add_cascade(label="Top Indicator",menu=topIndi)


        mainI=tk.Menu(menubar,tearoff=1)
        mainI.add_command(label="None",
                            command=lambda:addMiddleIndicator('none'))
        mainI.add_command(label="SMA",
                            command=lambda:addMiddleIndicator('sma'))
        mainI.add_command(label="EMA",
                            command=lambda:addMiddleIndicator('ema'))
        menubar.add_cascade(label="Main/middle Indicator",menu=mainI)


        bottomI=tk.Menu(menubar,tearoff=1)
        bottomI.add_command(label="None",
                            command=lambda:addBottomIndicator('none'))
        bottomI.add_command(label="RSI",
                            command=lambda:addBottomIndicator('rsi'))
        bottomI.add_command(label="MACD",
                            command=lambda:addBottomIndicator('macd'))
        menubar.add_cascade(label="Bottom Indicator",menu=bottomI)

        tradeButton= tk.Menu(menubar,tearoff=1)
        tradeButton.add_command(label="Manual Trading",
                                command=lambda:popupmsg("This is not live yet"))
        tradeButton.add_command(label="Automated trading Trading",
                                command=lambda:popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label="Quick Buy",
                                command=lambda:popupmsg("This is not live yet"))
        tradeButton.add_command(label="Quick Sell",
                                command=lambda:popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label="Set-up quick buy sell",
                                command=lambda:popupmsg("This is not live yet"))
        menubar.add_cascade(label="Trading",menu=tradeButton)

        startStop= tk.Menu(menubar,tearoff=1)
        startStop.add_command(label="Resume",
                              command=lambda:loadChart('start'))
        startStop.add_command(label="Stop",
                              command=lambda:loadChart('stop'))
        menubar.add_cascade(label="Resume/Pause",menu=startStop)

        helpmenu=tk.Menu(menubar,tearoff=0)
        helpmenu.add_command(label="Tutorial",command=tutorial)

        menubar.add_cascade(label="Help",menu=helpmenu)
        
        
        tk.Tk.config(self, menu=menubar)

        
        self.frames={}

        for F in (StartPage,BTCe_page):
            frame = F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame=self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="""ALPHA Bitcoin trading application,
USE at your own risk
there is no promise or warranty of your safety""",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1=ttk.Button(self,text="Agree",
                          command=lambda:controller.show_frame(BTCe_page))
        button1.pack()
        button2=ttk.Button(self,text="disagree",
                          command=quit)
        button2.pack()
        

        
class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        tk.Frame.__init__(self,parent)
        label=ttk.Label(self,text="",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1=ttk.Button(self,text="Back to home",
                          command=lambda:controller.show_frame(BTCe_page))
        button1.pack()
        button2=ttk.Button(self,text="Third page",
                          command=quit)
        button2.pack()
        

class BTCe_page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        tk.Frame.__init__(self,parent)
        label=ttk.Label(self,text="Graph Page",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1=ttk.Button(self,text="Back to home",
                          command=lambda:controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        toolbar=NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
    
app = SeaofBTCapp()
app.geometry("1360x720")
ani = animation.FuncAnimation(f,animate,interval=9000)
app.mainloop()
        
        
            
    

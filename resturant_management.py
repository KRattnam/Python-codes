
from Tkinter import *
import random
import time

root=Tk()
root.geometry("1600x800+0+0")
root.title("Resturant Management")

#===============================Variables==============================

#--calcu-----
localtime=time.asctime(time.localtime(time.time()))

text_input=StringVar()
operator=""

#---Resturant--
rand=StringVar()
fries=StringVar()
burger=StringVar()
cheese=StringVar()
cmeal=StringVar()
mmeal=StringVar()
drinks=StringVar()
Cost=StringVar()
state_tax=StringVar()
service_charge=StringVar()
sub_total=StringVar()
total_cost=StringVar()



#===============================Functions==============================

#=========Calculator==========
def btnClick(numbers):
	global operator
	operator=operator+str(numbers)
	text_input.set(operator)

def btnClearDisplay():
	global operator
	operator=""
	text_input.set("")

def btnEqualsInput():
	global operator
	sumup=str(eval(operator))
	text_input.set(sumup)
	operator=""
#========Resturant============

def Ref():
	x=random.randint(12908,50876)
	randomRef=str(x)
	rand.set(randomRef)

	cof=float(fries.get())
	coburger=float(burger.get())
	cocheese=float(cheese.get())
	cocmeal=float(cmeal.get())
	commeal=float(mmeal.get())
	codrinks=float(drinks.get())
	
	CostofFries= cof * 0.99
	CostofBurger= coburger * 5.0
	CostofCheese= cocheese * 3.99
	CostofCmeal= cocmeal * 0.99
	CostofMmeal= commeal * 0.99
	CostofDrinks= codrinks * 0.99

	TotalCost=(CostofFries+CostofBurger+CostofCheese+CostofCmeal+CostofMmeal+CostofDrinks)

	CostofMeal= "$" , str('%.2f' %TotalCost)

	PayTax = (CostofFries+CostofBurger+CostofCheese+CostofCmeal+CostofMmeal+CostofDrinks)*0.2

	

	Ser_Charge= TotalCost/99

	Service= "$" , str('%.2f' %Ser_Charge)

	OverAllCost= "$", str('%.2f' %(PayTax+TotalCost+Ser_Charge))
	PaidTax= "$", str('%.2f' % PayTax)

	Cost.set(CostofMmeal)
	sub_total.set(CostofMmeal)
	service_charge.set(Service)
	state_tax.set(PaidTax)
	total_cost.set(OverAllCost)


def qExit():
	root.destroy()

def Reset():
	rand.set("")
	fries.set("")
	burger.set("")
	cheese.set("")
	cmeal.set("")
	mmeal.set("")
	drinks.set("")
	Cost.set("")
	state_tax.set("")
	service_charge.set("")
	sub_total.set("")
	total_cost.set("")



#============GUI ELEMETS===============
Tops= Frame(root,width = 1600 ,height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1= Frame(root,width = 800 ,height= 700,  relief=SUNKEN)
f1.pack(side=LEFT)


f2= Frame(root,width = 300 ,height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Resturant management System", fg="Steel Blue", bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime, fg="Steel Blue", bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

#========================================CALCULATOR=========================
txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

#------ROW1--------------
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue", command=lambda:btnClick(7))
btn7.grid(row=2,column=0)


btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue", command=lambda:btnClick(8))
btn8.grid(row=2,column=1)


btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue", command=lambda:btnClick(9))
btn9.grid(row=2,column=2)


Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue", command=lambda:btnClick("+"))
Addition.grid(row=2,column=3)

#--------ROW 2------------

btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue", command=lambda:btnClick(4))
btn4.grid(row=3,column=0)


btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue", command=lambda:btnClick(5))
btn5.grid(row=3,column=1)


btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue", command=lambda:btnClick(6))
btn6.grid(row=3,column=2)


Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue", command=lambda:btnClick("-"))
Subtraction.grid(row=3,column=3)

#--------ROW 3------------

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue", command=lambda:btnClick(1))
btn1.grid(row=4,column=0)


btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue", command=lambda:btnClick(2))
btn2.grid(row=4,column=1)


btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue", command=lambda:btnClick(3))
btn3.grid(row=4,column=2)


Multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue", command=lambda:btnClick("*"))
Multiplication.grid(row=4,column=3)


#--------ROW 4------------

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue", command=lambda:btnClick(0))
btn0.grid(row=5,column=0)


btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=lambda:btnClearDisplay())
btnClear.grid(row=5,column=1)


btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=lambda:btnEqualsInput())
btnEquals.grid(row=5,column=2)


Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue", command=lambda:btnClick("/"))
Division.grid(row=5,column=3)


#=======================================Resturant Bill================================

#-------Resturant Info 1----------

lblReference=Label(f1,font=('arial',16,'bold'), text="Reference", bd=8, anchor='w')
lblReference.grid(row=0,column=0)

txtReference=Entry(f1,font=('arial',16,'bold'), textvariable=rand , bd=16, insertwidth=4, bg="powder blue", justify="right")
txtReference.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'), text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1,column=0)

txtFries=Entry(f1,font=('arial',16,'bold'), textvariable=fries , bd=16, insertwidth=4, bg="powder blue", justify="right")
txtFries.grid(row=1,column=1)



lblBurger=Label(f1,font=('arial',16,'bold'), text="Chicken Burger", bd=16, anchor='w')
lblBurger.grid(row=2,column=0)

txtBurger=Entry(f1,font=('arial',16,'bold'), textvariable=burger , bd=16, insertwidth=4, bg="powder blue", justify="right")
txtBurger.grid(row=2,column=1)

lblCheese=Label(f1,font=('arial',16,'bold'), text="Cheese Burger", bd=16, anchor='w')
lblCheese.grid(row=3,column=0)

txtCheese=Entry(f1,font=('arial',16,'bold'), textvariable=cheese , bd=16, insertwidth=4, bg="powder blue", justify="right")
txtCheese.grid(row=3,column=1)

lblCMeal=Label(f1,font=('arial',16,'bold'), text="Chicken Meal", bd=16, anchor='w')
lblCMeal.grid(row=4,column=0)

txtCMeal=Entry(f1,font=('arial',16,'bold'), textvariable=cmeal , bd=16, insertwidth=4, bg="powder blue", justify="right")
txtCMeal.grid(row=4,column=1)


lblMMeal=Label(f1,font=('arial',16,'bold'), text="Mutton Meal", bd=16, anchor='w')
lblMMeal.grid(row=5,column=0)

txtMMeal=Entry(f1,font=('arial',16,'bold'), textvariable=mmeal , bd=16, insertwidth=4, bg="powder blue", justify="right")
txtMMeal.grid(row=5,column=1)

#------Resturant Info 2-----------

lblDrinks=Label(f1,font=('arial',16,'bold'), text="Drinks", bd=8, anchor='w')
lblDrinks.grid(row=0,column=2)

txtDrinks=Entry(f1,font=('arial',16,'bold'), textvariable=drinks , bd=16, insertwidth=4, bg="#ffffff", justify="right")
txtDrinks.grid(row=0,column=3)

lblCost=Label(f1,font=('arial',16,'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1,column=2)

txtCost=Entry(f1,font=('arial',16,'bold'), textvariable=Cost , bd=16, insertwidth=4, bg="#ffffff", justify="right")
txtCost.grid(row=1,column=3)



lblService=Label(f1,font=('arial',16,'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2,column=2)

txtService=Entry(f1,font=('arial',16,'bold'), textvariable=service_charge , bd=16, insertwidth=4, bg="#ffffff", justify="right")
txtService.grid(row=2,column=3)

lblStateTax=Label(f1,font=('arial',16,'bold'), text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=3,column=2)

txtStateTax=Entry(f1,font=('arial',16,'bold'), textvariable=state_tax , bd=16, insertwidth=4, bg="#ffffff", justify="right")
txtStateTax.grid(row=3,column=3)

lblSubTotal=Label(f1,font=('arial',16,'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4,column=2)

txtSubTotal=Entry(f1,font=('arial',16,'bold'), textvariable=sub_total , bd=16, insertwidth=4, bg="#ffffff", justify="right")
txtSubTotal.grid(row=4,column=3)


lblTotalCost=Label(f1,font=('arial',16,'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5,column=2)

txtTotalCost=Entry(f1,font=('arial',16,'bold'), textvariable=total_cost , bd=16, insertwidth=4, bg="#ffffff", justify="right")
txtTotalCost.grid(row=5,column=3)

#--------------Buttons---------------
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Total",bg="powder blue" ,command=lambda: Ref())
btnTotal.grid(row=7, column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Reset",bg="powder blue" ,command=lambda: Reset())
btnReset.grid(row=7, column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Exit",bg="powder blue" ,command=lambda: qExit())
btnExit.grid(row=7, column=3)


root.mainloop()







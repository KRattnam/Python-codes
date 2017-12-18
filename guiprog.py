
import Tkinter

root=Tkinter.Tk()
root.title("GUI Application")
album={}
album["Artist 1"]="Song1"
album["Artist 2"]="Song2"
album["Artist 3"]="Song3"
#Function
def show_all():
	#Clear list box
	lb_music.delete(0,"end")
	#iterate through keys
	for artist in album:
		lb_music.insert("end",artist)

def show_one():
	artist=lb_music.get("active")
	albums=album[artist]
	msg= artist +" : "+ albums
	lbl_output["text"]= msg

def add_one():
	info=txt_input.get()
	split_info=info.split(",")
	artist=split_info[0]
	albums=split_info[1]
	album[artist]=albums
	show_all()
	txt_input.delete(0,"end")
	

#GUI
lbl_output=Tkinter.Label(root,text="Ready")
lbl_output.pack()

txt_input=Tkinter.Entry(root)
txt_input.pack()

lb_music=Tkinter.Listbox(root)
lb_music.pack()

btn_show_all=Tkinter.Button(root,text="Show All",command=show_all)
btn_show_all.pack()

btn_show_one=Tkinter.Button(root,text="Show one",command=show_one)
btn_show_one.pack()

btn_add_one=Tkinter.Button(root,text="Add One" ,command=add_one)
btn_add_one.pack()

root.mainloop()


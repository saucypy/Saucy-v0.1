from tkinter import *
import webbrowser
import random
import time




window = Tk()
window.geometry("720x720")
window.title("Saucy!")
window.config(
	background="#282828"
	)



link = "https://www.nhentai.net/g/"





def openCode():
	code = openSauce_Entry.get()
	try:
		webbrowser.open(f"{link}{int(code)}")

	except:
		print("ERROR! Needed type 'int'")


def randomCode():
	code = random.randrange(360000)
	webbrowser.open(f"{link}{code}")


def search():
	keyword = search_Entry.get()
	
	if keyword != "":
		webbrowser.open(f"https://nhentai.to/search?q={str(keyword)}")

	else:
		print("Nothing to search for")
	






search_Entry = Entry(
	window,
	width=14,
	font=("Arial",17,"italic","bold"),
	bg="#282828",
	bd="1",
	fg="#ffffff"
	)
search_Confirm = Button(
	window,
	text="?",
	font=("Arial",13,"bold"),
	bg="#282828",
	bd="0",
	fg="#ffffff",
	command=search
	)
search_Text = Label(
	text="Search bar",
	font=("Arial",11,"bold"),
	bg="#282828",
	bd="0",
	fg="#ffffff"
	)




openSauce_Entry = Entry(
	window,
	width=6,
	font=("Arial",21,"bold"),
	fg="#ffffff",
	bg="#282828",
	bd="1"
	)
openSauce_Confirm = Button(
	text="Confirm",
	command = openCode,
	background="#ffffff",
	bd="1",
	fg="#ffffff",
	bg="#282828",
	font=("Arial",15,"bold")
	)
openSauce_Text = Label(
	text="Code",
	font=("Arial",11,"bold"),
	bg="#282828",
	bd="0",
	fg="#ffffff"
	)



randomSauce_Button = Button(
	text="Random code",
	command=randomCode,
	font=("Arial",20,"bold"),
	bg="#282828",
	fg="#ffffff",
	bd="1"
	)



mainLabel = Label(
	window,
	text="Saucy!",
	font=("Arial",30,"bold"),
	bd="0",
	fg="#ffffff",
	bg="#282828"
	)







openSauce_Entry.place(x=10,y=75)
openSauce_Confirm.place(x=120,y=75)
openSauce_Text.place(x=14,y=63)


search_Entry.place(x=475,y=78)
search_Confirm.place(x=670,y=78)
search_Text.place(x=570,y=63)


randomSauce_Button.pack(side="bottom",pady=20)


mainLabel.pack(side="top",pady=10)






window.mainloop()
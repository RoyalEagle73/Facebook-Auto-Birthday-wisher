from tkinter import *
from PIL import ImageTk, Image
import fb
from tkinter.ttk import Progressbar
import webbrowser
from tkinter import messagebox

home=Tk()

logo = ImageTk.PhotoImage(Image.open("logo.png"))
fb_img = ImageTk.PhotoImage(Image.open("fb.png"))
github_img = ImageTk.PhotoImage(Image.open("github.png"))
linkedin_img = ImageTk.PhotoImage(Image.open("linkedin.png"))

logo_label = Label(home, image=logo, bg="white")
logo_label.place(x=170,y=10)

title = Label(home, text=" WISH AT A SWISH ", bg="white", fg="OrangeRed2")
title.configure(font =( "Arial", 15, "bold"))
title.place(x=120,y=80)

cuz = Label(home, text="( cuz we and zucku got your back... )", bg="white", fg="RoyalBlue1")
cuz.configure(font =( "Comic Sans MS" ,8, "italic"))
cuz.place(x=125,y=100)

username = Label(home, text="Enter Your Facebook username :", bg="white", fg="midnight blue")
username.place(x=110,y=130)

username_entry = Entry(home, bg="ivory")
username_entry.configure(width=40)
username_entry.place(x=60,y=150)

password = Label(home, text="Enter Your Facebook password :", bg="white", fg="midnight blue")
password.place(x=110,y=190)

password_entry = Entry(home, bg="ivory")
password_entry.configure(width=40, show="*")
password_entry.place(x=60,y=210)

customised = Label(home, text="Enter Customised Wish ( optional ):", bg="white", fg="midnight blue")
customised.place(x=110,y=250)

customised_entry = Entry(home, bg="ivory")
customised_entry.configure(width=40)
customised_entry.place(x=60,y=270)


## FUNCTIONS
def driver_fun(event):
	global customised_entry
	global username_entry
	global password_entry

	messagebox.showinfo("Notification", "1) Process has been started and it takes time according to your internet connection.\n2) Don't spam button till it's grey.\n3) Wait for next update below the button on application.")

	message = customised_entry.get()
	if len(message) == 0:
		message = "Happy Birthday :)"

	new_wish = fb.wish(username_entry.get(), password_entry.get(), message)
	collect_result = 0
	collect_result = new_wish.collect_data()
	wishing_result = 0
	update = ""

	if collect_result == 0:
		update = "Please Check your Internet Connection"
		update_label = Label(home, text=update, fg="red", bg="white")
		update_label.place(x=90,y=350)
		return	
	elif collect_result == 1:
		update = "Please Check Login Credentials"
		update_label = Label(home, text=update, fg="red", bg="white")
		update_label.place(x=110,y=350)
		return
	elif collect_result == 2:
		update = "Error opening wishing page"
		update_label = Label(home, text=update, fg="red", bg="white")
		update_label.place(x=100,y=350)
		return
	elif collect_result == 3:
		update = "Data Collected, Starting To Wish"
		update_label = Label(home, text=update, fg="green", bg="white")
		update_label.place(x=120,y=350)
		##PROGRESSBAR AND PROGRESS WINDOW
		progress_window = Tk()
		progress_window.title("Wish Progress")
		progress_window.configure(background="white")
		progress_window.configure(width=300, height=(fb.size+1)*20)
		progress=Progressbar(progress_window,orient=HORIZONTAL,length=300,mode='determinate')
		post = ""

		for i in range(fb.size):
			wishing_result = new_wish.wishing(i)
			if wishing_result == 0:
				post = "You've already wished %s."%(fb.names[i])
			else:
				post = "Wished %s"%(fb.names[i])
			progress['value']=((i+1)/fb.size)*300
			progress_window.update_idletasks()
			post_label = Label(progress_window, text = post, bg="white", fg="VioletRed4")
			post_label.place(x=10, y=((i+1)*20))
	
	update = "Data Collected, Starting To Wish\nWished %d of your friends"%(fb.size)
	update_label_2 = Label(home, text=update, fg="green", bg="white")
	update_label_2.place(x=120,y=350)

	progress.place(x=0, y=0)
	new_wish.kill()
	progress_window.resizable(0,0)
	progress_window.mainloop()

## CONTACT FUNCTIONS
def github_callback(event):
	webbrowser.open_new("https://Github.com/RoyalEagle73")

def facebook_callback(event):
	webbrowser.open_new("https://Facebook.com/RoyalEagle073")

def linkedin_callback(event):
	webbrowser.open_new("https://www.linkedin.com/in/deepak-chauhan-173756170/")

button = Button(home, text="Wish now", bg="ivory", fg="black")
button.place(x=160,y=310)
button.bind("<Button-1>", driver_fun)
home.title("Auto Wish Poster")


##ABOUT ME TABS
about_me = Label(home, text = "-------------------- Follow me on -------------------- ", bg="white", fg="RoyalBlue1")
about_me.configure(font=("Times New Roman", 15, "bold italic"))
about_me.place(x=50, y=410)

github = Label(home, image = github_img, bg="white")
github.bind("<Button-1>",github_callback)
github.place(x=90, y=450)


facebook = Label(home, image = fb_img, bg="white")
facebook.bind("<Button-1>", facebook_callback)
facebook.place(x=170, y=450)


linkedin= Label(home, image = linkedin_img, bg="white")
linkedin.bind("<Button-1>", linkedin_callback)
linkedin.place(x=250, y=450)

home.configure(width=400, height=550)
home.resizable(0,0)
home.configure(background="white")
home.mainloop()

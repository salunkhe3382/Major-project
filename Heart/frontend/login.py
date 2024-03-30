import customtkinter as ctk
import tkinter
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import os
import sys
from omegaconf import OmegaConf


# Load config file
conf = OmegaConf.load("../config.yaml")
# Add path
sys.path.append(conf["VARIABLES"]["DATA_PATH"])
from run import MainApp

app = ctk.CTk()
app.geometry("1440x900")
app.title("Login Page")

ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")




#img = Image.open("message_icon.png")

def login():
    username = "admin"
    password = "doctor"
    #new_window = ctk.CTkToplevel(open_App)

    #new_window.geometry("350x150")
    #main_app = MainApp()
    #main_app.mainloop()
    #app.destroy()
    

    if user_entry.get() == username and user_pass.get() == password:
       tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
       #Destroy the login page
       #app.destroy()
       #Open the main page
       main_app = MainApp()
       main_app.mainloop()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showinfo(title="Wrong password",message="Please check your password again")
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showinfo(title="Wrong username",message="Please check your username again")
    else:
        tkmb.showerror(title="Login failed",message="Invalid username and password")

label = ctk.CTkLabel(app,text = "HEART DISEASE DETECTION MODEL",font=('Arial',40,'bold'))

label.pack(pady = 20)

frame = ctk.CTkFrame(master = app,width=320, height = 360,corner_radius=15)
frame.pack(pady=20,padx=40,fill='both',expand=True)

heading_label=ctk.CTkLabel(master=frame,text="WELCOME",font=('Arial',32,'bold'))
heading_label.pack(padx=50,pady=45)

subheading_label=ctk.CTkLabel(master=frame,text="Log in to your Account",font=('Arial',32,'bold'))
subheading_label.pack(padx=50,pady=45)

user_entry = ctk.CTkEntry(master = frame,width=220,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass = ctk.CTkEntry(master = frame,width=220,placeholder_text="Password" ,show="*")
user_pass.pack(pady=12,padx=10)

#forgotpass_label = ctk.CTkLabel(master=frame,text="Forget password",font=('Arial',12))
#forgotpass_label.pack(pady=9,padx=5)

checkbox = ctk.CTkCheckBox(master=frame,text="Remember Me")
checkbox.pack(pady=12,padx=10)

button = ctk.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)

app.mainloop()
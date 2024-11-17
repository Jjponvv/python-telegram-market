import tkinter as tk
from tkinter import filedialog, messagebox
import sys

#DATA VARIABLES
API = ''
ADMIN = ''
PATH = ''

# FONTS
TITLEFONT = ('Arial', 25, 'bold')
ENTRYFONT = ('Arial', 18, 'bold')

#WINDOW SETTINGS
sc = tk.Tk()
sc.title("Create bot based on messages")
sc.geometry('500x500')

#OBJECTS
title = tk.Label(text="Create telegram bot based\n on messages", font=TITLEFONT).pack(pady=40)

apiKeyText = tk.Label(text="API key:", font=ENTRYFONT).pack()
apiKeyEntry = tk.Entry(width=30, font=ENTRYFONT)
apiKeyEntry.pack(pady=20)


adminUserText = tk.Label(text="Admin username (with @): ", font=ENTRYFONT).pack()
adminUserEntry = tk.Entry(width=30, font=ENTRYFONT)
adminUserEntry.pack(pady=20)

SubmitButton = tk.Button(text="Submit and create", command=lambda: setData() if setData() != False else False, font=ENTRYFONT).pack()

#GET PATH
def setData():
    global PATH, ADMIN, API
    if apiKeyEntry.get() != '':
        API = apiKeyEntry.get()
    else:
        # messagebox.showerror('error', 'Enter API')
        # return False
        API = '6916453662:AAHCrXJWssOjRzwwpcH_uIEPx0E2X3sMlIs'
    
    if adminUserEntry.get() == '':
        messagebox.showerror('error', 'Enter admin user')
        return False
    elif adminUserEntry.get().startswith('@') != True:
        messagebox.showerror('error', 'invalid username')
        return False
    else:
        ADMIN = adminUserEntry.get()
        
    
    PATH = filedialog.askdirectory(title='save bot')
    if PATH != '':
        pass
    else:
        return False
    
    messagebox.showinfo('info', 'bot succesfully created')
    
    return True
    
    
#LOOP
sc.mainloop()
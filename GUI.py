import tkinter
from tkinter import *
from tkinter.ttk import *

#Main window dimensions
_root = Tk()
_root.title('ISRA')
_root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
_root.geometry('330x300')


 #defining about
def _about():
    about = Tk()
    about.title('ISRA')
    about.iconbitmap('C:\ISRA\ISRA LOGO.ico')
    about.geometry('300x200')
    ab = Label(about, text='Indian Speech Recognition Assistant')
    ab.place(anchor = CENTER, rely=0.15, relx=0.5)
    v = Label(about, text ='Version v1.0 beta')
    v.place(anchor = CENTER ,relx=0.5,rely=0.25)
    c = Label(about, text='Creators: Varun Bhatnagar and Tushar Garg')
    c.place(anchor = CENTER,relx=0.5,rely=0.75)


#defining help
def _help():
    help = Tk()
    help.title('ISRA')
    help.iconbitmap('C:\ISRA\ISRA LOGO.ico')
    help.geometry('300x50')
    h = Label(help, text='It is a simple program so there is no need for help.')
    h.pack()


#setting menues
my_menu = Menu(_root)
_root.config(menu = my_menu)



#setting main menu
options_menu = Menu(my_menu,tearoff = 0)
my_menu.add_cascade(label ='Menu', menu = options_menu)
options_menu.add_command(label="Settings")
options_menu.add_command(label ='Help', command = _help)
options_menu.add_command(label ='About', command = _about)


#setting another menu
options_menu = Menu(my_menu,tearoff = 0)
my_menu.add_cascade(label ='Account', menu = options_menu)
options_menu.add_command(label="General")
options_menu.add_command(label ='Privacy and Security')
options_menu.add_command(label ='Sign Out')


#Making Exit button
exit_button = Button(_root, text='Exit', command = _root.destroy)
exit_button.place(relx=0.5, rely=0.95, anchor = CENTER)
exit_button.config(width = 15)


#Making Mic button

photo = PhotoImage(file = 'MIC.png')
_photo = photo.subsample(4,4)
mic_button = Button(_root, image = _photo)
mic_button.place(relx=0.5, rely=0.15, anchor = CENTER)

scroll = Scrollbar(_root)
scroll.place(relx=0.605, rely=0.6, anchor = CENTER)

#adding assistant text area
ass_text = Text(_root, height = 10 , width=35, yscrollcommand = scroll.set)
ass_text.place(anchor = CENTER, relx=0.5,rely=0.6)
scroll.config(command = ass_text.yview)



_root.mainloop()

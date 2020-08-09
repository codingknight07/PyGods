import tkinter
from tkinter import *
from tkinter.ttk import *


#main window
root = Tk()
root.title('ISRA')
root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
root.geometry('430x500')
root.resizable(height = False, width=False)

#about window
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


#making menus
my_menu = Menu(root)

root.config(menu = my_menu)

my_menu.add_cascade(label = 'Settings')

options = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = 'Account', menu = options)
options.add_command(label = 'General')
options.add_command(label = 'Privacy and Security')
options.add_separator()
options.add_command(label = 'Sign Out')

my_menu.add_cascade(label = 'Help', command = _help)

my_menu.add_cascade(label = 'About', command = _about)

frame = Frame(root)

 #adding assistant text area
scroll = Scrollbar(frame)
scroll.pack(side = RIGHT, fill = Y)        
ass_text = Text(frame, height = 18 , width=50)
ass_text.place(anchor = CENTER, relx=0.48,rely=0.49)
ass_text.config(yscrollcommand = scroll.set)
scroll.config(command = ass_text.yview)
frame.pack(fill = BOTH, expand = True)
#Web search entry
search_lab = Label(root, text = 'Search Web: ', font = ("Times New Roman", 10, "bold"))
search_lab.place(relx=0.1 , rely = 0.85, anchor = CENTER)
search_entry = Entry(root)
search_entry.config(width = 53)
search_entry.place(relx=0.56,rely=0.85,anchor=CENTER)

#functioning of mic
on = True
def start():
    global on
    if on:
        mic_button.configure(image = _offmic)
        on = False
    else:
        mic_button.configure(image = _onmic)
        on = True

#making mic button

onmic = PhotoImage(file = 'MIC.png')
_onmic = onmic.subsample(4,4)

offmic = PhotoImage(file = 'offmic.png')
_offmic = offmic.subsample(18,18)

mic_button = Button(root, image = _onmic, command=start)
mic_button.place(relx=0.5, rely=0.1, anchor = CENTER)




#Making Exit button
style = Style()
style.configure('Exit.TButton', font =('Showcard Gothic', 10))

exit_button = Button(root, text='Exit', style = 'Exit.TButton', command = root.destroy)
exit_button.place(relx=0.5, rely=0.95, anchor = CENTER)
exit_button.config( width = 25)




root.mainloop() 

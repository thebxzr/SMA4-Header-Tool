#imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import sys
import os

filename = ""


#idk
def quitprogram():
   answer = askyesno('Exit?', 'Are you sure you want to exit?')
   if answer:
      root.destroy()
      sys.exit()

content = None
file = None

#Selecting and understanding file
def selectfile():
    filetypes = (
        ('level files', '*.level'),
    )

    filename = fd.askopenfilename(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    print("User opened " + filename)

    with open(filename, 'r+b') as f:
      global content
      global file
      content = bytearray(f.read())
      levelIconData = content[4]
      setIconData = str(content[2])
      setNumberData = content[3]
      print(content)
      print(file)

    
    print("Current level icon id is " + str(levelIconData))
    levelIcon.set(level_icons['values'][levelIconData])
    fileLabel.config(text = "Current File: " + os.path.basename(filename))

    if len(setIconData) == 1:
       setIconData = "0" + setIconData
   
    print("Current level set id is " + str(setIconData) + ", " + str(setNumberData))
    selected_set.set(setIconData)
    setNumberInput.delete('1.0', END)
    setNumberInput.insert(END, setNumberData)

#Saving file
def savefile():
   filetypes = (
        ('level files', '*.level')
    )
   
   global content
   content[4] = int(levelIcon.get()[0] + levelIcon.get()[1], base=16)
   content[3] = int(setNumberInput.get("1.0", END))
   content[2] = int(selected_set.get(), base=16)
   
   print(levelIcon.get()[0] + levelIcon.get()[1])

   
   savedFile = fd.asksaveasfile(mode = 'wb', defaultextension='.level', 
         filetypes= [('Level','.level')])


   if savedFile is None or filename is None or content is None:
      return

   savedFile.write(content)

#About
def about():
   messagebox.showinfo(title="About SMA4 Header Tool", message="SMA4 Header Tool is an e-reader card editing tool for Super Mario Advance 4.\nIt is designed around editing things related to the header like the Icon shown in a level.\nYou can use programs like Smaghetti (https://smaghetti.com/), a level editor for SMA4 to create levels, then with the flask icon in the corner, export as binary to get a .level file.\n\nCreated by: Bxzr,\nDiscord: Bxzr#8797")

#Help
def helpinfo():
   messagebox.showinfo(title="Help", message="To use SMA4 Header Tool, all you need is .level file (more info in 'About' section). Then you can simply press Open, select the file, make edits, then Save it.\n\nPlease also save it to a different file in case of corruption.\n\nPlease report any found bugs on GitHub or to the creator (details in 'About' section), to help improve this tool even further.\nIn the future, I plan for this tool to have even more content, with things like editing Names, A and E coins, Timers and more, but that is in the future.\nAlso check out Smaghetti, SMA4 level editor (https://smaghetti.com/)!")

#beta Tool: hex Addresses
def hexaddresses():
   messagebox.showinfo(title="Hex Addresses", message="The hex addresses of all used values are:\n\n0x02: Set Icon\n0x03: Set Number\n0x04: Level Icon\n\n(More will be added in future updates.)")
                       
#Setting up main things (title, size, icon)   
root = Tk()
root.wm_title("SMA4 Header Tool (Alpha v0)")
icon = PhotoImage(file = 'icon.ico')
root.iconphoto(False, icon)
root.geometry("516x350")
root.resizable(0, 0)


#Menu bar (File, Help, etc...)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=selectfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitprogram)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Help", command=helpinfo)
menubar.add_cascade(label="Help", menu=helpmenu)

submenu = Menu(helpmenu, tearoff=0)
submenu.add_command(label='Hex Addresses', command=hexaddresses)

helpmenu.add_cascade(label="Beta Tools",menu=submenu)

root.config(menu=menubar)


#loading images
LevelIconKey = tk.PhotoImage(file = "level_icon_key.gif")

#file displayer
fileLabel = Label(root, text = "Current File: -", height=1)  
fileLabel.grid(row = 0, column = 0, sticky = W, pady = 2, padx=3)


#LI frame
LI_frame = tk.LabelFrame(root, text="Level Icon")
LI_frame.grid(row = 1, column = 0, sticky = W, pady = 2, padx=5)

#level icon select menu
levelIcon = tk.StringVar()
level_icons = ttk.Combobox(LI_frame, width = 27, textvariable = levelIcon, state = 'readonly')
level_icons.grid(row = 1, column = 0, sticky = W, pady = 2)

#level icons list
level_icons['values'] = [
    '00 e+',
    '01 Star',
    '02 Swirling Sand',
    '03 Level Selector',
    '04 Fortress',
    '05 Giant Castle',
    '06 Spiral Tower',
    '07 Pyramid',
    '08 Gold Mushroom House',
    '09 Mansion',
    '0A Airship',
    '0B Tank',
    '0C Airship + Cannon',
    '0D Small Airship',
    '0E Coin Ship',
    '0F Hand',
    '10 Cloud',
    '11 Hills',
    '12 Tree',
    '13 Water',
    '14 Flower',
    '15 Ice Spike',
    '16 Muncher',
    '17 Flame',
    '18 Skull',
    '19 Hammer Bro',
    '1A Boomerang Bro',
    '1B Another Hammer Bro',
    '1C Fire Bro',
    '1D Sledge Bro',
    '1E Glitched Tile',
    '1F Nothing',
    ]

level_icons.current(0)

#level icon key
LIKframe = tk.Label(LI_frame, image = LevelIconKey)
LIKframe.grid(row = 1, column = 1, sticky = W, pady = 2)

#set icon frame
SET_frame = tk.LabelFrame(root, text="Set Number and Icon")
SET_frame.grid(row = 2, column = 0, sticky = W, pady = 2, padx=5)

#set icon
labelSET = Label(SET_frame, text = "Set Icon", height=1)  
labelSET.grid(row = 0, column = 0, sticky = W, pady = 2)

#set chooser buttons
selected_set = tk.StringVar()
sets =  (('Star',    '01'),
         ('Mushroom', '02'),
         ('Flower',  '03'),
         ('Heart',   '04'),
         ('Promo',   '1F'))


setrb1 = tk.Radiobutton(SET_frame, text = sets[0][0], value = sets[0][1], variable = selected_set)
setrb2 = tk.Radiobutton(SET_frame, text = sets[1][0], value = sets[1][1], variable = selected_set)
setrb3 = tk.Radiobutton(SET_frame, text = sets[2][0], value = sets[2][1], variable = selected_set)
setrb4 = tk.Radiobutton(SET_frame, text = sets[3][0], value = sets[3][1], variable = selected_set)
setrb5 = tk.Radiobutton(SET_frame, text = sets[4][0], value = sets[4][1], variable = selected_set)

setrb1.grid(row = 1, column = 0, sticky = W)
setrb2.grid(row = 2, column = 0, sticky = W)
setrb3.grid(row = 3, column = 0, sticky = W)
setrb4.grid(row = 4, column = 0, sticky = W)
setrb5.grid(row = 5, column = 0, sticky = W)

selected_set.set('01') #default value

#set number box
setNumberLabel = Label(SET_frame, text = "Set Number: ", height=1, width = 10)  
setNumberLabel.grid(row = 6, column = 0, sticky = W, pady = 2)
setNumberInput = tk.Text(SET_frame, height = 1, width = 4)
setNumberInput.grid(row = 6, column = 1, padx = 8, sticky = W)

#main loop that every program has
while True:
   root.mainloop()

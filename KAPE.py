# A program for Task of the "Basics of programming"
# "KAPE Gallery"  v. 1.1.2
# To Open your images you have to change the argument PATH_GALLERY and ADDRES
# which located on the 22 and 23 lines.
# For example: PATH_GALLERY='C:\\Users\\1\\Desktop\\фотографии\\'
#              ADDRES = ' "C:\\Users\\1\\Desktop\\фотографии\\" '
# Programm have been written on the Python 2.7.5 and 2.7.6
# and not tested with the Python 2.7.7 and more newer.
# This program have "Open source softwre" license.
# Thank you for using our project, we wish that you will be pleased.


import os
from Tkinter import *
import tkFileDialog
import subprocess
from PIL import Image
from PIL import ImageTk


class Screen():
     def __init__(self):
          self.ROOT = Tk()
          self.ROOT.title('KAPE Gallery')
          self.ROOT.maxsize(650,560)
          self.ROOT.minsize(650,560)
          self.MAIN_MENU = Menu(self.ROOT)    # Creating menu
          self.ROOT.config(menu=self.MAIN_MENU)    # Add Menu to the Main Window
          self.FILE_MENU = Menu(self.MAIN_MENU)    # Creating submenu
          self.FILE_MENU2 = Menu(self.MAIN_MENU)    # Creating submenu №2
          self.FILE_MENU3 = Menu(self.MAIN_MENU)    # Creating submenu №3
          self.MAIN_MENU.add_cascade(label="File", menu=self.FILE_MENU)
          self.FILE_MENU.add_command(label="Open Gallery")
          self.FILE_MENU.add_separator()
          self.FILE_MENU.add_command(label="Exit", command=self.ROOT.destroy)
          self.MAIN_MENU.add_cascade(label="Options", menu=self.FILE_MENU3)
          self.FILE_MENU3.add_command(label="Configuration")
          self.MAIN_MENU.add_cascade(label="Help", menu=self.FILE_MENU2)
          self.FILE_MENU2.add_command(label="About")
          self.FILE_MENU2.add_separator()
          self.FILE_MENU2.add_command(label="Contact us")
          self.label = Label(self.ROOT, compound=TOP)
          self.label.pack()
          self.canvas = Canvas(self.ROOT, width=600, height=600,bg='green')
          self.ChangePicture(0)


          self.frame = Frame(self.ROOT)
          self.frame.pack()
          # Button to change the picture(back)
          Button(self.frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
               cursor='hand2',bg='dark green', fg='white', text='Previous picture',
               command=lambda: self.ChangePicture(-1)).pack(side=LEFT)
          # Button to change the picture(forward)

          Button(self.frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
               cursor='hand2',bg='dark green', fg='white', text='Next picture',
               command=lambda:self.ChangePicture(+1)).pack(side=LEFT)
          # Button fo0000000 closing the program
          Button(self.frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
               cursor='hand2',bg='dark green', fg='white', text='Quit',
               command=self.ROOT.destroy).pack(side=LEFT)

          self.ROOT.mainloop()


     
     def OpenPicture(self, PATH_GALLERY, image_list, text_list):
         for ROOT, DIRS, FILES in os.walk(PATH_GALLERY): 
             for NAME in FILES:
                 FULL_NAME = os.path.join(ROOT, NAME)
                 image_list.append(FULL_NAME)
                 text_list.append(NAME)
        

    
     def ChangePicture(self, SHIFT):
          self.OpenPicture(PATH_GALLERY, image_list, text_list)
          global CURRENT
          self.CURRENT = 0
          if not (0 <= self.CURRENT + SHIFT < len(image_list)):
            # что тут было? :D
            return
          self.CURRENT += SHIFT
          self.IMAGE = Image.open(image_list[self.CURRENT])
          self.PHOTO = ImageTk.PhotoImage(self.IMAGE)
          self.label['text'] = text_list[self.CURRENT]
          self.label['image'] = self.PHOTO
          self.label.PHOTO = self.PHOTO

         
image_list = []
text_list = []

PATH_GALLERY = 'C:\\Users\\user\\Desktop\\Программрование\\Python\\Task2\\arts\\'

WINDOW = Screen()
WINDOW.OpenPicture(PATH_GALLERY,image_list, text_list)







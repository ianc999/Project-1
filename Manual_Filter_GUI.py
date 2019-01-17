"""
A module that makes a GUI to sort solar panels easily.
This is for the manual selection of solar panels. One would select yes or no as options
for whether or not the image displayed has IR light. Images that do contain IR light will
be outputted as a JSON file.
"""

import tkinter
import tkinter.messagebox
from tkinter import font
from json import loads
from json import dump
from PIL import ImageTk, Image
import cv2
import PIL
import os
import glob
import shutil
import _json

# Creating the structure of the GUI
top = tkinter.Tk()
top.title("IR Light Filter")
top.geometry("20000x20000")

# Inputting the contents in the incoming JSON file
input_file = open('C:/Users/aa123/Desktop/input.json')
input_file_contents = input_file.read()
input_dict = loads(input_file_contents)
img_list = input_dict['positive']

counter = 0
positive = []

# Setting up the "Yes" button which will collect all the images into a file when clicked
def handle_btn_click_yes():
    global counter
    positive.append(img_list[counter])
    counter = counter+1
    img_2 = ImageTk.PhotoImage(Image.open(img_list[counter]).resize((600, 600), Image.ANTIALIAS))
    panel.configure(image=img_2)
    panel.image = img_2

# Setting up the "No" button which will simply move on to the next picture when clicked
def handle_btn_click_no():
    global counter
    counter = counter+1
    img_3 = ImageTk.PhotoImage(Image.open(img_list[counter]).resize((600, 600), Image.ANTIALIAS))
    panel.configure(image=img_3)
    panel.image = img_3

# Importing the first picture and setting up the contents within the GUI
img = ImageTk.PhotoImage(Image.open(img_list[counter]).resize((600, 600), Image.ANTIALIAS))
panel = tkinter.Label(top, image= img)
panel.pack(fill = "none", expand = "no")

# Setting up the dimensions of the buttons and assigning their functions
button = tkinter.Button(top, text =("Yes"), command = handle_btn_click_yes, padx = 275, pady = 100)
button.pack(side="left", fill="both")
button.config(bg='green',fg='white')
button.config(font=('helvetica',50))
button = tkinter.Button(top, text ="No", command = handle_btn_click_no, padx = 275, pady = 100)
button.pack(side="right", fill="both")
button.config(bg='red',fg='white')
button.config(font=('helvetica',50))

top.mainloop()

# Converting the collected images and outputting as a JSON file
data = {
    "positive": [positive]
}
with open('positive_file.json', 'w') as write_file:
    dump(data, write_file)

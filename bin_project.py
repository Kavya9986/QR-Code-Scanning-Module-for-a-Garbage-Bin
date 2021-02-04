#################################################################################################################

# PROJECT TITLE : Qrcode scanning module for a garbage bin
# USAGE : python p9.py 
# csv file: USERID.csv
# Date: 18 March 2020
# Author : Kavya S Jain

############################################## PROJECT CODE ######################################################

import cv2
import pyzbar.pyzbar as pyzbar
import numpy as numpy
import csv
from time import sleep

# writes adat into the file named "USERID.csv"
def reports():
    global i
    i=100
    with open('USERID.csv', 'r', newline='') as files:
        var=csv.reader(files)
        for line in var:
            if line[0]==str(obj.data)[1:]:
                i=i+100
    with open('USERID.csv', 'a', newline='') as file:
        fieldnames = ['USER ID', 'COINS']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'USER ID': str(obj.data)[1:], 'COINS': i})

font=cv2.FONT_HERSHEY_SIMPLEX
cap=cv2.VideoCapture(0)
while 1 :
    _ , frame = cap.read()
    decodedObjects=pyzbar.decode(frame)
    for obj in decodedObjects:
        cv2.putText(frame,str(obj.data)[1:],(50,50),font,1,(255,0,0),3)
    cv2.imshow("frame",frame)
    if cv2.waitKey(10)==77:
        reports()
        cap.release()
        break
    else:
        continue

cap.release()
cv2.destroyAllWindows()

# additional function after destroying the windows.
with open('USERID.csv', 'r', newline='') as files:
        var=csv.reader(files)
        userids=[]
        coins=[]
        for line in var:
                userids.append(line[0])
                coins.append(line[1])

#################################################### GUI ###################################################

import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title("Check your coins")
b=StringVar()
def check():
    a=0
    c=b.get()
    new_userids=userids[::-1]
    new_coins=coins[::-1]
    for user in new_userids:
        if user==c:
            label1=Label(window,text="You have",font=50).grid(row=7,column=59,sticky=W)
            label1=Label(window,text=new_coins[new_userids.index(user)],font=50).grid(row=7,column=60,sticky=W)
            label1=Label(window,text="coins !",font=50).grid(row=7,column=63,sticky=W)
            break
        else:   
            a=a+1
            continue
    if a==len(userids):
        label2=Label(window,text="Not a valid user",font=50).grid(row=7,column=50,sticky=W)

Label(window, text="CHECK YOUR REWARD HERE!",font=40).grid(row=0,column=50,sticky=W)
Label(window, text="Enter your USER ID",font=30).grid(row=5,column=25,sticky=W) 
Entry(window, textvariable = b,font=30).grid(row=5, column=26, sticky=E)

Click_button = Button(window, text="Check coins", command=check,font=30).grid(row=6, column=25, sticky=W)
Click_button = Button(window, text="Exit", command=window.destroy,font=30).grid(row=7, column=25, sticky=W)
window.mainloop()

########################################## USER GUIDE ################################################

#  In the terminal python bin_project.py
# Your camera wil turn on
# Show the QR code in front of the camera until you see your user_id on the screen.
# Press Ctrl-M.
# To check your reward points use the application else Exit.
# NOTE : You can fine the logs of the users and track their activity in the file called USERID.csv

########################################### END ######################################################


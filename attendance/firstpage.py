#import module from tkinter for UI
from Tkinter import *
from playsound import playsound
import os
import subprocess
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("python dataset_capture.py")
    
def function2():
    
    os.system("python training_dataSet.py")

def function3():

    os.system("python recognizer.py")
    playsound('sound.mp3')

def function5():    
   #os.startfile(os.getcwd()+"/developers/diet1frame1firstcopy.html");
   #os.system(os.getcwd()+"/developers/diet1frame1firstcopy.html")
   subprocess.call("google-chrome developers/diet1frame1firstcopy.html", shell=True)

def function6():

    root.destroy()

def attend():
    subprocess.call("libreoffice firebase/attendance_files/attendance.xls", shell=True)
    #os.system("open -a 'libreoffice' 'firebase/attendance_files/attend.xls'")
    #os.startfile(os.getcwd()+"/firebase/attendance_files/attend.xls")

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Developers",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()


from io import BufferedRandom
from os import read
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self , root):
        self.root=root
        self.root.geometry("1300x650+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=50)

        img_top=Image.open(r"college_images\Developer1.jpg")
        img_top=img_top.resize((1300,650),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl1=Label(self.root,image=self.photoimg_top)
        f_lbl1.place(x=0,y=50,width=1300,height=650)

       
        #Developer info
        dep_label=Label(f_lbl1,text="hello Everyone,",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=20)

        dep_label=Label(f_lbl1,text="Welcome to my project.",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=70)

        img_top2=Image.open(r"college_images\Swa.jpg")
        img_top2=img_top2.resize((200,200),Image.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        img_top2=Label(f_lbl1,image=self.photoimg_top2)
        img_top2.place(x=500,y=200,width=200,height=200)

        b1_1=Button(f_lbl1,text="Swapnil Chopade",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=400,width=200,height=40)









if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1300x650+0+0")

    #=============Variable=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self._var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()   



    #==========bg image==================
        self.bg=ImageTk.PhotoImage(file=r"college_images\di.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

    #===========left image=================
        self.bg1=ImageTk.PhotoImage(file=r"college_images\img1.jpeg")
        left_lbl=Label(self.root,image=self.bg)
        left_lbl.place(x=50,y=100,width=470,height=550)

    #====== main frame===================
        frame=Frame(self.root,bg="white")
        frame.place(x=240,y=60,width=800,height=550)
        registre_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        registre_lbl.place(x=20,y=20)

    #===========label and entry===========
    #====================row1=====
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")  
        fname.place(x=50,y=100)  

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white")  
        l_name.place(x=370,y=100)  

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

    #=====row2=
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

    #=========row3=========
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self._var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","your birth place","your girlfriend name","your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

    #=====row4======
        pswd=Label(frame,text="password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.confim_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.confim_pswd.place(x=370,y=340,width=250)

    #==== check button==========
        self.var_check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=380)

    #====button==============
        img=Image.open(r"college_images\BestFacialRecognition.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"college_images\BestFacialRecognition.jpg")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)

        #=====function declaration====
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self._var_securityQ.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree your terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self._var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")



if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
    


from io import BufferedRandom
from os import read
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter as tk
from tkcalendar import DateEntry

class Student:
    def __init__(self , root):
        self.root=root
        self.root.geometry("1300x650+0+0")
        self.root.title("Face Recognition System")

#===================variable=================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_phone=StringVar()


        #first image
        img=Image.open(r"college_images\facialrecognition.png")
        img=img.resize((1300,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0, width=1300,height=100)

       

        #bg image
        img3=Image.open(r"college_images\Bg3.jpg")
        img3=img3.resize((1300,650),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100, width=1300,height=650)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=40,width=1300,height=520)

        #left label fram
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=620,height=500)

       
        title_lbl=Label(Left_frame,text="STUDENT DETAILS",font=("times new roman",25,"bold"),bg="deep sky blue",fg="black")
        title_lbl.place(x=0,y=0,width=620,height=60)

        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=3,y=60,width=610,height=110)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer science","electrical","mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame, text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","MCA","MBA","CS","EC")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year ,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=170,width=610,height=300)

        #student id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id , width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20,font=("times new roman",11,"bold"))
        studentName_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        #class divison
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)


        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=18 ,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("A","B","c")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=0,pady=5,sticky=W)


        #Roll no
        roll_no_label=Label(class_student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=0,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

       
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18 ,font=("times new roman",11,"bold"),state="readonly")
        gender_combo["values"]=("male","female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=0,pady=10,sticky=W)


        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        dob_entry=DateEntry(class_student_frame,width=24, year=2023, month=7, day=14,background='darkblue', foreground='white', borderwidth=2)
        dob_entry.grid(row=2,column=3,padx=0,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email, width=20,font=("times new roman",11,"bold"))
        email_entry.grid(row=3,column=1,padx=0,pady=5,sticky=W)

        #Phone no.
        phone_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20,font=("times new roman",11,"bold"))
        phone_entry.grid(row=3,column=3,padx=0,pady=5,sticky=W)
        
        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address, width=18,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=0,pady=5,sticky=W)
        
        #Teacher
        teacher_label=Label(class_student_frame,text="HOD:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20,font=("times new roman",11,"bold"))
        teacher_entry.grid(row=4,column=3,padx=0,pady=5,sticky=W)

        #radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No photo sample",value="NO")
        radiobtn2.grid(row=6,column=1)

        #button frame
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=200,width=600,height=35)

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data, width=14,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data, width=14,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data, width=14,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data, width=14,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=600,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="TAKE PHOTO SAMPLE",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="UPDATE PHOTO SAMPLE",command=self.generate_dataset,width=30,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
        update_photo_btn.grid(row=0,column=1)

        
       #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=640,y=0,width=620,height=500)

        img_right=Image.open(r"college_images\topR.jpg")
        img_right=img_right.resize((620,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0, width=620,height=130)

        #==========================Search System====================================
        search_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        search_frame.place(x=3,y=135,width=610,height=50)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",10,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",11,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=13,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",11,"bold"),bg="blue",fg="white",cursor="hand2")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",11,"bold"),bg="blue",fg="white",cursor="hand2")
        showAll_btn.grid(row=0,column=4,padx=4)

        #===========================Table Frame===============================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=190,width=610,height=285)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.xview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone NO.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#=================== function declaration=================
    def add_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()==""or self.va_std_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                    
                                                                                                    ))
                                                                                                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been addes successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error ",f"Due to :{str(es)}",parent=self.root)

    #======fetch data==========================================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#============get cursor============
    def get_cursor(self,event=""):
        curser_focus=self.student_table.focus()
        content=self.student_table.item(curser_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.va_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()==""or self.va_std_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)

        else:
            try:
                update=messagebox.askyesno("update","DO You Want To Update Student Details",parent=self.root)
                if update>0:
                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.va_std_id.get()
                                                                                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must me required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select course")
        self.var_year.set("Select year")
        self.var_semester.set("Select semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #============= Generate data set or Take photo Samples  ==============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()==""or self.va_std_id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:     
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.va_std_id.get()==id+1
                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=========== Load predifiend data on face frontals from opencv =============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('cropped Face',face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"due To:{str(es)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

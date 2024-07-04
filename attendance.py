from io import BufferedRandom
from os import read
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:

        def __init__(self , root):
                self.root=root
                self.root.geometry("1350x650+0+0")
                self.root.title("Face Recognition System")

       # =============variable===============
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_attendance=StringVar()
    

        #first image
                img=Image.open(r"college_images\smart-attendance.jpg")
                img=img.resize((650,200),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0, width=650,height=150)

       

        #second image
                img1=Image.open(r"college_images\clg.jpg")
                img1=img1.resize((650,200),Image.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=650,y=0, width=650,height=150)

        #bg image
                img3=Image.open(r"college_images\Bg3.jpg")
                img3=img3.resize((1350,650),Image.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=150, width=1350,height=650)

                title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="orange")
                title_lbl.place(x=0,y=0,width=1350,height=45)

                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=0,y=48,width=1350,height=600)

        #left label fram
                Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
                Left_frame.place(x=2,y=0,width=650,height=450)

                img_left=Image.open(r"college_images\topL.jpg")
                img_left=img_left.resize((650,100),Image.LANCZOS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(Left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=650,height=100)

                left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
                left_inside_frame.place(x=3,y=100,width=640,height=320)

        # Lebaland entry
        # Attendance id
                attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
                attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

                attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
                attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # name
                rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
                rollLabel.grid(row=0,column=2,padx=4,pady=8)
        

                rollLabel_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
                rollLabel_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # name
                nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
                nameLabel.grid(row=1,column=0)

                nameLabel=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
                nameLabel.grid(row=1,column=1,pady=8)

        # Department
                depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
                depLabel.grid(row=1,column=2)

                depLabel=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
                depLabel.grid(row=1,column=3,pady=8)

        # time
                timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
                timeLabel.grid(row=2,column=0)

                atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
                atten_time.grid(row=2,column=1,pady=8)
        #date
                datelabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
                datelabel.grid(row=2,column=2)

                datelabel=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
                datelabel.grid(row=2,column=3,pady=8)

        # Attendance
                attendanceLabel=Label(left_inside_frame,text="Attendance status:",bg="white",font="comicsansns 11 bold")
                attendanceLabel.grid(row=3,column=0)

                self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
                self.atten_status["value"]=("status","Present","Absent")
                self.atten_status.grid(row=3,column=1,pady=8)
                self.atten_status.current(0)

        # button frame
                btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=280,width=638,height=30)

                save_btn=Button(btn_frame,text="Import csv",command=self.importCsv, width=15,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
                save_btn.grid(row=0,column=0)

                update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv, width=15,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
                update_btn.grid(row=0,column=1)

                delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
                delete_btn.grid(row=0,column=2)

                reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
                reset_btn.grid(row=0,column=3)
        
        #Right label fram
                Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
                Right_frame.place(x=660,y=0,width=610,height=450)

                tabel_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
                tabel_frame.place(x=5,y=0,width=600,height=430)

        # =================scroll bar table=============
                scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

                self.attendanceReporttable=ttk.Treeview(tabel_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.attendanceReporttable.xview)
                scroll_y.config(command=self.attendanceReporttable.yview)

                self.attendanceReporttable.heading("id",text="Attendance ID")
                self.attendanceReporttable.heading("roll",text="roll")
                self.attendanceReporttable.heading("name",text="name")
                self.attendanceReporttable.heading("department",text="department")
                self.attendanceReporttable.heading("time",text="time")
                self.attendanceReporttable.heading("date",text="date")
                self.attendanceReporttable.heading("attendance",text="Attendance")

                self.attendanceReporttable["show"]="headings"

                self.attendanceReporttable.column("id",width=100)
                self.attendanceReporttable.column("roll",width=100)
                self.attendanceReporttable.column("name",width=100)
                self.attendanceReporttable.column("department",width=100)
                self.attendanceReporttable.column("time",width=100)
                self.attendanceReporttable.column("date",width=100)
                self.attendanceReporttable.column("attendance",width=100)


                self.attendanceReporttable.pack(fill=BOTH,expand=1)

                self.attendanceReporttable.bind("<ButtonRelease>",self.get_cursor)

        #===============fetch data==============


        def fetchData(self,rows):
            self.attendanceReporttable.delete(*self.attendanceReporttable.get_children())
            for i in rows:
                self.attendanceReporttable.insert("",END,values=i)

            # import csv
        def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV file","*.csv"),("ALl file","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                    self.fetchData(mydata)
                #export csv
        def exportcsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("No Data","no data found to export",parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV file","*.csv"),("ALl file","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("data export","your data exported to"+ os.path.basename(fln)+"successfully")
            except Exception as es:
                messagebox.showerror("Error ",f"Due to :{str(es)}",parent=self.root)
        def get_cursor(self,event=""):
            cursor_row=self.attendanceReporttable.focus()
            content=self.attendanceReporttable.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])


        def reset_data(self):
            
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")

        

        

        
            

                

if __name__=="__main__" :
    root=Tk()
    obj=Attendance(root)
    root.mainloop()


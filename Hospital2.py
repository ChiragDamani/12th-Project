from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title(" + Hospital Management System")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="gray")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar() 





        lbltitle=Label(self.root,bd=20,relief=RIDGE,text=" + HOSPITAL MANAGEMENT SYSTEM",fg="maroon",bg="black",font=("times new roman",35,"bold"))
        lbltitle.pack(side=TOP,fill=X)


        #=========================DataFrame==========
        Dataframe=Frame(self.root,bd=10,relief=RIDGE,bg="powder blue")
        Dataframe.place(x=0,y=95,width=1366,height=400)


        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=95,width=1360,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=15,padx=10,relief=RIDGE,bg="powder blue",
                                              font=("arial",15,"bold"),text="Patient Information",)
        DataFrameLeft.place(x=0,y=5,width=950,height=356)

        DataFrameRight=LabelFrame(DataFrame,bd=15,padx=10,relief=RIDGE,bg="powder blue",
                                                font=("arial",15,"bold"),text="Prescription",)
        DataFrameRight.place(x=955,y=5,width=360,height=356)


        #=================Buttons===============
        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE,bg="black")
        ButtonFrame.place(x=0,y=496,width=1366,height=70)


        #==============Details Frame=============
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE,bg="black")
        DetailsFrame.place(x=0,y=565,width=1366,height=202)

        

        #=================DataFrame Left===============

        lblNameTablet=Label(DataFrameLeft,text="Name of Tablet",font=("arial",12,"bold"),padx=2, pady=6,bg="powder blue")
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),width=18)
        comNameTablet["values"]=("Nice","Coronil","Acetaminophen","Addreall","Amlodipine","Antivan","Crocin","Dolo 650")
        comNameTablet.grid(row=0,column=1,sticky=W)

        lblref=Label(DataFrameLeft,text="Reference No: ",font=("arial",12,"bold"),padx=2,pady=4,bg="powder blue")
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.ref,width=20)
        txtref.grid(row=1,column=1,sticky=W)

        lblDose=Label(DataFrameLeft,text="Dose: ",font=("arial",12,"bold"),padx=2,pady=4,bg="powder blue")
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Dose,width=20)
        txtDose.grid(row=2,column=1,sticky=W)

        lblNoOftablets=Label(DataFrameLeft,text="No of Tablets: ",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NumberofTablets,width=20)
        txtNoOftablets.grid(row=3,column=1,sticky=W)

        lblLot=Label(DataFrameLeft,text="Lot : ",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Lot,width=20)
        txtLot.grid(row=4,column=1,sticky=W)

        lblissueDate=Label(DataFrameLeft,text="Issue Date: ",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Issuedate,width=20)
        txtissueDate.grid(row=5,column=1,sticky=W)

        lblExpDate=Label(DataFrameLeft,text="Expiry Date: ",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=20)
        txtExpDate.grid(row=6,column=1,sticky=W)

        lblDailyDose=Label(DataFrameLeft,text="Daily Dose: ",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=20)
        txtDailyDose.grid(row=7,column=1,sticky=W)

        lblSideEffect=Label(DataFrameLeft,text="Side Effect: ",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.sideEfect,width=20)
        txtSideEffect.grid(row=8,column=1,sticky=W)

        lblFurtherinfo=Label(DataFrameLeft,text="Further Info: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblFurtherinfo.grid(row=0,column=5,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=20)
        txtFurtherinfo.grid(row=0,column=6,sticky=W)

        lblBloodPressure=Label(DataFrameLeft,text="Blood Pressure: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblBloodPressure.grid(row=1,column=5,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=20) 
        txtBloodPressure.grid(row=1,column=6,sticky=W)

        lblStorage=Label(DataFrameLeft,text="Storage Advice: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblStorage.grid(row=2,column=5,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=20)
        txtStorage.grid(row=2,column=6,sticky=W)

        lblMedicine=Label(DataFrameLeft,text="Medication: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblMedicine.grid(row=3,column=5,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=20)
        txtMedicine.grid(row=3,column=6,sticky=W)

        lblPatiendId=Label(DataFrameLeft,text="Patient ID: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblPatiendId.grid(row=4,column=5,sticky=W)
        txtPatiendId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=20)
        txtPatiendId.grid(row=4,column=6,sticky=W)

        lblNhsNumber=Label(DataFrameLeft,text="NHS Number: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblNhsNumber.grid(row=5,column=5,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=20)
        txtNhsNumber.grid(row=5,column=6,sticky=W)

        lblPatientname=Label(DataFrameLeft,text="Patient Name: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblPatientname.grid(row=6,column=5,sticky=W)
        txtPatientname=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=20)
        txtPatientname.grid(row=6,column=6,sticky=W)

        lblDateOfBirth=Label(DataFrameLeft,text="Date of Birth: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblDateOfBirth.grid(row=7,column=5,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=20)
        txtDateOfBirth.grid(row=7,column=6,sticky=W)

        lblPatientAddress=Label(DataFrameLeft,text="Patient Address: ",font=("arial",12,"bold"),padx=4,pady=6,bg="powder blue")
        lblPatientAddress.grid(row=8,column=5,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=20)
        txtPatientAddress.grid(row=8,column=6,sticky=W)


        #===================DataFrameRight=========================
        self.txtPrescription=Text(DataFrameRight,width=34,height=16,font=("arial",12,"bold"))
        self.txtPrescription.grid(row=0,column=0)


        #====================Buttons===============================
        btnPrescription=Button(ButtonFrame,command=self.iPrescription,padx=16,pady=1,bd=4,fg="white",bg="black",font=("arial",12,"bold"),width=17,height=1,text="Prescription")
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(ButtonFrame,command=self.iPrescriptionData,padx=16,pady=1,bd=4,fg="white",bg="maroon",font=("arial",12,"bold"),width=17,height=1,text="Prescription Data")
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,command=self.Update,padx=16,pady=1,bd=4,fg="white",bg="maroon",font=("arial",12,"bold"),width=17,height=1,text="Update")
        btnUpdate.grid(row=0,column=2)

        btnClear=Button(ButtonFrame,command=self.iDelete,padx=16,pady=1,bd=4,fg="white",bg="maroon",font=("aredrial",12,"bold"),width=17,height=1,text="Delete")
        btnClear.grid(row=0,column=3)
        
        btnClear=Button(ButtonFrame,command=self.clear,padx=16,pady=1,bd=4,fg="white",bg="maroon",font=("arial",12,"bold"),width=17,height=1,text="Clear")
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,command=self.iExit,padx=16,pady=1,bd=4,fg="white",bg="maroon",font=("arial",12,"bold"),width=20,height=1,text="Exit")
        btnExit.grid(row=0,column=5)



        #======================Table and ScrollBar===========================

        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailsFrame,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose",
                                                            "storage","nhsnumber","pname","dob","address" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Ref")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="address")

        self.hospital_table["show"]="headings"

    
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        #===========================Functionality Declaration===========================
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are Required!!")
        else:
            conn=mysql.connector.connect(host="localhost" , user ="root" , password= "Lamborghini99" ,database="hospital_data")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                                    (
                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NumberofTablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.StorageAdvice.get(),
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get()
                                                                                                                                ))      
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Prescription Data Added Successfully!!")
    
    def Update(self):
            conn=mysql.connector.connect(host="localhost" , user ="root" , password= "Lamborghini99" ,database="hospital_data")
            my_cursor=conn.cursor()
            my_cursor.execute("update hospital set Name_of_tablets=%s,dose=%s,Numbersoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patienaddress=%s where Reference_No=%s",(
                                                                                                                                                                                                                                    self.Nameoftablets.get(),
                                                                                                                                                                                                                                    self.ref.get(),
                                                                                                                                                                                                                                    self.Dose.get(),
                                                                                                                                                                                                                                    self.NumberofTablets.get(),
                                                                                                                                                                                                                                    self.Lot.get(),
                                                                                                                                                                                                                                    self.Issuedate.get(),
                                                                                                                                                                                                                                    self.ExpDate.get(),
                                                                                                                                                                                                                                    self.DailyDose.get(),
                                                                                                                                                                                                                                    self.StorageAdvice.get(),
                                                                                                                                                                                                                                    self.nhsNumber.get(),
                                                                                                                                                                                                                                    self.PatientName.get(),
                                                                                                                                                                                                                                    self.DateOfBirth.get(),
                                                                                                                                                                                                                                    self.PatientAddress.get(),          

                                                                                                                                                                                                                                                                ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success","Prescription Data Updated Successfully!!")


    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issuedate:\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Expdate:\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t"+self.PatientAddress.get()+"\n")
        

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost" , user ="root" , password= "Lamborghini99" ,database="hospital_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        contents=self.hospital_table.item(cursor_row)
        row=contents['values']
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iDelete(self):
        conn=mysql.connector.connect(host="localhost" , user ="root" , password= "Lamborghini99" ,database="hospital_data")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success","The records have been deleted!!")
    
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System", 'Do you want to exit?')
        if iExit>0:
            root.destroy()
            return
        

root = Tk()
ob = Hospital(root)
root.mainloop()
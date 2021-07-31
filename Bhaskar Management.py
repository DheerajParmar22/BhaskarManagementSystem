from tkinter import *
from tkinter import ttk
import pymysql
class Bhaskar:
    def __init__(self,root):
        self.root=root
        self.root.title("BHASKAR MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="BHASKAR MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #All Variables
        self.name_var=StringVar()
        self.contact_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.area_var=StringVar()
        self.copies_var=StringVar()


        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="CRIMSON")
        Manage_Frame.place(x=20,y=100,width=450,height=595)

        m_title=Label(Manage_Frame,text="Manage Hawkers",bg="CRIMSON",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_name=Label(Manage_Frame,text="Hawker Name",bg="CRIMSON",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        lbl_contact=Label(Manage_Frame,text="Contact",bg="CRIMSON",fg="White",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,text="Email id",bg="CRIMSON",fg="White",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_Frame, text="Gender", bg="CRIMSON", fg="White", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",12,"bold"),state='readonly')
        combo_gender['values']=("Male","Female")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_area=Label(Manage_Frame,text="Area",bg="CRIMSON",fg="White",font=("times new roman",20,"bold"))
        lbl_area.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        lbl_copies = Label(Manage_Frame, text="No. of Copies", bg="CRIMSON", fg="White", font=("times new roman", 20, "bold"))
        lbl_copies.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        lbl_address=Label(Manage_Frame, text="Address", bg="CRIMSON", fg="White", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",12,"bold"),bd=3,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman", 12, "bold"), bd=3, relief=GROOVE)
        txt_contact.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman", 12, "bold"), bd=3, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        txt_area=Entry(Manage_Frame,textvariable=self.area_var,font=("times new roman", 12, "bold"), bd=3, relief=GROOVE)
        txt_area.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        txt_copies=Entry(Manage_Frame,textvariable=self.copies_var,font=("times new roman", 12, "bold"), bd=3, relief=GROOVE)
        txt_copies.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.txt_address=Text(Manage_Frame, width=25, height=4, font=("", 10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #Buttom Frame

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="CRIMSON")
        btn_Frame.place(x=15, y=523, width=410)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_hawkers).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)


        #Details Frame
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="CRIMSON")
        Details_Frame.place(x=500, y=100, width=800, height=590)

        lbl_search=Label(Details_Frame, text="Search By", bg="CRIMSON", fg="White",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search=ttk.Combobox(Details_Frame,width=10,font=("times new roman", 12, "bold"), state='readonly')
        combo_search['values'] = ("Name", "Contact","Area")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_Search=Entry(Details_Frame,width=15,font=("times new roman", 13, "bold"), bd=3, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(Details_Frame, text="Search", width=10,pady=3).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Details_Frame, text="Show All", width=10,pady=3).grid(row=0, column=4, padx=10, pady=10)

        #Table Frame
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="CRIMSON")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Hawker_table=ttk.Treeview(Table_Frame,columns=("name","contact","email","copies","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Hawker_table.xview)
        scroll_y.config(command=Hawker_table.yview)
        Hawker_table.heading("name",text="Name")
        Hawker_table.heading("contact",text="Contact")
        Hawker_table.heading("email",text="Email")
        Hawker_table.heading("copies",text="Copies")
        Hawker_table.heading("address",text="Address")
        Hawker_table['show']='headings'
        Hawker_table.column("name",width=200)
        Hawker_table.column("contact", width=200)
        Hawker_table.column("email", width=200)
        Hawker_table.column("copies", width=200)
        Hawker_table.column("address", width=200)
        Hawker_table.pack(fill=BOTH,expand=1)

    def add_hawkers(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cursor=con.cursor()
        cursor.execute("insert into student system(%s,%s,%s,%s,%s,%s,%s)",(self.name_var.get(),
                                                                           self.contact_var.get(),
                                                                           self.email_var.get(),
                                                                           self.gender_var.get(),
                                                                           self.area_var.get(),
                                                                           self.contact_var.get(),
                                                                           self.txt_address.get('1.0',END)
                                                                           ))
        con.commit()
        con.close()


root = Tk()
ob=Bhaskar(root)
root.mainloop()

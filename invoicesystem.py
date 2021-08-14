from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
    # .........variable.............
    # ........cosmetic........
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spary=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
    # ......glocery.....
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.dall=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
    # .......cold_drinks.....
        self.maza=IntVar()
        self.seven_up=IntVar()
        self.tiger=IntVar()
        self.sprit=IntVar()
        self.fruto=IntVar()
        self.speed=IntVar()

    # .....total product price....
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
    # .......customer .....
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()




    #..................customer details frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cpn_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_phone,bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,font="arial 15",textvariable=self.search_bill,bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font='arial 12 bold').grid(row=0,column=6,padx=10,pady=10)

        #...........cosmatics frame
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F2.place(x=5, y=180,width=325,height=380)
        bath_lbl=Label(F2,text="Bath Soap",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt =Entry(F2, width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        face_cream__txt =Entry(F2, width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        face_w_lbl=Label(F2,text="Face Wash",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        face_w__txt =Entry(F2, width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        Hair_s__txt =Entry(F2, width=10,textvariable=self.spary,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        Hair_g_lbl=Label(F2,text="Hair Gell",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Hair_g__txt =Entry(F2, width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        Body__lbl=Label(F2,text="Body Loshan",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        Body__txt =Entry(F2, width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        #...........Grocery frame
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Glocery", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=340, y=180,width=325,height=380)
        g1_lbl=Label(F3,text="Rice",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        g1_txt =Entry(F3, width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        g2_lbl=Label(F3,text="Food Oil",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        g2_cream__txt =Entry(F3, width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        g3_lbl=Label(F3,text="Daal",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        g3__txt =Entry(F3, width=10,textvariable=self.dall,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        g4_lbl=Label(F3,text="Wheat",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        g4__txt =Entry(F3, width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        g5_lbl=Label(F3,text="Sugar",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        g5__txt =Entry(F3, width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        g6__lbl=Label(F3,text="Tea",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        g6__txt =Entry(F3, width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)#...........cosmatics frame


        #...........cold Drinks............
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=670, y=180,width=325,height=380)
        c1_lbl=Label(F4,text="Maza",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        c1_txt =Entry(F4, width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        c2_lbl=Label(F4,text="7Up",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        c2_cream__txt =Entry(F4, width=10,textvariable=self.seven_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        c3_lbl=Label(F4,text="Tiger",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        c3__txt =Entry(F4, width=10,textvariable=self.tiger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        c4_lbl=Label(F4,text="Sprite",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        c4__txt =Entry(F4, width=10,textvariable=self.sprit,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        c5_lbl=Label(F4,text="Fruto",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        c5__txt =Entry(F4, width=10,textvariable=self.fruto,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        c6__lbl=Label(F4,text="Speed",font=('times new roman',16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        c6__txt =Entry(F4, width=10,textvariable=self.speed,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

      #............Bill Area
        F5 =Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=340, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
#         .......Button Frame............
        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Cosmaetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN,).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price,font="arial 10 bold", bd=7, relief=SUNKEN, ).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cold_drink_price, bd=7, relief=SUNKEN, ).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmaetic Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cosmetic_tax, bd=7, relief=SUNKEN, ).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_tax,bd=7, relief=SUNKEN, ).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax",bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN, ).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)
        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_F, text="Genrate Bill",command=self.bill_area, bg="cadetblue", fg="white", pady=15, width=10, bd=2,font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        clear_btn=Button(btn_F,text="Claer",command=self.clear_data,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spary.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180
        self.total_costemic_price=float(
                                   self.c_s_p+
                                   self.c_fc_p+
                                   self.c_fw_p+
                                   self.c_hs_p+
                                   self.c_hg_p+
                                   self.c_bl_p
                                  )
        self.cosmetic_price.set("Tk. "+str(self.total_costemic_price))
        self.c_tax=(str(round((self.total_costemic_price*0.05),2)))
        self.cosmetic_tax.set("Tk. "+str(self.c_tax))


        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*240
        self.g_d_p=self.dall.get()*140
        self.g_w_p=self.wheat.get()*340
        self.g_s_p=self.sugar.get()*410
        self.g_t_p=self.tea.get()*440
        self.total_grocery_price = float(
            self.g_r_p+
            self.g_f_p+
            self.g_d_p+
            self.g_w_p+
            self.g_s_p+
            self.g_t_p
        )

        self.grocery_price.set("Tk. " + str(self.total_grocery_price))
        self.g_tax = (str(round((self.total_grocery_price * 0.05), 2)))
        self.grocery_tax.set("Tk. " + str(self.g_tax))

        self.d_m_p = self.maza.get() * 40
        self.d_s_p = self.seven_up.get() * 240
        self.d_t_p = self.tiger.get() * 140
        self.d_sp_p = self.sprit.get() * 340
        self.d_f_p = self.fruto.get() * 410
        self.d_spd_p = self.speed.get() * 440
        self.total_cold_drink_price = float(
            self.d_m_p +
            self.d_s_p +
            self.d_t_p +
            self.d_sp_p+
            self.d_f_p +
            self.d_spd_p

        )

        self.cold_drink_price.set("Tk. " + str(self.total_cold_drink_price))
        self.d_tax = (str(round((self.total_cold_drink_price * 0.05), 2)))
        self.cold_drink_tax.set("Tk. " + str(self.d_tax))

        self.Total_bill=float(
                              self.total_costemic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price
                              # self.c_tax+
                              # self.g_tax+
                              # self.d_tax

        )



    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tFahad Super Shop\n")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone Number:{self.c_phone.get()}")
        self.textarea.insert(END, "\n=====================================")
        self.textarea.insert(END, "\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END, "\n=====================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer  Details Must be Need")
        elif self.cosmetic_price.get()=="Tk. 0.0" and self.grocery_price.get()=="Tk. 0.0" and self.cold_drink_price.get()=="Tk. 0.0":
            messagebox.showerror("Error", "No Product Selected")
        else:

            self.welcome_bill()
            # -------cosmetics-----------
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.textarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.textarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spary.get() != 0:
               self.textarea.insert(END, f"\n Hair Sparay\t\t{self.spary.get()}\t\t{self.c_s_p}")
            if self.gell.get() != 0:
               self.textarea.insert(END, f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.loshan.get() != 0:
               self.textarea.insert(END, f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")
    #         *********grocery********
            if self.rice.get() != 0:
               self.textarea.insert(END, f"\n Rice \t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
               self.textarea.insert(END, f"\n Food oil \t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.dall.get() != 0:
               self.textarea.insert(END, f"\n Dall \t\t{self.dall.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
               self.textarea.insert(END, f"\n Wheat \t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
               self.textarea.insert(END, f"\n Sugar \t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
               self.textarea.insert(END, f"\n Tea \t\t{self.tea.get()}\t\t{self.g_t_p}")
    # **********cold drinks********
            if self.maza.get() != 0:
               self.textarea.insert(END, f"\n Wheat \t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.seven_up.get() != 0:
               self.textarea.insert(END, f"\n Seven up \t\t{self.seven_up.get()}\t\t{self.d_s_p}")
            if self.tiger.get() != 0:
               self.textarea.insert(END, f"\n Tiger \t\t{self.tiger.get()}\t\t{self.d_t_p}")
            if self.sprit.get() != 0:
               self.textarea.insert(END, f"\n Sprite \t\t{self.sprit.get()}\t\t{self.d_sp_p}")
            if self.fruto.get() != 0:
               self.textarea.insert(END, f"\n Fruto \t\t{self.fruto.get()}\t\t{self.d_f_p}")
            if self.speed.get() != 0:
               self.textarea.insert(END, f"\n Speed \t\t{self.speed.get()}\t\t{self.d_spd_p}")

            self.textarea.insert(END, f"\n-------------------------------------")
            if self.cosmetic_tax.get()!="Tk. 0.0":
              self.textarea.insert(END,f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")
            self.textarea.insert(END, f"\n-------------------------------------")
            if self.grocery_tax.get()!="Tk. 0.0":
              self.textarea.insert(END,f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
            self.textarea.insert(END, f"\n-------------------------------------")
            if self.cold_drink_tax.get()!="Tk. 0.0":
              self.textarea.insert(END,f"\n Cold Drinks Tax\t\t{self.cold_drink_tax.get()}")

            self.textarea.insert(END, f"\n Total Bill: \t\t\t Tk. {self.Total_bill}")
            self.textarea.insert(END, f"\n-------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askquestion("Save Bill","Do you Want to save the bill?")
        if op == "yes":
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                      self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Inavalid Bill No.")
    def clear_data(self):
        op = messagebox.askyesno("Clear","Do You Clear Data?")
        if op > 0:

            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spary.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            # ......glocery.....
            self.rice.set(0)
            self.food_oil.set(0)
            self.dall.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # .......cold_drinks.....
            self.maza.set(0)
            self.seven_up.set(0)
            self.tiger.set(0)
            self.sprit.set(0)
            self.fruto.set(0)
            self.speed.set(0)
            # .....total product price....
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            # .......customer .....
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do You Exit The App?")
        if op>0:
            self.root.destroy()

root=Tk()
ob=Bill_App(root)
root.mainloop()
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title('Billing Slip')
root.geometry('1280x720')
bg_color = "#4D0039"

# ============Variable===============
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
Rate = IntVar()
Quantity = IntVar()
bill_no = StringVar()
x = random.randint(1000, 9999)
bill_no.set(str(x))


global l
l = []

# ============funciton===============

def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t Welcome To Swanand Retails")
    textarea.insert(END, f"\n\nBil Number:\t\t{bill_no.get()}")
    textarea.insert(END, f"\nCustomer Name:\t\t{c_name.get()} ")
    textarea.insert(END, f"\nPhone Number:\t\t{c_phone.get()} ")
    textarea.insert(END, f"\n\n======================================")
    textarea.insert(END, f"\nProduct\t\t QTY\t\tPrice")
    textarea.insert(END, f"\n======================================\n")
    textarea.config(font="arial 15 bold")


def additm():
    n = Rate.get()
    m = Quantity.get()*n
    l.append(m)
    if item.get() == '':
        messagebox.showerror('ERROR', 'Please Enter the Item')
    else:
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t{Quantity.get()}\t\t{ m}\n")


def gbill():
    if c_name.get() == '' or c_phone.get()=='':
        messagebox.showerror('Error','Customer Details are Must')
    else:
        tex=textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END,tex)
        textarea.insert(END, f"\n======================================\n")
        textarea.insert(END, f"Total Paybill Amount: \t\t{sum(l)}")
        textarea.insert(END, f"\n======================================\n")
        save_bill()

def save_bill():
    op=messagebox.askyesno('Save Bill','Do Want to Save the Bill')
    if op>0:
        bill_details=textarea.get(1.0,END)
        f1=open("Bills/"+str(bill_no.get())+".txt","w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo('Saved',f'Bill No: {bill_no.get()} Saved Successfully')
    else:
        return

def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exit():
    op=messagebox.askyesno('Exit','Do You Want To Exit.')
    if op>0:
        root.destroy()
# ============Top Section===============
title = Label(root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("Algerian", 30, "bold"), pady=2)
title.pack(fill=X)

# Customer details frame
F1 = LabelFrame(root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
F1.place(x=0, y=80, relwidth=1)

cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, fg="white", font=("times new roman", 18, "bold"))
cname_lbl.grid(row=0, column=0, padx=20, pady=5)
cname_txt = Entry(F1, width=15, font="arial 15", bd=6, textvariable=c_name, relief=SUNKEN)
cname_txt.grid(row=0, column=1, pady=5, padx=6)

cphn_lbl = Label(F1, text="Phone No.:", bg=bg_color, fg="white", font=("times new roman", 18, "bold"))
cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
cphn_txt=Entry(F1,width=15,font="arial 15",bd=6,textvariable=c_phone,relief=SUNKEN)
cphn_txt.grid(row=0,column=3,pady=5,padx=6)

# ============Product Details=============
F2=LabelFrame(root, text="Product Details", bd=10, relief=GROOVE, font=("times new roman",15,"bold"),fg="gold", bg=bg_color)
F2.place(x=20, y=180,width=630,height=500)

itm_lbl = Label(F2,text='Product Name:',font=("times new roman:", 15, "bold"),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=40,pady=20)
itm_txt = Entry(F2,width=20,font=("arial", 15, "bold"),textvariable=item).grid(row=0,column=1,padx=30,pady=20)

rate = Label(F2,text='Product Rate:',font=("times new roman:", 15, "bold"),bg=bg_color,fg='lightgreen').grid(row=1,column=0,padx=30,pady=20)
rate_txt = Entry(F2,width=20,font=("arial", 15, "bold"),textvariable=Rate).grid(row=1,column=1,padx=30,pady=20)

quantity = Label(F2,text='Product Quantity:',font=("times new roman:", 15, "bold"),bg=bg_color,fg='lightgreen').grid(row=2,column=0,padx=30,pady=20)
quantity_txt = Entry(F2,width=20,font=("arial", 15, "bold"),textvariable=Quantity).grid(row=2,column=1,padx=30,pady=20)


#===========Button=========
btn1=Button(F2,text='Add item',font=("arial", 15, "bold"), command=additm,padx=5,pady=10,bg='yellow',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)

btn2=Button(F2,text='Genrate Bill',font=("arial", 15, "bold"),command=gbill,padx=5,pady=10,bg='yellow',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)

btn3=Button(F2,text='Clear',font=("arial", 15, "bold"),command=clear,padx=5,pady=10,bg='yellow',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)

btn4=Button(F2,text='Exit',font=("arial", 15, "bold"),command=exit,padx=5,pady=10,bg='yellow',width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)

#===========Bill Area=========
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text='Bill Area',font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()

root.mainloop()


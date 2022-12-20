from tkinter import*
from tkinter import messagebox,ttk
import random

root=Tk()
root.title('Movie Ticket Booking System')
root.geometry('1290x800')
bg_color='#385a7c'

city = ["Navi Mumbai", "Mumbai", "Pune", "Chennai", "Delhi"]
theater_names=["Cinepolis","INOX","PVR","Balaji Moviplex"]
Movie_names=["Avatar: The Way of Water","Spider-Man :Across the Spider-Verse","Bhediya","Mission: Impossible - Dead Reckoning","Drishyam 2","John Wick: Chapter 4","Aquaman and the Lost Kingdom","Ant-Man and the Wasp: Quantumania"]
timing=["8:30AM-11:30AM","10:00AM-12:30AM","1:00PM-3:00PM","4:00PM-6:30PM","6:00PM-8:00PM","7:30PM-9:30PM","9:00PM-11:00PM","10:00PM-12:00PM"]

dict={  'Navi  Mumbai-Cinepolis':'Screen 1',
        'Navi Mumbai-INOX':'Screen 2',
        'Navi Mumbai-PVR':'Screen 3',
        'Navi Mumbai-Balaji Moviplex':'Screen 1',
        'Mumbai-Cinepolis':'Screen 2',
        'Mumbai-INOX':'Screen 3',
        'Mumbai-PVR':'Screen 1',
        'Mumbai-Balaji Moviplex':'Screen 2',
        'Pune-Cinepolis':'Screen 3',
        'Pune-INOX':'Screen 1',
        'Pune-PVR':'Screen 2',
        'Pune-Balaji Moviplex':'Screen 3',
        'Chennai-Cinepolis':'Screen 1',
        'Chennai-INOX':'Screen 2',
        'Chennai-PVR':'Screen 3',
        'Chennai-Balaji Moviplex':'Screen 1',
        'Delhi-Cinepolis':'Screen 2',
        'Delhi-INOX':'Screen 3',
        'Delhi-PVR':'Screen 1',
        'Delhi-Balaji Moviplex':'Screen 2',
        
}
#=================variables================
person=IntVar()
c_name=StringVar()
c_phone=StringVar()
ticket_no=StringVar()
#======================================Frames=================

    
def verify():
    global dis
    a = combo_s.get()
    b = combo_d.get()
    p = person.get()
    d=a+'-'+b
    e=b+'-'+a
    if c_name.get() != "" or c_phone.get() != "":
        if c_phone.get().isnumeric() is not True:
            messagebox.showerror('Error','Phone number should be integer')
            return
    else:
        messagebox.showerror("Error", "customer details are must")
        return
    if a!=b:
        if d in dict:
            dis= dict[d]
        elif e in dict:
            dis = dict[e]
    else:
        messagebox.showwarning('Warning ','Please select right root')
        return
    messagebox.showinfo('Verified','Successfully Veirified')

def gticket():
    try:
        welcome()
        p=person.get()
        textarea.insert(END,f"\n {55*'*'}")
        textarea.insert(END,f"\n\nCity :\t\t{combo_s.get()}")
        textarea.insert(END,f"\nMovie Theatre :\t\t{combo_d.get()}")
        textarea.insert(END,f"\nNo. of Tickets: \t\t {p}")
        textarea.insert(END,f"\nScreen No. :\t\t{dis}")
        textarea.insert(END,f"\nMovie Name:\t\t{combo_m.get()}")
        textarea.insert(END,f"\nTiming: \t\t  {combo_t.get()}")
        textarea.insert(END,f"\n {55*'-'}")
        textarea.insert(END,f"\nAmount :\t\t{2*p*199}")
        textarea.insert(END,f"\n {35*'='}")
        textarea.insert(END,f"\n\n {55*'*'}")
        save_ticket()
    except Exception:
        messagebox.showwarning('Warrning','Please verify the details first')
        clear()
    

def clear():
    c_name.set('')
    c_phone.set('')
    combo_s.set('select city')
    combo_d.set('select movietheatre')
    combo_t.set('select timing')
    combo_m.set('select movienames')
    person.set(0)
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()

def save_ticket():
    op=messagebox.askyesno("Save ticket","Do you want to download ticket ?")
    if op>0:
        ticket_details=textarea.get('1.0',END)
        f1=open("bills/"+str(ticket_no.get())+".txt","w")
        f1.write(ticket_details)
        f1.close()
        messagebox.showinfo("Saved",f"Ticket no, :{ticket_no.get()} Saved Successfully")
    else:
        return
    

def welcome():
    x = random.randint(1000, 9999)
    ticket_no.set(str(x))
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\tEnjoy your Movie!")
    textarea.insert(END,f"\n\nTicket Number:\t {    ticket_no.get()}")
    textarea.insert(END,f"\nName:\t\t{c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t {c_phone.get()}")
    textarea.configure(font='arial 15 bold')

title=Label(root,pady=2,text="Movie Ticket Generator",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#=================Product Frames=================
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='#f99192',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Movie Details', font=('times new romon', 18, 'bold'), fg='#f99192',bg=bg_color)
F2.place(x=20, y=180,width=630,height=800)

source= Label(F2, text='City', font=('times new romon',18, 'bold'), bg=bg_color, fg='#b2eee6').grid(
row=0, column=0, padx=30, pady=20)
combo_s=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=city)
combo_s.grid(row=0,column=1,pady=10)
combo_s.set('select city')

des= Label(F2, text='Theatre', font=('times new romon',18, 'bold'), bg=bg_color, fg='#b2eee6').grid(
row=1, column=0, padx=30, pady=20)
combo_d=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=theater_names)
combo_d.grid(row=1,column=1,pady=10)
combo_d.set('select theatre')

mov= Label(F2, text='Movie Names', font=('times new romon',18, 'bold'), bg=bg_color, fg='#b2eee6').grid(
row=2, column=0, padx=30, pady=20)
combo_m=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=Movie_names)
combo_m.grid(row=2,column=1,pady=10)
combo_m.set('select theatre')



time= Label(F2, text='timing', font=('times new romon',18, 'bold'), bg=bg_color, fg='#b2eee6').grid(
row=3, column=0, padx=30, pady=20)
combo_t=ttk.Combobox(F2,font=('times new roman',18),state='readonly',value=timing)
combo_t.grid(row=3,column=1,pady=10)
combo_t.set('select timing')

n= Label(F2, text='Number of ticket', font=('times new romon',18, 'bold'), bg=bg_color, fg='#b2eee6').grid(
row=4, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=person, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=4, column=1, padx=10,pady=20)


#========================Ticket area================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=600,height=500)

bill_title=Label(F3,text='Ticket',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#=========================Buttons======================
btn1=Button(F2,text='Verify',font='arial 15 bold',command=verify,padx=5,pady=10,bg='#f97171',width=15)
btn1.grid(row=5,column=0,padx=10,pady=30)
btn2=Button(F2,text='Ticket',font='arial 15 bold',command=gticket,padx=5,pady=10,bg='#f97171',width=15)
btn2.grid(row=5,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='#f97171',width=15)
btn3.grid(row=6,column=0,padx=10,pady=10)
btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='#f97171',width=15)
btn4.grid(row=6,column=1,padx=10,pady=10)

root.mainloop()
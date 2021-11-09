import tkinter as tk
import time
from datetime import date
import random

root = tk.Tk()
root.geometry('500x500')

root.title("Kindle Employee service site")

name_var = tk.StringVar()
id_var = tk.StringVar()
email_var = tk.StringVar()
password_var = tk.StringVar()
dept_var = tk.StringVar()
Otp_var = tk.StringVar()

birth = {'1':'12/01/1981','2':'12/4/1979','3':'14/5/1992','4':'1/12/1979'}
Hire_date ={'1':'2001','2':'2004','3':'2012','4':'1996'}
sal={'1':'50000','2': '45000','3':'40000','4':'65000'}
dept ={'A':'Management','B':'Vice programmer','C':'coder','D':'Database Administrater'}

otp = random.randint(1000, 2000)
Check_Otp = Otp_var.get()
def In():#total 4 functions in all
    todays_date = date.today()
    year = todays_date.year
   # birth = {'1': '12/01/2001', '2': '12/4/2014','3':'14/12/2002','4':'}
   # dept ={'A':'Management','B':'Vice programmer','C':'coder','D':'Database Administrater'}
    FullName = name_var.get()
    ID = id_var.get()
    deptID = dept_var.get()
    Password = password_var.get()
    Email = email_var.get()
    a = Hire_date[ID]
    S_year = year-int(a)
    print("The name is : " + FullName)
    print("Your ID : " + ID)
    print("Your Email is : " + Email)

    label_0 = tk.Label(root, text="Verify", width=20, font=("bold", 20))#verify
    label_0.place(x=90, y=53)

    label_1 = tk.Label(root, text="Your name:", width=20, font=("bold", 13))#name
    label_1.place(x=80, y=130)

    label_1 = tk.Label(root, text=FullName, width=20, font=("bold", 13))
    label_1.place(x=240, y=130)

    label = tk.Label(root, text="Department:", width=20, font=("bold", 13))  # password
    label.place(x=68, y=180)

    label = tk.Label(root, text=dept[deptID], width=20, font=("bold", 13))
    label.place(x=240, y=180)

    label = tk.Label(root, text="ID(confirm):", width=20, font=("bold", 13))  # Employee id
    label.place(x=70, y=230)

    label = tk.Label(root, text=ID, width=20, font=("bold", 13))
    label.place(x=240, y=230)

    label_4 = tk.Label(root, text="Birth_date:", width=20, font=("bold", 13))#birth date
    label_4.place(x=70, y=280)

    label_4 = tk.Label(root, text=birth[ID], width=20, font=("bold", 13))
    label_4.place(x=240, y=280)

    label_4 = tk.Label(root, text="Service Years"
                                  ":", width=20, font=("bold", 13))  # Service year
    label_4.place(x=70, y=320)

    label_4 = tk.Label(root, text=S_year, width=20, font=("bold", 15))
    label_4.place(x=240, y=320)
    tk.Button(root, text='Back', width=20, bg='brown', fg='white', command=face).place(x=100, y=380)
    tk.Button(root, text='Forward..', width=20, bg='brown', fg='white',command=proceed).place(x=280, y=380)

    name_var.set("")



def proceed():
    todays_date = date.today()
    year = todays_date.year
  #  birth = {'1': '12/01/2001', '2': '12/4/2014', '3': '14/12/2002'}
  #  dept = {'A': 'Management', 'B': 'Vice programmer', 'C': 'coder'}
    FullName = name_var.get()
    ID = id_var.get()
    deptID = dept_var.get()
    Password = password_var.get()
    Email = email_var.get()
    a = Hire_date[ID]
    S_year = year - int(a)



    label_0 = tk.Label(root, text='''A verification code has been
     sent on your email''', width=30, font=("bold", 15))  # verify
    label_0.place(x=80, y=53)


    label_1 = tk.Label(root, text="Enter sent Otp:", width=20, font=("bold", 13))  # name
    label_1.place(x=80, y=130)

    entry_1 = tk.Entry(root, textvariable=name_var)
    Check_Otp = entry_1.place(x=240, y=130)

    label = tk.Label(root, text="Otp(sent on system):", width=20, font=("bold", 13))  # password
    label.place(x=68, y=180)

    label = tk.Label(root, text=otp, width=20, font=("bold", 10))
    label.place(x=240, y=180)

    label = tk.Label(root, text="ID(confirm):", width=20, font=("bold", 13))  # Employee id
    label.place(x=70, y=230)

    label = tk.Label(root, text=ID, width=20, font=("bold", 13))
    label.place(x=240, y=230)

    label_4 = tk.Label(root, text="Birth_date:", width=20, font=("bold", 13))  # birth date
    label_4.place(x=70, y=280)

    label_4 = tk.Label(root, text=birth[ID], width=20, font=("bold", 13))
    label_4.place(x=240, y=280)

    label_4 = tk.Label(root, text="Service Years"
                                  ":", width=20, font=("bold", 13))  # Service year
    label_4.place(x=70, y=320)

    label_4 = tk.Label(root, text=S_year, width=20, font=("bold", 15))
    label_4.place(x=240, y=320)
    tk.Button(root, text='Back', width=20, bg='brown', fg='white', command=In).place(x=100, y=380)
    tk.Button(root, text='Check_detail..', width=20, bg='brown', fg='white',command=End).place(x=280, y=380)

    name_var.set("")


def End():
    todays_date = date.today()
    year = todays_date.year
   # birth = {'1': '12/01/2001', '2': '12/4/2014', '3': '14/12/2002'}
   # dept = {'A': 'Management', 'B': 'Vice programmer', 'C': 'coder'}
    FullName = name_var.get()
    ID = id_var.get()
    deptID = dept_var.get()
    Password = password_var.get()
    Email = email_var.get()
    a = Hire_date[ID]
    S_year = year - int(a)
    b = sal[ID]
    main = int(b) + (int(b)*6/100)
    count = 0
    while count != (year - int(a)):
        b = int(b) + (int(b)*6/100)
        red = b * 0.08
        count = count + 1
        final = (year - int(a)) * (12 * red)
        total = int(final + (final * 12 / 100))

    label_0 = tk.Label(root, text='''Otp Verified!!!!
         ''', width=30, font=("bold", 15))  # verify
    label_0.place(x=80, y=53)

    label = tk.Label(root, text="Verified Otp:", width=20, font=("bold", 11))  # password
    label.place(x=80, y=130)

    label = tk.Label(root, text=otp, width=20, font=("bold", 10))
    label.place(x=240, y=130)

    label = tk.Label(root, text='''Your Starting
        salary:''', width=20, font=("bold", 13))  # password
    label.place(x=68, y=180)

    label = tk.Label(root, text=sal[ID], width=20, font=("bold", 13))
    label.place(x=240, y=180)

    label = tk.Label(root, text='''After 6% increment 
     on your salary per year''', width=20, font=("bold", 13))  # Employee id
    label.place(x=70, y=230)

    label = tk.Label(root, text=round(b), width=20, font=("bold", 13))
    label.place(x=240, y=230)

    label_4 = tk.Label(root, text='''Final PF amount 
   with 8% increment''', width=20, font=("bold", 13))  # birth date
    label_4.place(x=70, y=280)

    label_4 = tk.Label(root, text=round(total), width=20, font=("bold", 15))
    label_4.place(x=240, y=280)

    tk.Button(root, text='Home', width=20, bg='brown', fg='white', command=face).place(x=100, y=380)
    tk.Button(root, text='Exit', width=20, bg='brown', fg='white',command=exit).place(x=280, y=380)


def face():#3rd function
    label_0 = tk.Label(root, text="Registration form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = tk.Label(root, text="FullName", width=20, font=("bold", 13))
    label_1.place(x=80, y=130)

    entry_1 = tk.Entry(root, textvariable=name_var)
    FullName = entry_1.place(x=240, y=130)

    label_2 = tk.Label(root, text="Email", width=20, font=("bold", 13))
    label_2.place(x=68, y=180)

    entry_2 = tk.Entry(root, textvariable=email_var)
    Email = entry_2.place(x=240, y=180)

    label_3 = tk.Label(root, text="Gender", width=20, font=("bold", 13))
    label_3.place(x=70, y=230)
    var = tk.IntVar()
    tk.Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
    tk.Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

    label_4 = tk.Label(root, text="Employee ID:", width=20, font=("bold", 13))
    label_4.place(x=70, y=280)

    entry_4 = tk.Entry(root, textvariable=id_var)
    Age = entry_4.place(x=240, y=280)

    label_5 = tk.Label(root, text="Department ID", width=20, font=("bold", 13))
    label_5.place(x=70, y=320)

    entry_5 = tk.Entry(root, textvariable=dept_var)
    Password = entry_5.place(x=240, y=330)

    #label_5 = tk.Label(root, text="Department ID", width=20, font=("bold", 10))
    #label_5.place(x=70, y=320)



    tk.Button(root, text='verify', width=20, bg='brown', fg='white', command=In).place(x=100, y=380)
    tk.Button(root, text='Exit', width=20, bg='brown', fg='white',command=exit).place(x=280, y=380)
# it is use for display the registration form on the window

face()
root.mainloop()
print("registration form  succussfully created...")

from tkinter import * 
import time 
#----------------------------------------->connect to database
def connectdb():
    dbroot= Toplevel()
    dbroot.geometry('470x250')
    dbroot.grab_set()
    dbroot.resizable(False,False)
    dbroot.config(bg='plum1')
    #------------------------------------------>labels
    hostlabel1=Label(dbroot,text="Enter the Host",bg='OliveDrab1',font=("Times New Roman", 12, "italic"),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel1.place(x=10,y=10)
    userlabel1=Label(dbroot,text="Enter the User",bg='OliveDrab1',font=("Times New Roman", 12, "italic"),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userlabel1.place(x=10,y=70)
    passwordlabel1=Label(dbroot,text="Enter the Password",bg='OliveDrab1',font=("Times New Roman", 12, "italic"),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    passwordlabel1.place(x=10,y=130)
    #---------------------------------------------------->Entry boxes
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()
    hostentry=Entry(dbroot,width=20,borderwidth=3,font=("Times New Roman", 12, "italic"),relief=GROOVE,bd=5)
    hostentry.place(x=150,y=10)
    userentry=Entry(dbroot,width=20,borderwidth=3,font=("Times New Roman", 12, "italic"),relief=GROOVE,bd=5)
    userentry.place(x=150,y=70)
    passwordentry=Entry(dbroot,width=20,borderwidth=3,font=("Times New Roman", 12, "italic"),relief=GROOVE,bd=5)
    passwordentry.place(x=159,y=130)
    dbroot.mainloop()

def tik():
    timestring=time.strftime("%H:%M:%S")
    datestring=time.strftime("%d-%m-%y")
    clock.config(text=f"Time: {timestring}\nDate: {datestring}")
    clock.after(200,tik)
root=Tk()
root.title("Student Management")
root.configure(bg='#90ee90')
root.geometry('1174x640+200+50')
root.resizable(False,False)
#--------------------------------------------------------------------->Data entry frame
entry_frame=Frame(root,bg='seashell3',relief=GROOVE,borderwidth=5)
entry_frame.place(x=10,y=80,width=400,height=400)

showDataFrame = Frame(root,bg='seashell3',relief=GROOVE,borderwidth=5)
showDataFrame.place(x=550,y=80,width=600,height=400)
#--------------------------------------------------------------------------->slides
ss='Student Management'
slide1 = Label(root, text=ss, font=('Arial', 9), bg='seaGreen3',relief=GROOVE,borderwidth=5)
slide1.place(x=10, y=10, width=150, height=50)
clock=Label(root, font=('times', 14,'bold'), bg='azure',relief=RIDGE,borderwidth=5)
clock.place(x=1020,y=6,width=150,height=70)
tik()
connectbutton=Button(root,text="Connect to database",width=23,font=('times', 14,'bold'),relief=RIDGE,borderwidth=5,bg='gold4',activebackground='LightYellow2',command=connectdb)
connectbutton.place(x=10,y=580,width=400,height=50)
#--------------------------------------------------------------------------->submit button
submitbutton=Button(root,text="Submit",width=23,font=('times', 14,'bold'),relief=RIDGE,borderwidth=5,bg='red',activebackground='LightYellow2')
submitbutton.place(x=890,y=580)
root.mainloop()

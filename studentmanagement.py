from tkinter import * 
import time 
def tik():
    timestring=time.strftime("%H:%M:%S")
    datestring=time.strftime("%d-%m-%y")
    clock.config(text=f"Time: {timestring}\nDate: {datestring}")
    clock.after(200,tik)
root=Tk()
root.title("Student Management")
root.configure(bg='#90ee90')
root.geometry('1174x700+200+50')
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
root.mainloop()

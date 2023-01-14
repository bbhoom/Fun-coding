import tkinter
from tkinter import messagebox
from tkinter import *
top = tkinter.Tk()
def crash():
    yes.destroy()
    qu.destroy()
    next.destroy()
    top.destroy()

def yes1():
    global yes
    yes=Toplevel(top)
    yes.geometry("200x150")
    label=Label(yes, text="AW SO CUTE!",fg="red").pack()
    button=Button(yes, text="YAY,BYE!",command=crash).pack()
    yes.mainloop()
def no():
    qu.destroy()
    ques()


def ques():
    global qu
    qu=Toplevel(top)
    qu.geometry("200x150")
    label=Label(qu, text="Will u be mine?",fg="red").pack()
    button=Button(qu, text="YES",command=yes1).pack()
    button=Button(qu, text="NO" ,justify="left",command=no ).pack()
    qu.mainloop()
def next1():
    global next
    #messagebox.showwarning("BUT i just have one question for you..")
    next=Toplevel(top)
    next.geometry("300x150")
    label=Label(next, text="BUT i just have one question for you..",fg="red").pack()
    button=Button(next, text="OK", justify="right",command=ques).pack()
    next.mainloop()
#messagebox.showwarning("warning!","Your computer is HACKED!")
top.title("CAREFUL!")
top.geometry("200x150")
label=Label(top, text="Your Computer is HACKED!",fg="red").pack()
button=Button(top, text="OK", justify="right",command=next1).pack()



top.mainloop()

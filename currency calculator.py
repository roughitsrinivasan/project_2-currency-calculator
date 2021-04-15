from tkinter import *
cur=Tk()
cur.title("image to view")
ser=Entry(cur)
ser.grid(row=1,column=0,columnspan=4,ipadx=40,ipady=5,pady=10)

label_0=Label(cur,text="Currency Calaculator",fg="red")
label_0.grid(row=0)

label_1=Label(cur,text="INR")
label_1.grid(row=1,column=3)

label_2=Label(cur,text="Enter the amount :")
label_2.grid(row=1,column=0)    

def button_clear():
    ser.delete(0,END)
def usd():
    global value
    value=ser.get()
    ser.delete(0,END)
    ser.insert(0,float(value)* 75.132)
    

def euro():
    global value
    value=ser.get()
    ser.delete(0,END)
    ser.insert(0,float(value)* 89.69)
    

def yen():
    global value
    value=ser.get()
    ser.delete(0,END)
    ser.insert(0,float(value) * 0.68887)
    
def yuan():
    global value
    value=ser.get()
    ser.delete(0,END)
    ser.insert(0,float(value) * 11.4724)

button_usd=Button(cur,text="USD",padx=40,pady=20,fg="black",bg="white",command=usd)
button_euro=Button(cur,text="euro",padx=40,pady=20,fg="black",bg="white",command=euro)
button_yen=Button(cur,text="yen",padx=40,pady=20,fg="black",bg="white",command=yen)
button_yuan=Button(cur,text="yuan",padx=40,pady=20,fg="black",bg="white",command=yuan)
button_clear=Button(cur,text="clear",padx=38,pady=20,fg="black",bg="white",command=button_clear)


button_usd.grid(row=2,column=0)
button_euro.grid(row=2,column=1)
button_yen.grid(row=2,column=2)
button_yuan.grid(row=2,column=3)
button_clear.grid(row=3,column=0)

cur.mainloop()

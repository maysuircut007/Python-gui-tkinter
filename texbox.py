from tkinter import *


root = Tk() #สร้างหน้าต่างวิทเจ็ท
root.title("My GUI") #ชื่อโปรเเกรม

#กำหนดขนาดและตำแหน่งหน้าจอ
            #  กว้าง สูง แกนx แกนy
root.geometry("600x400+100+100") 


mylabel1 = Label(root,text="Hello World",fg="red",font=20,bg="yellow").pack()


def showMessang():
    messang = txt.get()
    Label(root,text=messang,font=30,bg="blue",fg="black").pack()    

#กล้องข้อความ
txt = StringVar()
mytext = Entry(root,textvariable=txt).pack()

# ใส่ปุ่ม
btn1 = Button(root,text="บันทึก",font=30,bg="green",fg="black",command=showMessang).pack()
btn2 = Button(root,text="ยกเลิก",font=30,bg="red",fg="black").pack()


root.mainloop() #ตรวจเช็คการทำงานในโปรเเกรม

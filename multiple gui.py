from tkinter import *


root = Tk() #สร้างหน้าต่างวิทเจ็ท
root.title("My GUI") #ชื่อโปรเเกรม
root.geometry("600x400+100+100") 

mylabel1 = Label(root,text="Hello World",fg="red",font=20,bg="yellow").pack()


#หน้าจอที่2
def openwindow():
    mywindow = Tk()
    mywindow.title("รายงานผล")
    mywindow.geometry("600x200")


def showMessang():
    messang = txt.get()
    Label(root,text=messang,font=30,bg="blue",fg="black").pack()    

#กล้องข้อความ
txt = StringVar()
mytext = Entry(root,textvariable=txt).pack()

# ใส่ปุ่ม
btn1 = Button(root,text="บันทึก",font=30,bg="green",fg="black",command=showMessang).pack()
btn2 = Button(root,text="เปิดรายงาย",font=30,bg="red",fg="black",command=openwindow).pack()


root.mainloop() #ตรวจเช็คการทำงานในโปรเเกรม

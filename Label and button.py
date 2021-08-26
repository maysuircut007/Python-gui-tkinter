from tkinter import *


root = Tk() #สร้างหน้าต่างวิทเจ็ท
root.title("My GUI") #ชื่อโปรเเกรม

#กำหนดขนาดและตำแหน่งหน้าจอ
            #  กว้าง สูง แกนx แกนy
root.geometry("600x400+100+100") 

#ใส่ข้อความไปที่หน้าจอ 
      #.pack() => เเสดงกลางหน้าจอ
      #.place(x=70,y=10) => แกนx แกนy
      #.grid(row=0,column=1)
mylabel1 = Label(root,text="Hello World",fg="red",font=20,bg="yellow").place(x=130,y=0)


def showMessang():
    mylabel2 = Label(root,text="Maysa Kumnerdde",font=30,bg="blue",fg="black").pack()
    return mylabel2
# ใส่ปุ่ม
btn1 = Button(root,text="บันทึก",font=30,bg="blue",fg="black",command=showMessang).place(x=90,y=30)



root.mainloop() #ตรวจเช็คการทำงานในโปรเเกรม

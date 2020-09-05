# 使用 Tkinter 创建一个 Windows 窗口 GUI 程序示例
from tkinter import *                         # 导入 Tkinter 模块

def callback_borrow():
    br = Toplevel()
    br.title("借用人信息")
    br.geometry("330x150")

    label = Label(br,text="请填写借用人信息！")
    label.pack()

    name_label = Label(br, text="借用人名字",width=15).place(x=3,y=50)
    name_text = Entry(br, width=20).place(x=100,y=50)

    time_label = Label(br, text="借用时间（格式：年-月-日)",width=27).place(x=3,y=70)
    time_text = Entry(br, width=20).place(x=180,y=70)

    button = Button(br, text="确定", command="")
    button.pack(anchor="center")
    button.place(x=150,y=100)

def callback_return():
    re = Toplevel()
    re.title("还用人信息")
    re.geometry("330x150")

    label = Label(re, text="请填写还用人信息！")
    label.pack()

    name_label = Label(re, text="还用人名字", width=15).place(x=3, y=50)
    name_text = Entry(re, width=20).place(x=100, y=50)

    time_label = Label(re, text="还用时间（格式：年-月-日)",width=27).place(x=3,y=70)
    time_text = Entry(re, width=20).place(x=180, y=70)

    button = Button(re, text="确定", command="")
    button.pack(anchor="center")
    button.place(x=150, y=100)

def quit_program():
    win.destroy()
    exit()

# main
win = Tk()                      # 创建 Windows 窗口对象
win.title("借用系统")                    # 设置窗口标题
win.geometry("400x180")

label = Label(win, text = "欢迎使用借用系统！")
label.pack()

button_borrow = Button(win, text = "借", command = callback_borrow)
button_borrow.pack(side = "left", ipadx = "1c", padx = "1c")

button_return = Button(win, text = "还", command = callback_return)
button_return.pack(side = "right", ipadx = "1c", padx = "1c")

button_end = Button(win, text = "结束", command=quit_program,width=15,height=1)
button_end.pack()
button_end.place(x=145,y=140)
win.mainloop()                          # 进入消息循环，显示窗口


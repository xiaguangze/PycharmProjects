import tkinter
import time
import threading
import random

root = tkinter.Tk()

root.title("元旦晚会抽奖活动")
root.geometry("960x540+300+100")
root.resizable(width=False, height=False)
number = []
root.flag = True


def update():
    if entry.get() != '':
        number.append(entry.get())
        text.delete(0.0, tkinter.END)
        text.insert(tkinter.INSERT, number)
        entry.delete(0, tkinter.END)


def pop():
    if entry.get() in number:
        number.remove(entry.get())
        text.delete(0.0, tkinter.END)
        text.insert(tkinter.INSERT, number)
        entry.delete(0, tkinter.END)


def main():
    root.flag = True
    while root.flag:
        i = random.randint(0, len(number)-1)
        label1['text'] = label4['text']
        label4['text'] = label7['text']
        label7['text'] = label8['text']
        label8['text'] = label9['text']
        label9['text'] = label6['text']
        label6['text'] = label3['text']
        label3['text'] = label2['text']
        label2['text'] = label5['text']
        label5['text'] = number[i]
        time.sleep(0.01)


def startmain():
    start.place(x=470, y=90)
    stop.place(x=610, y=90)
    print(number)


def startbutton():
    t = threading.Thread(target=main)
    t.start()


def stopbutton():
    root.flag = False


labeltitle = tkinter.Label(root,
                           text="欢迎来到元旦晚会抽奖活动",
                           bg="#f0a1a8",
                           font=("楷体", 35)
                           )

insertbutton = tkinter.Button(root,
                              text="添加",
                              width=10,
                              command=update,
                              )

popbutton = tkinter.Button(root,
                           text="删除",
                           width=10,
                           command=pop,
                           )

# content = tkinter.StringVar()    textvariable=content
entry = tkinter.Entry(root, font=("宋体", 20), )

text = tkinter.Text(root, font=("宋体", 10),)

numberstopbutton = tkinter.Button(root,
                                  text="人员添加完毕",
                                  width=16,
                                  command=startmain,
                                  )

start = tkinter.Button(root, width=14, text="开始", command=startbutton)
stop = tkinter.Button(root, width=14, text="结束", command=stopbutton)

label1 = tkinter.Label(root, text='', font=("宋体", 15))
label1.place(x=380, y=150, width=150, height=100)

label2 = tkinter.Label(root, text='', font=("宋体", 15))
label2.place(x=380, y=250, width=150, height=100)

label3 = tkinter.Label(root, text='', font=("宋体", 15))
label3.place(x=380, y=350, width=150, height=100)

label4 = tkinter.Label(root, text='', font=("宋体", 15))
label4.place(x=530, y=150, width=150, height=100)

label5 = tkinter.Label(root, text='', font=("宋体", 15))
label5['fg'] = 'red'
label5.place(x=530, y=250, width=150, height=100)

label6 = tkinter.Label(root, text='', font=("宋体", 15))
label6.place(x=530, y=350, width=150, height=100)

label7 = tkinter.Label(root, text='', font=("宋体", 15))
label7.place(x=680, y=150, width=150, height=100)

label8 = tkinter.Label(root, text='', font=("宋体", 15))
label8.place(x=680, y=250, width=150, height=100)

label9 = tkinter.Label(root, text='', font=("宋体", 15))
label9.place(x=680, y=350, width=150, height=100)

labeltitle.pack(fill=tkinter.X, side=tkinter.TOP)
insertbutton.place(x=170, y=70)
popbutton.place(x=170, y=110)
entry.place(x=40, y=90, width=120, height=40)
text.place(x=40, y=170, width=240, height=300)
numberstopbutton.place(x=84, y=480)


root.mainloop()

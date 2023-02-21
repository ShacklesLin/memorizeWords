'''
变量=StringVar()，这样可以定义一个文本变量。变量.get()可以获取这个变量的文本值(注意在使用值时记得用这个方法)，变量.set('文本内容')可以设置这个变量的文本内容。Label(root,textvariable=变量)可以这样把变量放进去显示文本，如果这个变量发生变化，那么控件里使用了这个文本变量的内容显示也会跟着发生改变

python中列表中的元素可以是任意类型的数据，例如下面所示
word1=StringVar()
word2=StringVar()
list=[word1,word2]

在表达式里面声明变量需要把=换成:=，例如下所示
list=[word1:=StringVar(),word2:=StringVar(),word3:=StringVar(),word4:=StringVar(),word5:=StringVar(),word6:=StringVar(),word7:=StringVar(),word8:=StringVar(),word9:=StringVar(),word10:=StringVar()]

for index in range(0,10):#这里的(0,10)表示0,1,2,3,4,5,6,7,8,9。也可以把(0,10)换成(10)
    Label(root,textvariable=list[index],fg='blue',font=('楷体',12,'bold')).grid(row =index,column=1)
    list[index].set(index)

在python中批量生成变量的方法如下
for i in range(3):
    locals() ['x' + str(i)] = i

以下代码注意想要在流程控制语句中使用列表的.append()方法要注意在这个流程控制语句外面先声明这个列表。locals()方法只能作为单独一条语句进行声明变量，不能在其他方法内声明变量
list=[]
for index in range(10):
    locals()['word'+str(index)]=StringVar()
    list.append(locals()['word'+str(index)])

sss=words.readlines()#这个列表里面的每一个元素的末尾都是\n有时候会影响到赋值，所以需要去掉\n，可以用.rstrip('\n')去掉\n

Entry(root,textvariable=inputValue).grid(row =9,column=1)#部署一个输入框，同时inputValue与输入框内容绑定，也就是可以通过inputValue来获取该输入框的值

以下描述了如何使用消息对话框
import tkinter.messagebox
result=tkinter.messagebox.askokcancel ("提示"," 你确定要关闭窗口吗? ")

想用button绑定一个事件，必须先定义一个方法，然后把这个方法绑定到这个button如下所示
def callback():
    print ("click me!")
b = tk.Button(window, text="点击执行回调函数", command=callback).pack()
'''

#导入库
from tkinter import *
import tkinter.messagebox
#初始化窗口root
root = Tk()
#设置窗口root的标题
root.title('word记忆工具')
#声明输入框‘更新’的文本变量
inputValue=StringVar()
Entry(root,textvariable=inputValue).grid(row =9,column=1)
#

    
def callback():
    tkinter.messagebox.showinfo("测试", inputValue.get())

list=[]

words=open("words.txt", mode='r',encoding='utf-8')
sss=words.readlines()
for index in range(10):
    locals()['word'+str(index)]=StringVar()
    list.append(locals()['word'+str(index)])
    list[index].set(sss[index].rstrip('\n'))
    Label(root,textvariable=list[index],fg='blue',font=('楷体',12,'bold')).grid(row =index,column=2)
words.close()
def updateTxt():
    f=open('words.txt', "r+",encoding='utf-8')
    f.truncate()
    for index in range(10):
        f.write(list[index].get()+'\n')
    f.close()
    
def drop(index):
    temp=list[index].get()
    for index in range(index,9):
        list[index].set(list[index+1].get())
    list[9].set(temp)
    updateTxt()
def b0():
    drop(0)
def b1():
    drop(1)
def b2():
    drop(2)
def b3():
    drop(3)
def b4():
    drop(4)
def b5():
    drop(5)
def b6():
    drop(6)
def b7():
    drop(7)
def b8():
    drop(8)

def update1():
    for index in range(9):
        list[index].set(list[index+1].get())
    list[9].set(inputValue.get())
    inputValue.set('')
    updateTxt()
for index in range(9):
    Button(root,width=10,height=1,text="置底",command=locals()['b'+str(index)]).grid(row=index,column=0)
Button(root,width=10,height=1,text="更新",command=update1).grid(row=9,column=0)






root.mainloop()

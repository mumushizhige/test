# -*- encoding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from readfile import filecls

def print123():	
	url = str(readfile_entry.get()) 
	print(url)
	input_entry.delete('1.0',END)
	try:
		contests = filecls.readfilerobot(url)
		for contest in contests:
			ncontest = contest
			print(ncontest)
			input_entry.insert(INSERT,ncontest)
	except Exception:
		showinfo('提示',"请输入正确的文件路径和文件名\n"+"可能输入的文件路径带有特殊字符或空格回车等")
	
def inputyuansu():
	listtext = []
	listtext1 = []
	list_text = input_entry.get("0.0",END).split("\n")
	for ltexts in list_text:
		listtext1.append(ltexts+"\n")
		
	filecls.writefilerobot(listtext1)
	
	showinfo('提示',"元素层文本已生成，请到该运行文件下查找")
	
def inputyemian():
	listtext = []
	listtext1 = []	
	list_text = input_entry.get("0.0",END).split("\n")
	for ltexts in list_text:
		listtext1.append(ltexts+"\n")
	filecls.writeymfilerobot(listtext1)
	
	showinfo('提示',"页面层文本已生成，请到该运行文件下查找")

def helpinfo():
	showinfo("帮助","例如\n"+"*** Settings ***\n"+"\n"+"*** Test Cases ***\n"+"登录系统\n"+"\t##打开浏览器,${url},/\n"+"\topen browser\t${url}\tchrome\t##输入账号,${zhanghao},/\n"+"\tinput text\txpath=//input[contains(@id,'username')]\t${zhanghao}\n"+"\tinput text\txpath=//input[contains(@id,'password')]\t${mima}\n"+"\n"+"转换成\n"+"*** Settings ***\n"+"\n"+"*** KeyWords ***\n"+"登录系统\n"+"打开浏览器\n"+"\t[Arguments]\t${url}	\n"+"\topen browser\t${url}\tchrome\n"+"输入账号\n"+"\t[Arguments]\t${zhanghao}\n"+"\tinput text\txpath=//input[contains(@id,'username')]\t${zhanghao}\n"+"\tinput text\txpath=//input[contains(@id,'password')]\t${mima}\n")

#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('robotframework用例转关键字')
#设置窗口大小
#width = 380
#height = 300
width = 720
height = 600
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
myWindow.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)


Label(myWindow,text="请输入robotframework的用例文件名").grid(row=0,column=0)
readfile_entry = Entry(myWindow)
readfile_entry.grid(row=0,column=2)
input_entry = Text(myWindow,width=80,height=40)
input_entry.place(x=30,y=30)
Button(myWindow,text="读取",command=print123).grid(row=0,column=5)

Button(myWindow,text="获取元素层文本",command=inputyuansu).grid(row=0,column=6)
Button(myWindow,text="获取页面层文本",command=inputyemian).grid(row=0,column=7)
Button(myWindow,text="帮助说明",command=helpinfo).grid(row=0,column=8)

#进入消息循环
myWindow.mainloop()


	
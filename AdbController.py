# -*- coding: utf-8 -*-
import os
#from tkinter import * 
import tkinter as tk
from tkinter import messagebox

#pyinstaller -F  .\AdbController.py， 将生成exe文件
#tkinter 打包成exe可执行文件
#https://www.jianshu.com/p/bf592bd0a034


print("窗口启动...")

root = tk.Tk()
root.geometry("180x260")
iptextvar = tk.Variable() 
iptextvar.set('172.16.13.106')

resptextvar=tk.Variable()
resptextvar.set('...')

isConnected = False

def exeCmdKey(key):
    if  isConnected!=True:
        resptextvar.set('未链接!')
        return
    cmdl = ['adb shell input keyevent ', key]
    cmdStr = ''.join(cmdl)
    print(cmdStr)
    rt = os.popen(cmdStr).read()
    print(rt)
    resptextvar.set('命令已发送!')
    
def exeCmd(cmdStr):
    if  isConnected!=True:
        resptextvar.set('未链接!')
        return
    print(cmdStr)
    rt = os.popen(cmdStr).read()
    print(rt)
    resptextvar.set('命令已发送!')
    
def exeAction(action):
    if  isConnected!=True:
        resptextvar.set('未链接!')
        return
    cmdl = ['adb shell am start -a ', action]
    cmdStr = ''.join(cmdl)
    print(cmdStr)
    rt = os.popen(cmdStr).read()
    print(rt)
    resptextvar.set('命令已发送!')
    
def execConnect():
    cmdl = ['adb connect ', iptextvar.get()]
    cmdStr = ''.join(cmdl)
    print(cmdStr)
    rt = os.popen(cmdStr).read()
    print(rt)
    
    global isConnected
    if rt.startswith('connected') or rt.startswith('already connected'):
        resptextvar.set('已链接成功!')
        isConnected=True
        connect['fg']='green'
    else:
        resptextvar.set('执行异常!')
        isConnected=False
        connect['fg']='black'

def execDisConnect():
    global isConnected
    print(isConnected)
    if  isConnected!=True:
        resptextvar.set('未链接!')
        return
   
    rt = os.popen('adb disconnect').read()
    print(rt)
    if rt.startswith('disconnected'):
        resptextvar.set('已断开!')
    else:
        resptextvar.set('执行异常!')
   
    isConnected=False
    connect['fg']='black'

def execRebootCmd():
    if  isConnected!=True:
        resptextvar.set('未链接!')
        return
    cmdStr='adb reboot'
    print(cmdStr)
    resptextvar.set('正在重启...')
    os.popen(cmdStr).read()


header= tk.Frame(root)
home=tk.Button(header, text ="首页", command =lambda:exeCmdKey('3'))
home.pack(side='left')
menu=tk.Button(header, text ="菜单", command = lambda:exeCmdKey('1'))
menu.pack(side='left')
setting=tk.Button(header, text ="设置", command =lambda:exeAction('bestv.ott.action.setting.sys'))
setting.pack(side='left')
back=tk.Button(header, text ="返回", font='bold', fg='orange',command =lambda: exeCmdKey('4'))
back.pack(side='left')
header.pack(side='top')


grid= tk.Frame(root)
up=tk.Button(grid, text ="上",font='bold',  width=5, command = lambda:exeCmdKey('19'))
up.grid(row=1, column=1)
left=tk.Button(grid, text ="左",font='bold', width=5 ,command = lambda:exeCmdKey('21'))
left.grid(row=2, column=0)
ok=tk.Button(grid, text ="OK", font='bold',  width=5,bg='orange', fg='white',command = lambda:exeCmdKey('23'))
ok.grid(row=2, column=1)
right=tk.Button(grid, text ="右",font='bold', width=5, command = lambda:exeCmdKey('22'))
right.grid(row=2, column=2)
down=tk.Button(grid, text ="下",font='bold', width=5, command = lambda:exeCmdKey('20'))
down.grid(row=3, column=1)
grid.pack(side='top')

addr= tk.Frame(root)
ip = tk.Label(addr,text = "地址:")
ip.pack(side='left')
inputip=tk.Entry(addr,textvariable=iptextvar,width=15)
inputip.pack(side='left')
connect = tk.Button(addr,text="连接",command=lambda:execConnect())
connect.pack(side='left')
addr.pack(side='top')

funs=tk.Frame(root)
disconnect = tk.Button(funs,text="断开",command=lambda:execDisConnect())
disconnect.pack(side='right')
reboot=tk.Button(funs, text ="重启", command = lambda:execRebootCmd())
reboot.pack(side='right')
funs.pack(side='top')

more=tk.Frame(root)
zhibo=tk.Button(more, text ="直播", command =lambda:exeAction('bestv.ott.action.web --es param SERVICE_H5JINGXUAN'))
zhibo.grid(row=0, column=0)
dianbo=tk.Button(more, text ="点播", command = lambda:exeAction('bestv.ott.action.categories'))
dianbo.grid(row=0, column=1)
yingyong=tk.Button(more, text ="应用", command =lambda: exeAction('bestv.ott.action.appstore'))
yingyong.grid(row=0, column=2)
favor=tk.Button(more, text ="收藏", command =lambda: exeAction('bestv.ott.action.favorite'))
favor.grid(row=0, column=3)
more.pack(side='top')

volumn=tk.Frame(root)
mute=tk.Button(volumn, text ="mute", command =lambda:exeCmdKey('164'))
mute.pack(side='left')
zhibo=tk.Button(volumn, text ="vol+", command =lambda:exeCmdKey('24'))
zhibo.pack(side='left')
dianbo=tk.Button(volumn, text ="vol-", command = lambda:exeCmdKey('25'))
dianbo.pack(side='left')
volumn.pack(side='top')


alertinfo=tk.Frame(root)
informtext=ip = tk.Label(alertinfo,textvariable=resptextvar,fg='gray')
informtext.pack(side='left')
alertinfo.pack(side='top')


root.mainloop()# 进入消息循环

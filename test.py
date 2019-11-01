#coding:utf-8  
#!/usr/bin/env python  
import wx                               #导入wx包  
app = wx.App()                          #创建应用程序对象  
win = wx.Frame(None,-1,'install test', size=(600, 400),pos=(400, 300))  #创建窗体
btn = wx.Button(win, label = 'Hello World!')  #创建Button  
win.Show()                              #显示窗体  
app.MainLoop()                          #运行程序  



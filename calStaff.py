# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:24:35 2020

@author:   
"""


import wx
import calStaffGUI
import pandas as pd
from pandas.api.types import is_string_dtype
from datetime import date
import numpy as np

  
class calStaff(calStaffGUI.calStaff):
	def __init__(self,parent):
		calStaffGUI.calStaff.__init__(self,parent)  


#退出按钮
	def onExit( self, event ):
		frame.Destroy()
        
	def onCal( self, event ):
		path = self.m_filePicker.GetPath()
		data = pd.read_excel(path)
        #身份证号标志列名    
		ids = ['身份证号', '身份证', 'id', 'ID']
		#得到列名    
		i_d = []    
		i_d = [i for i in ids if i in data.columns]
		if len(i_d) == 0:
		    show_info = "列中没有身份证号，或是列名不是'身份证号', '身份证', 'id', 'ID'中的一个，\
请修改Excel列名。"
		    dlg = wx.MessageDialog(None, show_info , u"列名异常", wx.OK | wx.ICON_INFORMATION)
		    if dlg.ShowModal() == wx.ID_YES:
		        pass

		elif len(i_d) == 1:
		    i_d = i_d[0]
		else:
		  show_info = "列中有多个表示身份证号的列，请修正原文件列名"
		  dlg = wx.MessageDialog(None, show_info , u"列名异常", wx.OK | wx.ICON_INFORMATION)
		  if dlg.ShowModal() == wx.ID_YES:
		      frame.Show(True)

		#总人数
		total = len(data)
        #当前年份
		thisYear = date.today().year
        #如果身份证列是数字，转化为字符
		if is_string_dtype(data[i_d]) == False:
		  data[i_d]=data[i_d].astype('str')
        #出生年代
		bornYear = data[i_d].str[6:10].astype(int)
        #各年年龄
		data['age'] = thisYear - bornYear
        #平均年龄
		meanAge = data['age'].mean()
        
        #性别代码
		data['sexCode'] = data[i_d].str[-2].astype(int)
        #性别填充
		data['sex']=np.where((data['sexCode']%2) == 0,'女','男')
        #性别分组
		group = data['sex'].groupby(data['sex'])
        #性别统计
		sexCount = group.count()
        #性别0 女
		sex0 = sexCount.index[0]
		sex0c = sexCount[0]
		sex0p = sex0c / total * 100 #百分比
        #性别1 男
		sex1 = sexCount.index[1]
		sex1c = sexCount[1]
		sex1p = sex1c / total * 100 #百分比
        #年龄按性别分组
		groupAge = data['age'].groupby(data['sex'])
		meanAgeBySex = groupAge.mean()
		sex0Age = meanAgeBySex[0] #女
		sex1Age = meanAgeBySex[1] #男
		show_info = '本部门共{0}人，其中{1}性{2}人,占{3:.0f}%，平均年龄{4:.0f}岁；\
{5}性{6}人，占{7:.0f}%，平均年龄{8:.0f}岁，所有人平均年龄{9:.0f}岁。'.format(total, sex0, sex0c, sex0p, sex0Age,\
		sex1, sex1c, sex1p, sex1Age, meanAge)
		dlg = wx.MessageDialog(None, show_info , u"统计结果", wx.OK | wx.ICON_INFORMATION)
		if dlg.ShowModal() == wx.ID_YES:
		  frame.Show(True)
		dlg.Destroy()
		
      
app = wx.App(False)
frame = calStaff(None)
frame.Show(True)
#start the applications
app.MainLoop()

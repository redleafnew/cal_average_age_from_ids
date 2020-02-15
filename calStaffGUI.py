# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class calStaff
###########################################################################

class calStaff ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"部门平均年龄计算程序", pos = wx.DefaultPosition, size = wx.Size( 500,70 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer1.SetMinSize( wx.Size( -1,40 ) )
		fileBrowser = wx.BoxSizer( wx.HORIZONTAL )

		fileBrowser.SetMinSize( wx.Size( -1,40 ) )

		fileBrowser.Add( ( 5, 10), 0, wx.EXPAND, 5 )

		self.m_filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"请选择文件...", u"Excel 2007-2019 (*.xlsx)|*.xlsx|Excel 2003 (*.xls)|*.xls|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fileBrowser.Add( self.m_filePicker, 6, wx.ALL|wx.EXPAND, 5 )


		fileBrowser.Add( ( 5, 0), 0, wx.EXPAND, 5 )

		self.m_cal = wx.Button( self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		fileBrowser.Add( self.m_cal, 1, wx.ALL, 5 )

		self.m_exit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		fileBrowser.Add( self.m_exit, 0, wx.ALL, 5 )


		fgSizer1.Add( fileBrowser, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_cal.Bind( wx.EVT_BUTTON, self.onCal )
		self.m_exit.Bind( wx.EVT_BUTTON, self.onExit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onCal( self, event ):
		event.Skip()

	def onExit( self, event ):
		event.Skip()



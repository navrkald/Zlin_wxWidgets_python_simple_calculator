# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"KMPP Calculator by David Navkal", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,300 ), wx.Size( 500,300 ) )
		self.SetBackgroundColour( wx.Colour( 48, 214, 16 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 5, 0, 0 )
		
		self.m_but1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but1, 0, wx.ALL, 5 )
		
		self.m_but2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but2, 0, wx.ALL, 5 )
		
		self.m_but3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but3, 0, wx.ALL, 5 )
		
		self.m_but_plus = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_plus, 0, wx.ALL, 5 )
		
		self.m_but_decimal_point = wx.Button( self, wx.ID_ANY, u",", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_decimal_point, 0, wx.ALL, 5 )
		
		self.m_but4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but4, 0, wx.ALL, 5 )
		
		self.m_but5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but5, 0, wx.ALL, 5 )
		
		self.m_but6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but6, 0, wx.ALL, 5 )
		
		self.m_but_minus = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_minus, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"BCK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_but7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but7, 0, wx.ALL, 5 )
		
		self.m_but8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but8, 0, wx.ALL, 5 )
		
		self.m_but9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but9, 0, wx.ALL, 5 )
		
		self.m_but_multiplication = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_multiplication, 0, wx.ALL, 5 )
		
		self.m_but_clear = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_clear, 0, wx.ALL, 5 )
		
		self.m_but0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but0, 0, wx.ALL, 5 )
		
		self.m_but_left_backet = wx.Button( self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_left_backet, 0, wx.ALL, 5 )
		
		self.m_but_right_bracket = wx.Button( self, wx.ID_ANY, u")", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_right_bracket, 0, wx.ALL, 5 )
		
		self.m_but_division = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_division, 0, wx.ALL, 5 )
		
		self.m_but_solve = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_but_solve, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrl.Bind( wx.EVT_TEXT, self.m_textCtrlOnText )
		self.m_but1.Bind( wx.EVT_BUTTON, self.OnOneClick )
		self.m_but2.Bind( wx.EVT_BUTTON, self.OnTwoClick )
		self.m_but3.Bind( wx.EVT_BUTTON, self.OnThreeClick )
		self.m_but_plus.Bind( wx.EVT_BUTTON, self.OnPlusClick )
		self.m_but_decimal_point.Bind( wx.EVT_BUTTON, self.OnDecimalPointClick )
		self.m_but4.Bind( wx.EVT_BUTTON, self.OnFourClick )
		self.m_but5.Bind( wx.EVT_BUTTON, self.OnFiveClick )
		self.m_but6.Bind( wx.EVT_BUTTON, self.OnSixClick )
		self.m_but_minus.Bind( wx.EVT_BUTTON, self.OnMinusClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnBackClick )
		self.m_but7.Bind( wx.EVT_BUTTON, self.OnSevenClick )
		self.m_but8.Bind( wx.EVT_BUTTON, self.OnEightClick )
		self.m_but9.Bind( wx.EVT_BUTTON, self.OnNineClick )
		self.m_but_multiplication.Bind( wx.EVT_BUTTON, self.OnMultiplicateClick )
		self.m_but_clear.Bind( wx.EVT_BUTTON, self.OnClearClick )
		self.m_but0.Bind( wx.EVT_BUTTON, self.OnZeroClick )
		self.m_but_left_backet.Bind( wx.EVT_BUTTON, self.OnLeftBracketClick )
		self.m_but_right_bracket.Bind( wx.EVT_BUTTON, self.OnRighBracketClick )
		self.m_but_division.Bind( wx.EVT_BUTTON, self.OnDivideClick )
		self.m_but_solve.Bind( wx.EVT_BUTTON, self.OnSolveClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_textCtrlOnText( self, event ):
		event.Skip()
	
	def OnOneClick( self, event ):
		event.Skip()
	
	def OnTwoClick( self, event ):
		event.Skip()
	
	def OnThreeClick( self, event ):
		event.Skip()
	
	def OnPlusClick( self, event ):
		event.Skip()
	
	def OnDecimalPointClick( self, event ):
		event.Skip()
	
	def OnFourClick( self, event ):
		event.Skip()
	
	def OnFiveClick( self, event ):
		event.Skip()
	
	def OnSixClick( self, event ):
		event.Skip()
	
	def OnMinusClick( self, event ):
		event.Skip()
	
	def OnBackClick( self, event ):
		event.Skip()
	
	def OnSevenClick( self, event ):
		event.Skip()
	
	def OnEightClick( self, event ):
		event.Skip()
	
	def OnNineClick( self, event ):
		event.Skip()
	
	def OnMultiplicateClick( self, event ):
		event.Skip()
	
	def OnClearClick( self, event ):
		event.Skip()
	
	def OnZeroClick( self, event ):
		event.Skip()
	
	def OnLeftBracketClick( self, event ):
		event.Skip()
	
	def OnRighBracketClick( self, event ):
		event.Skip()
	
	def OnDivideClick( self, event ):
		event.Skip()
	
	def OnSolveClick( self, event ):
		event.Skip()
	


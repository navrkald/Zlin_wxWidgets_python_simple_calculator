#!/usr/env python
# -*- coding: utf-8 -*- 

'''
Created on 31.1.2015

@author: David Navrkal
'''

import wx
import gui
import locale

class MainFrame(gui.MainWindow):
    def OnCloseDialog( self, event ):
        self.Destroy()

    def __init__ (self, parent):
        gui.MainWindow.__init__(self, parent)
        self.m_textCtrl.SetEditable(False)
        # Get decimal point based on locale
        locale.setlocale(locale.LC_ALL, '')
        self.dec_pont = locale.localeconv()['decimal_point']
        self.m_but_decimal_point.Label = self.dec_pont

    def OnClose( self, event ):
        self.Destroy()
    
    def OnZeroClick(self, event):
        self.m_textCtrl.AppendText("0") 
            
    def OnOneClick(self, event):
        self.m_textCtrl.AppendText("1")
        
    def OnTwoClick(self, event):
        self.m_textCtrl.AppendText("2")
        
    def OnThreeClick(self, event):
        self.m_textCtrl.AppendText("3")
        
    def OnFourClick(self, event):
        self.m_textCtrl.AppendText("4")
        
    def OnFiveClick(self, event):
        self.m_textCtrl.AppendText("5")
        
    def OnSixClick(self, event):
        self.m_textCtrl.AppendText("6")
        
    def OnSevenClick(self, event):
        self.m_textCtrl.AppendText("7")
        
    def OnEightClick(self, event):
        self.m_textCtrl.AppendText("8")
        
    def OnNineClick(self, event): 
        self.m_textCtrl.AppendText("9")         
    
    def OnPlusClick(self, event): 
        self.m_textCtrl.AppendText("+")    
        
    def OnMinusClick(self, event): 
        self.m_textCtrl.AppendText("-")    
        
    def OnMultiplicateClick(self, event): 
        self.m_textCtrl.AppendText("*")    
        
    def OnDivideClick(self, event): 
        self.m_textCtrl.AppendText("/")
        
    def OnLeftBracketClick(self, event):
        self.m_textCtrl.AppendText("(")  

    def OnRighBracketClick(self, event):
        self.m_textCtrl.AppendText(")")
        
    def OnDecimalPointClick(self, event):
        self.m_textCtrl.AppendText(self.dec_pont)
        
    def OnClearClick(self,event):
        self.m_textCtrl.SetValue("")
    
    def OnBackClick(self,event):
        self.m_textCtrl.SetValue(self.m_textCtrl.GetValue()[:-1])
    
    def OnSolveClick(self, event): 
        try:
            # handle decimal point
            text = str(self.m_textCtrl.GetValue());
            text = text.replace(",", ".")
            text = str(eval(text))
            text = text.replace(".", self.dec_pont)
            self.m_textCtrl.SetValue(text)
        except ZeroDivisionError:
            # Catch division by zero
            wx.MessageBox('Division by zero!', 'Alert', wx.ICON_EXCLAMATION | wx.STAY_ON_TOP)
    
    def m_textCtrlOnText(self, event):
        self.ResultValidate()
    
    # Check result and hide/show solution button
    def ResultValidate(self):
        try:
            text = str(self.m_textCtrl.GetValue());
            text.replace(",", ".")
            eval(text)
        except SyntaxError:
            self.m_but_solve.Disable()
        except ZeroDivisionError:
            self.m_but_solve.Enable()
        else:
            self.m_but_solve.Enable()
            
if __name__ == '__main__':
    app = wx.App(0)
    app.SetTopWindow( MainFrame(parent = None) )
    app.GetTopWindow().Show()
    app.MainLoop()
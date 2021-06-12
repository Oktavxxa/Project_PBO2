# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 184, 214, 241 ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText141 = wx.StaticText( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		bSizer11.Add( self.m_staticText141, 0, wx.ALL, 5 )
		
		self.m_bitmap5 = wx.StaticBitmap( self.m_panel9, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_bitmap5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 11, 74, 90, 90, False, "Century Gothic" ) )
		
		bSizer11.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel9.SetSizer( bSizer11 )
		self.m_panel9.Layout()
		bSizer11.Fit( self.m_panel9 )
		bSizer5.Add( self.m_panel9, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Nama = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.Nama, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Username = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.Username, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Password = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer2.Add( self.Password, 0, wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( gSizer2 )
		self.m_panel7.Layout()
		gSizer2.Fit( self.m_panel7 )
		bSizer5.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer7.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.regis = wx.Button( self.m_panel8, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.regis.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer7.Add( self.regis, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer7 )
		self.m_panel8.Layout()
		bSizer7.Fit( self.m_panel8 )
		bSizer5.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.regis.Bind( wx.EVT_BUTTON, self.regisOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def regisOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 184, 214, 241 ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer13.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_bitmap4 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_bitmap4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 11, 74, 90, 90, False, "Century Gothic" ) )
		
		bSizer13.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel10.SetSizer( bSizer13 )
		self.m_panel10.Layout()
		bSizer13.Fit( self.m_panel10 )
		bSizer12.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer3.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.inputUname = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.inputUname, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gSizer3.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.inputPass = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer3.Add( self.inputPass, 0, wx.ALL, 5 )
		
		
		self.m_panel11.SetSizer( gSizer3 )
		self.m_panel11.Layout()
		gSizer3.Fit( self.m_panel11 )
		bSizer12.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText161 = wx.StaticText( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer14.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		self.login = wx.Button( self.m_panel12, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer14.Add( self.login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText171 = wx.StaticText( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		bSizer14.Add( self.m_staticText171, 0, wx.ALL, 5 )
		
		
		self.m_panel12.SetSizer( bSizer14 )
		self.m_panel12.Layout()
		bSizer14.Fit( self.m_panel12 )
		bSizer12.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.loginOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loginOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Selamat Datang !", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 184, 214, 241 ) )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self.m_panel14, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_bitmap3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Aplikasi Penjadwalan Agenda Mahasiswa ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( 11, 74, 90, 92, False, "Century Gothic" ) )
		
		bSizer16.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel14.SetSizer( bSizer16 )
		self.m_panel14.Layout()
		bSizer16.Fit( self.m_panel14 )
		bSizer15.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText27 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Ingin mendaftar?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		self.m_staticText27.SetFont( wx.Font( 10, 74, 90, 90, False, "Century Gothic" ) )
		
		bSizer17.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.regis1 = wx.Button( self.m_panel15, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.regis1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer17.Add( self.regis1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel15.SetSizer( bSizer17 )
		self.m_panel15.Layout()
		bSizer17.Fit( self.m_panel15 )
		bSizer15.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText28 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Sudah mendaftar?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		self.m_staticText28.SetFont( wx.Font( 10, 74, 90, 90, False, "Century Gothic" ) )
		
		bSizer18.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.login1 = wx.Button( self.m_panel16, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.login1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer18.Add( self.login1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel16.SetSizer( bSizer18 )
		self.m_panel16.Layout()
		bSizer18.Fit( self.m_panel16 )
		bSizer15.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.regis1.Bind( wx.EVT_BUTTON, self.regis1OnButtonClick )
		self.login1.Bind( wx.EVT_BUTTON, self.login1OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def regis1OnButtonClick( self, event ):
		event.Skip()
	
	def login1OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Beranda", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 184, 214, 241 ) )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( 11, 74, 90, 90, False, "Century Gothic" ) )
		
		bSizer12.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer12.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.jadwalB = wx.BitmapButton( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"jadwal.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer12.Add( self.jadwalB, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer12.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer12.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.TugasB = wx.BitmapButton( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"tugas.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer12.Add( self.TugasB, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer12.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer12.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.AkunB = wx.BitmapButton( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"logout.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer12.Add( self.AkunB, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel10.SetSizer( bSizer12 )
		self.m_panel10.Layout()
		bSizer12.Fit( self.m_panel10 )
		bSizer11.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.jadwalB.Bind( wx.EVT_BUTTON, self.jadwalBOnButtonClick )
		self.TugasB.Bind( wx.EVT_BUTTON, self.TugasBOnButtonClick )
		self.AkunB.Bind( wx.EVT_BUTTON, self.AkunBOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def jadwalBOnButtonClick( self, event ):
		event.Skip()
	
	def TugasBOnButtonClick( self, event ):
		event.Skip()
	
	def AkunBOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tugas", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 184, 214, 241 ) )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_bitmap6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel14 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 4, 2, 0, 0 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Mata Kuliah                   :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer5.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.iMatkul = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.iMatkul, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Deadline                        :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer5.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.iJam = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.iJam, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Keterangan                    :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gSizer5.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.iKet = wx.TextCtrl( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.iKet, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer5.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self.m_panel14, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer5.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		self.m_panel14.SetSizer( gSizer5 )
		self.m_panel14.Layout()
		gSizer5.Fit( self.m_panel14 )
		self.m_notebook1.AddPage( self.m_panel14, u"Menambahkan", False )
		self.m_panel15 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.listtugas = wx.grid.Grid( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.listtugas.CreateGrid( 0, 3 )
		self.listtugas.EnableEditing( True )
		self.listtugas.EnableGridLines( True )
		self.listtugas.EnableDragGridSize( False )
		self.listtugas.SetMargins( 0, 0 )
		
		# Columns
		self.listtugas.SetColSize( 0, 152 )
		self.listtugas.SetColSize( 1, 270 )
		self.listtugas.SetColSize( 2, 265 )
		self.listtugas.EnableDragColMove( False )
		self.listtugas.EnableDragColSize( True )
		self.listtugas.SetColLabelSize( 30 )
		self.listtugas.SetColLabelValue( 0, u"Mata Kuliah" )
		self.listtugas.SetColLabelValue( 1, u"Deadline" )
		self.listtugas.SetColLabelValue( 2, u"Keterangan" )
		self.listtugas.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.listtugas.EnableDragRowSize( True )
		self.listtugas.SetRowLabelSize( 80 )
		self.listtugas.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.listtugas.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer17.Add( self.listtugas, 0, wx.ALL, 5 )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText35 = wx.StaticText( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gSizer6.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer6.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self.m_panel15, wx.ID_ANY, u"Ubah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer6.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self.m_panel15, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer6.Add( self.m_button15, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		self.m_panel15.SetSizer( bSizer17 )
		self.m_panel15.Layout()
		bSizer17.Fit( self.m_panel15 )
		self.m_notebook1.AddPage( self.m_panel15, u"List Tugas", True )
		
		bSizer15.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.k1 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.k1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer15.Add( self.k1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button12.Bind( wx.EVT_BUTTON, self.tambahClick )
		self.m_button14.Bind( wx.EVT_BUTTON, self.ubahClick )
		self.m_button15.Bind( wx.EVT_BUTTON, self.hapusonclick )
		self.k1.Bind( wx.EVT_BUTTON, self.k1OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def tambahClick( self, event ):
		event.Skip()
	
	def ubahClick( self, event ):
		event.Skip()
	
	def hapusonclick( self, event ):
		event.Skip()
	
	def k1OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame7
###########################################################################

class MyFrame7 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ubah Tugas", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 184, 214, 241 ) )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap7 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_bitmap7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		bSizer18.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		gSizer7 = wx.GridSizer( 7, 2, 0, 0 )
		
		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Masukkan ID                :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		gSizer7.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.iId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.iId, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		gSizer7.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer7.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Mata Kuliah                   :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		gSizer7.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.iMK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.iMK, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Deadline                        :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		gSizer7.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.iD = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.iD, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Keterangan                    :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		gSizer7.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.iKT = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.iKT, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		gSizer7.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Ubah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer7.Add( self.m_button17, 0, wx.ALL, 5 )
		
		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer7.Add( self.m_button18, 0, wx.ALL, 5 )
		
		
		bSizer18.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer18 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button16.Bind( wx.EVT_BUTTON, self.cariClick )
		self.m_button17.Bind( wx.EVT_BUTTON, self.ubahClick )
		self.m_button18.Bind( wx.EVT_BUTTON, self.k2OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cariClick( self, event ):
		event.Skip()
	
	def ubahClick( self, event ):
		event.Skip()
	
	def k2OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame8
###########################################################################

class MyFrame8 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hapus Tugas", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 184, 214, 241 ) )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap8 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_bitmap8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		bSizer19.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Masukkan ID                :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		gSizer8.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.i_id = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.i_id, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		gSizer8.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer8.Add( self.m_button19, 0, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Mata Kuliah                   :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		gSizer8.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.i_m = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.i_m, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Deadline                        :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		gSizer8.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		self.i_d = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.i_d, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keterangan                    :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		gSizer8.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.i_k = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.i_k, 0, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		gSizer8.Add( self.m_staticText52, 0, wx.ALL, 5 )
		
		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer8.Add( self.m_button20, 0, wx.ALL, 5 )
		
		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer8.Add( self.m_button21, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer19 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button19.Bind( wx.EVT_BUTTON, self.carionclick )
		self.m_button20.Bind( wx.EVT_BUTTON, self.hapusonclick )
		self.m_button21.Bind( wx.EVT_BUTTON, self.k3OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def carionclick( self, event ):
		event.Skip()
	
	def hapusonclick( self, event ):
		event.Skip()
	
	def k3OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame9
###########################################################################

class MyFrame9 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Jadwal", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 182, 214, 241 ) )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap10 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_bitmap10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel18 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer12 = wx.GridSizer( 6, 3, 0, 0 )
		
		self.m_staticText60 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Hari                                 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		gSizer12.Add( self.m_staticText60, 0, wx.ALL, 5 )
		
		self.hr = wx.TextCtrl( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.hr, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		gSizer12.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_staticText62 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Mata Kuliah                    :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		gSizer12.Add( self.m_staticText62, 0, wx.ALL, 5 )
		
		self.matkul = wx.TextCtrl( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.matkul, 0, wx.ALL, 5 )
		
		self.m_staticText63 = wx.StaticText( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		gSizer12.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		self.m_staticText64 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Kelas                               :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		gSizer12.Add( self.m_staticText64, 0, wx.ALL, 5 )
		
		self.kls = wx.TextCtrl( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.kls, 0, wx.ALL, 5 )
		
		self.m_staticText65 = wx.StaticText( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		gSizer12.Add( self.m_staticText65, 0, wx.ALL, 5 )
		
		self.m_staticText66 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Jam Mulai                       :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		gSizer12.Add( self.m_staticText66, 0, wx.ALL, 5 )
		
		self.jamml = wx.TextCtrl( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.jamml, 0, wx.ALL, 5 )
		
		self.m_staticText67 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"(00.00)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )
		gSizer12.Add( self.m_staticText67, 0, wx.ALL, 5 )
		
		self.m_staticText68 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Jam Selesai                    :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )
		gSizer12.Add( self.m_staticText68, 0, wx.ALL, 5 )
		
		self.jamslsi = wx.TextCtrl( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.jamslsi, 0, wx.ALL, 5 )
		
		self.m_staticText69 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"(00.00)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		gSizer12.Add( self.m_staticText69, 0, wx.ALL, 5 )
		
		self.m_staticText70 = wx.StaticText( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )
		gSizer12.Add( self.m_staticText70, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.m_panel18, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		gSizer12.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.m_button27 = wx.Button( self.m_panel18, wx.ID_ANY, u"Tambahkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button27.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer12.Add( self.m_button27, 0, wx.ALL, 5 )
		
		
		self.m_panel18.SetSizer( gSizer12 )
		self.m_panel18.Layout()
		gSizer12.Fit( self.m_panel18 )
		self.m_notebook3.AddPage( self.m_panel18, u"Menambahkan", False )
		self.m_panel19 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.listjadwal = wx.grid.Grid( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.listjadwal.CreateGrid( 0, 5 )
		self.listjadwal.EnableEditing( True )
		self.listjadwal.EnableGridLines( True )
		self.listjadwal.EnableDragGridSize( False )
		self.listjadwal.SetMargins( 0, 0 )
		
		# Columns
		self.listjadwal.SetColSize( 0, 120 )
		self.listjadwal.SetColSize( 1, 130 )
		self.listjadwal.SetColSize( 2, 120 )
		self.listjadwal.SetColSize( 3, 120 )
		self.listjadwal.SetColSize( 4, 120 )
		self.listjadwal.EnableDragColMove( False )
		self.listjadwal.EnableDragColSize( True )
		self.listjadwal.SetColLabelSize( 30 )
		self.listjadwal.SetColLabelValue( 0, u"Hari" )
		self.listjadwal.SetColLabelValue( 1, u"Mata Kuliah" )
		self.listjadwal.SetColLabelValue( 2, u"Kelas" )
		self.listjadwal.SetColLabelValue( 3, u"Jam Mulai" )
		self.listjadwal.SetColLabelValue( 4, u"Jam Selesai" )
		self.listjadwal.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.listjadwal.EnableDragRowSize( True )
		self.listjadwal.SetRowLabelSize( 80 )
		self.listjadwal.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.listjadwal.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer21.Add( self.listjadwal, 0, wx.ALL, 5 )
		
		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button31 = wx.Button( self.m_panel19, wx.ID_ANY, u"Ubah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer13.Add( self.m_button31, 0, wx.ALL, 5 )
		
		self.m_button32 = wx.Button( self.m_panel19, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer13.Add( self.m_button32, 0, wx.ALL, 5 )
		
		
		bSizer21.Add( gSizer13, 1, wx.EXPAND, 5 )
		
		
		self.m_panel19.SetSizer( bSizer21 )
		self.m_panel19.Layout()
		bSizer21.Fit( self.m_panel19 )
		self.m_notebook3.AddPage( self.m_panel19, u"List Jadwal", True )
		
		bSizer22.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer22.Add( self.m_button26, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer22 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button27.Bind( wx.EVT_BUTTON, self.tambahclick )
		self.m_button31.Bind( wx.EVT_BUTTON, self.ubahclick )
		self.m_button32.Bind( wx.EVT_BUTTON, self.hapusonclick )
		self.m_button26.Bind( wx.EVT_BUTTON, self.kembaliclick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def tambahclick( self, event ):
		event.Skip()
	
	def ubahclick( self, event ):
		event.Skip()
	
	def hapusonclick( self, event ):
		event.Skip()
	
	def kembaliclick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame10
###########################################################################

class MyFrame10 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ubah Jadwal", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 182, 214, 241 ) )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer14 = wx.GridSizer( 2, 3, 0, 0 )
		
		self.m_staticText76 = wx.StaticText( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )
		gSizer14.Add( self.m_staticText76, 0, wx.ALL, 5 )
		
		self.m_bitmap12 = wx.StaticBitmap( self.m_panel20, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.m_bitmap12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText77 = wx.StaticText( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		gSizer14.Add( self.m_staticText77, 0, wx.ALL, 5 )
		
		self.m_staticText78 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Masukkan ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )
		gSizer14.Add( self.m_staticText78, 0, wx.ALL, 5 )
		
		self.iID = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.iID, 0, wx.ALL, 5 )
		
		self.m_button30 = wx.Button( self.m_panel20, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer14.Add( self.m_button30, 0, wx.ALL, 5 )
		
		
		self.m_panel20.SetSizer( gSizer14 )
		self.m_panel20.Layout()
		gSizer14.Fit( self.m_panel20 )
		bSizer24.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer15 = wx.GridSizer( 7, 3, 0, 0 )
		
		self.m_staticText82 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Hari                                 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )
		gSizer15.Add( self.m_staticText82, 0, wx.ALL, 5 )
		
		self.iHari = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.iHari, 0, wx.ALL, 5 )
		
		self.m_staticText83 = wx.StaticText( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )
		gSizer15.Add( self.m_staticText83, 0, wx.ALL, 5 )
		
		self.m_staticText84 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Mata Kuliah                   :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )
		gSizer15.Add( self.m_staticText84, 0, wx.ALL, 5 )
		
		self.iM = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.iM, 0, wx.ALL, 5 )
		
		self.m_staticText85 = wx.StaticText( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		gSizer15.Add( self.m_staticText85, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Kelas                              :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		gSizer15.Add( self.m_staticText86, 0, wx.ALL, 5 )
		
		self.iK = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.iK, 0, wx.ALL, 5 )
		
		self.m_staticText87 = wx.StaticText( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )
		gSizer15.Add( self.m_staticText87, 0, wx.ALL, 5 )
		
		self.m_staticText88 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Jam Mulai                      :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		gSizer15.Add( self.m_staticText88, 0, wx.ALL, 5 )
		
		self.iJM = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.iJM, 0, wx.ALL, 5 )
		
		self.m_staticText90 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"(00.00)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )
		gSizer15.Add( self.m_staticText90, 0, wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Jam Selesai                    :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		gSizer15.Add( self.m_staticText91, 0, wx.ALL, 5 )
		
		self.iJS = wx.TextCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer15.Add( self.iJS, 0, wx.ALL, 5 )
		
		self.m_staticText92 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"(00.00)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )
		gSizer15.Add( self.m_staticText92, 0, wx.ALL, 5 )
		
		self.m_staticText93 = wx.StaticText( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )
		gSizer15.Add( self.m_staticText93, 0, wx.ALL, 5 )
		
		self.m_staticText94 = wx.StaticText( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )
		gSizer15.Add( self.m_staticText94, 0, wx.ALL, 5 )
		
		self.ubah1 = wx.Button( self.m_panel21, wx.ID_ANY, u"Ubah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ubah1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer15.Add( self.ubah1, 0, wx.ALL, 5 )
		
		self.k1 = wx.Button( self.m_panel21, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.k1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer15.Add( self.k1, 0, wx.ALL, 5 )
		
		
		self.m_panel21.SetSizer( gSizer15 )
		self.m_panel21.Layout()
		gSizer15.Fit( self.m_panel21 )
		bSizer24.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button30.Bind( wx.EVT_BUTTON, self.cari1OnButtonClick )
		self.ubah1.Bind( wx.EVT_BUTTON, self.ubah1OnButtonClick )
		self.k1.Bind( wx.EVT_BUTTON, self.k1OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cari1OnButtonClick( self, event ):
		event.Skip()
	
	def ubah1OnButtonClick( self, event ):
		event.Skip()
	
	def k1OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame11
###########################################################################

class MyFrame11 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hapus Jadwal", pos = wx.DefaultPosition, size = wx.Size( 804,639 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 182, 214, 241 ) )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer16 = wx.GridSizer( 2, 3, 0, 0 )
		
		self.m_staticText95 = wx.StaticText( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )
		gSizer16.Add( self.m_staticText95, 0, wx.ALL, 5 )
		
		self.m_bitmap13 = wx.StaticBitmap( self.m_panel22, wx.ID_ANY, wx.Bitmap( u"logo.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_bitmap13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText96 = wx.StaticText( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( -1 )
		gSizer16.Add( self.m_staticText96, 0, wx.ALL, 5 )
		
		self.m_staticText97 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"Masukkan ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText97.Wrap( -1 )
		gSizer16.Add( self.m_staticText97, 0, wx.ALL, 5 )
		
		self.in_id = wx.TextCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.in_id, 0, wx.ALL, 5 )
		
		self.m_button33 = wx.Button( self.m_panel22, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer16.Add( self.m_button33, 0, wx.ALL, 5 )
		
		
		self.m_panel22.SetSizer( gSizer16 )
		self.m_panel22.Layout()
		gSizer16.Fit( self.m_panel22 )
		bSizer25.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer17 = wx.GridSizer( 7, 3, 0, 0 )
		
		self.m_staticText99 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"Hari                                 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )
		gSizer17.Add( self.m_staticText99, 0, wx.ALL, 5 )
		
		self.in_hr = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.in_hr, 0, wx.ALL, 5 )
		
		self.m_staticText100 = wx.StaticText( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )
		gSizer17.Add( self.m_staticText100, 0, wx.ALL, 5 )
		
		self.m_staticText101 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"Mata Kuliah                   :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		gSizer17.Add( self.m_staticText101, 0, wx.ALL, 5 )
		
		self.in_matkul = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.in_matkul, 0, wx.ALL, 5 )
		
		self.m_staticText102 = wx.StaticText( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText102.Wrap( -1 )
		gSizer17.Add( self.m_staticText102, 0, wx.ALL, 5 )
		
		self.m_staticText103 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"Kelas                              :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText103.Wrap( -1 )
		gSizer17.Add( self.m_staticText103, 0, wx.ALL, 5 )
		
		self.in_kls = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.in_kls, 0, wx.ALL, 5 )
		
		self.m_staticText104 = wx.StaticText( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText104.Wrap( -1 )
		gSizer17.Add( self.m_staticText104, 0, wx.ALL, 5 )
		
		self.m_staticText105 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"Jam Mulai                      :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText105.Wrap( -1 )
		gSizer17.Add( self.m_staticText105, 0, wx.ALL, 5 )
		
		self.in_jammli = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.in_jammli, 0, wx.ALL, 5 )
		
		self.m_staticText106 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"(00.00)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText106.Wrap( -1 )
		gSizer17.Add( self.m_staticText106, 0, wx.ALL, 5 )
		
		self.m_staticText107 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"Jam Selesai                    :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText107.Wrap( -1 )
		gSizer17.Add( self.m_staticText107, 0, wx.ALL, 5 )
		
		self.in_jamslsi = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.in_jamslsi, 0, wx.ALL, 5 )
		
		self.m_staticText108 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"(00.00)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText108.Wrap( -1 )
		gSizer17.Add( self.m_staticText108, 0, wx.ALL, 5 )
		
		self.m_staticText109 = wx.StaticText( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText109.Wrap( -1 )
		gSizer17.Add( self.m_staticText109, 0, wx.ALL, 5 )
		
		self.m_staticText110 = wx.StaticText( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText110.Wrap( -1 )
		gSizer17.Add( self.m_staticText110, 0, wx.ALL, 5 )
		
		self.m_button34 = wx.Button( self.m_panel24, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button34.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer17.Add( self.m_button34, 0, wx.ALL, 5 )
		
		self.m_button35 = wx.Button( self.m_panel24, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button35.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		gSizer17.Add( self.m_button35, 0, wx.ALL, 5 )
		
		
		self.m_panel24.SetSizer( gSizer17 )
		self.m_panel24.Layout()
		gSizer17.Fit( self.m_panel24 )
		bSizer25.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button33.Bind( wx.EVT_BUTTON, self.carionclick )
		self.m_button34.Bind( wx.EVT_BUTTON, self.hapusonclick )
		self.m_button35.Bind( wx.EVT_BUTTON, self.k2OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def carionclick( self, event ):
		event.Skip()
	
	def hapusonclick( self, event ):
		event.Skip()
	
	def k2OnButtonClick( self, event ):
		event.Skip()
	


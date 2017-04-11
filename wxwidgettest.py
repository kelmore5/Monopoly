#!/usr/bin/env python
import wx
class MainWindow(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,800))
        self.CreateStatusBar()  # Shows  a status bar in the bottom of the window
        
        #Setting up a menu
        filemenu = wx.Menu()

        #wx.ID_ABOUT and wx.ID_EXIT are standard ids in wxWidgets
        #Sets up filemenu options
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the Program")
        
        #Creates menubars
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")   #Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)    #Adding the MenuBar to the Frame content
        
        #Sets events - Things done when clicked
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        
        self.Show(True)

        Board = wx.Image("Monopoly.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        MainPanel = wx.Panel(self, -1, (0, 0), (700,700), style = wx.SUNKEN_BORDER)

        self.picture = wx.StaticBitmap(MainPanel, -1, Board)
        
    def OnAbout(self, e):
        #Displays a dialog box with an OK button. wx.OK is a standard ID in wxWidgets
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() #Show it
        dlg.Destroy()   #Destroy it when finished

    def OnExit(self, e):
        self.Close(True)    #Close the frame

app = wx.App(False)
frame = MainWindow(None, 'Sample editor')
app.MainLoop()

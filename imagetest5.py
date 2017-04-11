import wx
class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (725,725))

        jpg = wx.Image("Monopoly.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        jpg2 = wx.Image("Money.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        panel = wx.Panel(self, -1, (0, 0), (700,700), style = wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, (540, 630), (560, 665), style = wx.SUNKEN_BORDER)
        self.picture = wx.StaticBitmap(panel, -1, jpg)
        panel.SetBackgroundColour(wx.WHITE)
        panel2.SetBackgroundColour(wx.WHITE)
        self.picture = wx.StaticBitmap(panel2, -1, jpg2)

        self.images = ["Chance.jpg", "Monopoly.jpg"]

        self.Bind(wx.EVT_BUTTON, self.OnClose, id = 1)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.Centre()

    def OnClose(self, event):
        self.Close()

    def OnSelect(self, event):
        item = "Chance.jpg"
        self.picture.SetFocus()
        self.picture.SetBitmap(wx.Bitmap(self.images[item]))

class MyApp(wx.App):
    def OnInit(self):
        dlg = MyDialog(None, -1, "combobox.py")
        dlg.ShowModal()
        dlg.Destroy()
        return True

app = MyApp(0)
app.MainLoop()

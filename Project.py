import wx
import rolling
import wx.lib.agw.genericmessagedialog
player1 = [1500, 0]
player2 = [1500, 0]
player3 = [1500, 0]
player = player1
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size = (725, 775))

        Board = wx.Image("Monopoly.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MainPanel = wx.Panel(self, -1, (0, 0), (700,700))
        self.board = wx.StaticBitmap(MainPanel, -1, Board)
        self.Centre()

        filemenu = wx.Menu()
        menuStart = filemenu.Append(wx.ID_ANY, "Start the Game!")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.playerturn, menuStart)
        self.Bind(wx.EVT_MENU, self.Exit, menuExit)

        self.Show(True)
        
    def playerturn(self, event):
        if player is player1:
            dlg = wx.MessageDialog(self, "It is time for MONOPOLY! Player 1 start?", "Start Game", wx.OK)
            result = dlg.ShowModal()
            dlg.Destroy()
            self.movement(player)

    def movement(self, player):
        if not "money" in dir(self) or not "racecar" in dir(self):
            panel = wx.Panel(self, -1, (605, 630), (630, 665))
            MoneyBag = wx.BitmapFromImage(wx.Image("Money.jpg", wx.BITMAP_TYPE_ANY), depth=1)
            self.money = wx.StaticBitmap(panel, -1, MoneyBag)
            panel = wx.Panel(self, -1, (630, 630), (655, 665))
            RaceCar = wx.BitmapFromImage(wx.Image("Racecar.jpg", wx.BITMAP_TYPE_ANY), depth = 1)
            self.racecar = wx.StaticBitmap(panel, -1, RaceCar)
            panel = wx.Panel(self, -1, (630, 630), (655, 665))
            Dog = wx.BitmapFromImage(wx.Image("Dog.jpg", wx.BITMAP_TYPE_ANY), depth = 1)
            self.dog = wx.StaticBitmap(panel, -1, Dog)
            rolling.refresh(self)
            self.movement(player)
        if player is player1:
            rolling.status(self, player, player1, player2, player3)
            self.money.Destroy()
            rolling.rolling(self, player)
            panelstart = [[605, 630], [540, 630], [490, 630], [433, 630], [380, 630], [326, 630], [273, 630], [221, 630], [166, 630], [114, 630], [68, 630], [36, 540], [36, 486], [36, 432], [36, 379], [36, 327], [36, 273], [36, 220], [36, 166], [36, 112], [35, 60], [112, 34], [166, 34], [220, 34], [273, 34], [326, 34], [379, 34], [432, 34], [486, 34], [539, 34], [593, 34], [629, 112], [629, 166], [629, 219], [629, 272], [629, 326], [629, 378], [629, 432], [629, 486], [629, 539]]
            panel = rolling.onspace(self, panelstart[player[1]])
            MoneyBag = wx.BitmapFromImage(wx.Image("Money.jpg", wx.BITMAP_TYPE_ANY), depth=1)
            self.money = wx.StaticBitmap(panel, -1, MoneyBag)
            rolling.refresh(self)
            rolling.landing(self, player, player2, panelstart, player3)
            rolling.status(self, player, player1, player2, player3)
            rolling.refresh(self)
            player = player2
        if player is player2:
            rolling.status(self, player, player1, player2, player3)
            self.racecar.Destroy()
            rolling.rolling(self, player)
            panelstart = [[630, 630], [565, 630], [515, 630], [458, 630], [405, 630], [351, 630], [298, 630], [246, 630], [191, 630], [139, 630], [93, 630], [61, 540], [61, 486], [61, 432], [61, 379], [61, 327], [61, 273], [61, 220], [61, 166], [61, 112], [60, 60], [137, 34], [191, 34], [245, 34], [298, 34], [351, 34], [404, 34], [457, 34], [511, 34], [564, 34], [618, 34], [654, 112], [654, 166], [654, 219], [654, 272], [654, 326], [654, 378], [654, 432], [654, 486], [654, 539]]
            panel = rolling.onspace(self, panelstart[player[1]])
            RaceCar = wx.BitmapFromImage(wx.Image("Racecar.jpg", wx.BITMAP_TYPE_ANY), depth = 1)
            self.racecar = wx.StaticBitmap(panel, -1, RaceCar)
            rolling.refresh(self)
            rolling.landing(self, player, player1, panelstart, player3)
            rolling.status(self, player, player1, player2, player3)
            rolling.refresh(self)
            player = player3
        if player is player3:
            rolling.status(self, player, player1, player2, player3)
            self.dog.Destroy()
            rolling.rolling(self, player)
            panelstart = [[630, 630], [565, 630], [515, 630], [458, 630], [405, 630], [351, 630], [298, 630], [246, 630], [191, 630], [139, 630], [94, 630], [61, 540], [61, 486], [61, 432], [61, 379], [61, 327], [61, 273], [61, 220], [61, 166], [61, 112], [60, 60], [137, 34], [191, 34], [245, 34], [298, 34], [351, 34], [404, 34], [457, 34], [511, 34], [564, 34], [618, 34], [654, 112], [654, 166], [654, 219], [654, 272], [654, 326], [654, 378], [654, 432], [654, 486], [654, 539]]
            panel = rolling.onspace(self, panelstart[player[1]])
            Dog = wx.BitmapFromImage(wx.Image("Dog.jpg", wx.BITMAP_TYPE_ANY), depth = 1)
            self.dog = wx.StaticBitmap(panel, -1, Dog)
            rolling.refresh(self)
            rolling.landing(self, player, player1, panelstart, player3)
            rolling.status(self, player, player1, player2, player3)
            rolling.refresh(self)
            player = player1
            self.movement(player)
            
    def Exit(self, e):
        self.Close(True)
        return True

app = wx.App(False)
frame = MainWindow(None, "Monopoly")
app.MainLoop()

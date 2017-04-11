import wx
import wx.lib.agw.genericmessagedialog as GMD
def position(x, y):
    resolution = wx.GetDisplaySize()
    resolution = [k/2 for k in resolution]
    resolution[0] += x
    resolution[1] += y
    resolution = tuple(resolution)
    return resolution
def status(self, player, player1, player2):
    if player is player1:
        title = "Player 1's Turn"
    elif player is player2:
        title = "Player 2's Turn"
    message = "Money:" + str(player[0]) + "\nProperties:\n" + "\n".join(player[2:]) + "\n\nRoll\End Turn?"
    status = GMD.GenericMessageDialog(self, message, title, wx.DEFAULT)
    status.SetSize((200, 400))
    status.SetPosition(position(350, -188))
    status.ShowModal()
def rolling(self, player):
    import random
    roll = random.randint(2,12)
    player[1] += roll
    if player[1] > 39:
        player[1] -= 40
        dlg = GMD.GenericMessageDialog(self, "You passed Go. Collect $200", "Passed Go", wx.OK)
        result = dlg.ShowModal()
        player[0] += 200
        return player
    else:
        return player
def onspace(self, location):
    location2 = list(location)
    location2[0] += 25
    location2[1] += 35
    location2 = tuple(location)
    panel = wx.Panel(self, -1, location, location2)
    return panel
def refresh(self):
    self.board.Refresh()
    self.money.Refresh()
    self.racecar.Refresh()
    return self
def landing(self, player, player2, panelstart):
    spaces = ["Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Places", "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad", "St. James Avenue", "Community Chest", "Tennessee Avenue", "New York Avenue", "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue", "B. & O. Railroad", "Atlantic Avenue", "Ventrone Avenue", "Water Works", "Marven Gardens", "Go to Jail", "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"] 
    prices = ["", 60, "CC", 60, -200, 200, 100, "CH", 100, 120, "", 140, 150, 140, 160, 200, 180, "CC", 180, 200, "", 220, "CH", 220, 240, 200, 260, 260, 150, 280, "", 300, 300, "CC", 320, 200, "CH", 350, -75, 400]
    pictures = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen", "twenty", "twenty1", "twenty2", "twenty3", "twenty4", "twenty5", "twenty6", "twenty7", "twenty8", "twenty9", "thirty", "thirty1", "thirty2", "thirty3", "thirty4", "thirty5", "thirty6", "thirty7", "thirty8", "thirty9"]
    rents = ["", 2, "", 4, "", 25, 6, "", 6, 8, "", 10, 30, 10, 12, 25, 14, "", 14, 16, "", 18, "", 18, 20, 25, 22, 22, 30, 24, "", 26, 26, "", 28, 25, "", 35, "", 50]
    price = prices[player[1]]
    space = spaces[player[1]]

    image = "Spaces/" + pictures[player[1]] + ".jpg"
    image = wx.Image(image, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    dialog = wx.Dialog(None, -1, pos = position(-350-image.GetWidth(), -image.GetHeight()/2), size = (image.GetWidth(), image.GetHeight()+25))
    panel = wx.Panel(dialog, size = (image.GetWidth(),image.GetHeight()))
    panel.Center()
    self.property = wx.StaticBitmap(panel, -1, image)
    dialog.Show(True)
    
    if price == "CC":
        dlg = GMD.GenericMessageDialog(self, "You landed on %s." %(space), "Chance", wx.OK)
        result = dlg.ShowModal()
        dialog.Show(False)
        return
    elif price == "CH":
        dlg = GMD.GenericMessageDialog(self, "You landed on %s." %(space), "Community Chest", wx.OK)
        result = dlg.ShowModal()
        dialog.Show(False)
        return
    elif space == "Go to Jail":
        dlg = GMD.GenericMessageDialog(self, "GO TO JAIL. Do not pass Go. Do not collect $200. $50 is being subtracted for bail.", "Going to Jail", wx.OK)
        result = dlg.ShowModal()
        player[0] -= 50
        player[1] = 10
        if panelstart[player[1]] == [68, 630]:
            self.money.Destroy()
            panelstart = [(605, 630), (540, 630), (490, 630), (433, 630), (380, 630), (326, 630), (273, 630), (221, 630), (166, 630), (114, 630), (68, 630), (36, 540), (36, 486), (36, 432), (36, 379), (36, 327), (36, 273), (36, 220), (36, 166), (36, 112), (35, 60), (112, 34), (166, 34), (220, 34), (273, 34), (326, 34), (379, 34), (432, 34), (486, 34), (539, 34), (593, 34), (629, 112), (629, 166), (629, 219), (629, 272), (629, 326), (629, 378), (629, 432), (629, 486), (629, 539)]
            panel = onspace(self, panelstart[player[1]])
            MoneyBag = wx.BitmapFromImage(wx.Image("Money.jpg", wx.BITMAP_TYPE_ANY), depth=1)
            self.money = wx.StaticBitmap(panel, -1, MoneyBag)
            refresh(self)
        elif panelstart[player[1]] == [93, 630]:
            self.racecar.Destroy()
            panelstart = [[630, 630], [565, 630], [515, 630], [458, 630], [405, 630], [351, 630], [298, 630], [246, 630], [191, 630], [139, 630], [93, 630], [61, 540], [61, 486], [61, 432], [61, 379], [61, 327], [61, 273], [61, 220], [61, 166], [61, 112], [60, 60], [137, 34], [191, 34], [245, 34], [298, 34], [351, 34], [404, 34], [457, 34], [511, 34], [564, 34], [618, 34], [654, 112], [654, 166], [654, 219], [654, 272], [654, 326], [654, 378], [654, 432], [654, 486], [654, 539]]
            panel = onspace(self, panelstart[player[1]])
            RaceCar = wx.BitmapFromImage(wx.Image("Racecar.jpg", wx.BITMAP_TYPE_ANY), depth = 1)
            self.racecar = wx.StaticBitmap(panel, -1, RaceCar)
            refresh(self)
        dialog.Show(False)
        return self
    elif space == "Free Parking":
        dlg = GMD.GenericMessageDialog(self, "You landed on Free Parking. Collect $150", "Free Parking", wx.OK)
        result = dlg.ShowModal()
        player[0] += 150
        dialog.Show(False)
        return
    elif space == "Go":
        dlg = GMD.GenericMessageDialog(self, "You landed on Go. Collect $200", "Landed on Go", wx.OK)
        result = dlg.ShowModal()
        dialog.Show(False)
        return
    elif space == "Jail":
        dlg = GMD.GenericMessageDialog(self, "You landed on %s." %(space), "Just Visiting", wx.OK)
        result = dlg.ShowModal()
        dialog.Show(False)
        return
    elif price < 0:
        dlg = GMD.GenericMessageDialog(self, "You landed on tax. You have %s. You have to pay $%s." %(player[0], str(price)[1:]), "Tax", wx.OK)
        result = dlg.ShowModal()
        player[0] += price
        dialog.Show(False)
        return
    elif space in player:
        dlg = GMD.GenericMessageDialog(self, "You laned on %s.\nYou already own it." %(space), "Property Owned", wx.OK)
        result = dlg.ShowModal()
        dialog.Show(False)
        return
    elif space in player2:
        rent = rents[player[1]]
        dlg = GMD.GenericMessageDialog(self, "You landed on %s.\n%s is owned by the other Player. You have $%s.\nYou have to pay $%s to the other Player.""" %(space, space, player[0], rent), "Property Owned", wx.OK)
        result = dlg.ShowModal()
        player[0] -= rent
        player2[0] += rent
        dialog.Show(False)
        return
    else:
        dlg = GMD.GenericMessageDialog(self, "You landed on %s.\nYou have %s.\nWould you like to purchase it for %s?" %(space, player[0], price), "Property", wx.YES_NO)
        dlg.SetSize((300,150))
        dlg.SetPosition(position(-155,-100))
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_YES:
            player[0] -= price
            player.append(space)
            if player[0] <= 0:
                player[0] += price
                player.remove(space)
                dlg = GMD.GenericMessageDialog(self, "You do not have enough money to purchase this property.\nYou only have $%s." %player[0], "Not enough funds", wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
            dialog.Destroy()
            return
        if result == wx.ID_NO:
            dialog.Destroy()
            return

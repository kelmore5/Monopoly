import wx
def landing(location):
    spaces = ["Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Places", "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad", "St. James Avenue", "Community Chest", "Tennessee Avenue", "New York Avenue", "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue", "B. & O. Railroad", "Atlantic Avenue", "Ventrone Avenue", "Water Works", "Marven Gardens", "Go to Jail", "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"] 
    prices = [60, "CC", 60, -200, 200, 100, "CH", 100, 120, "", 140, 150, 140, 160, 200, 180, "CC", 180, 200, "", 220, "CH", 240, 200, 260, 260, 150, 280, "", 300, 300, "CC", 320, 200, "CH", 350, -75, 400]
    price = prices[location]
    space = spaces[location]
    if price == "CC" or price == "CH":
        return
    elif price == "":
        return
    elif price < 0:
        player1[0] += space
        return
    else:
        dlg = wx.MessageDialog(self, "Would you like to buy it?", "You landed on %s" %space, wx.YES, wx.NO)
        

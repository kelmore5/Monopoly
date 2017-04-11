""" Dialog to ask a model question, with coder-specified list of buttons. 
"""
import wx
from wx.lib.evtmgr import eventManager

class ModalQuestion(wx.Dialog):
    """ Ask a question.

    Modal return value will be the index into the list of buttons.  Buttons can be specified
    either as strings or as IDs.
    """

    def __init__(self, parent, message, buttons, **kw):
        wx.Dialog.__init__(self, parent, **kw)

        topSizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(topSizer)

        topSizer.Add(wx.StaticText(self, label=message), flag=wx.ALIGN_CENTRE|wx.ALL, border=5)

        line = wx.StaticLine(self, size=(20, -1), style=wx.LI_HORIZONTAL)
        topSizer.Add(line, flag=wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, border=5)

        buttonSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        topSizer.Add(buttonSizer, flag=wx.ALIGN_CENTRE)

        for i, button in enumerate(buttons):
            if isinstance(button, (int, long)):
                b = wx.Button(self, id=button)
            else:
                b = wx.Button(self, label=button)

                eventManager.Register(dropArgs(curry(self.EndModal, i)), wx.EVT_BUTTON, b)
                buttonSizer.Add(b, flag=wx.ALL, border=5)

            self.Fit()

    def questionDialog(message, buttons=[wx.ID_OK, wx.ID_CANCEL], caption=''):
        """ Ask a question.

        Return value will be the button the user clicked, in whatever form it was specified.
        Allowable button specifications are strings or wxIDs of stock buttons.

        If the user clicks the 'x' close button in the corner, the return value will be None.
        """

        dlg = ModalQuestion(None, message, buttons, title=caption)
        try:
            return buttons[dlg.ShowModal()]
        except IndexError:
            return None

class MyApp(wx.App):
    def OnInit(self):
        dlg = ModalQuestion(None, -1, "Monopoly.py")
        dlg.ShowModal()
        dlg.Destroy()
        return True

app = MyApp(0)
app.MainLoop()


import tkinter as tk


class IPage(tk.Frame):
    def __init__(self, parent, **kw):
        tk.Frame.__init__(self, parent, **kw)


class OutputPage(IPage):
    def __init__(self, parent, **kw):
        IPage.__init__(self, parent, **kw)


class InputPage(IPage):
    def __init__(self, parent, name, **kw):
        self.name = name
        IPage.__init__(self, parent, **kw)

    # virtual
    def collectData(self):
        pass

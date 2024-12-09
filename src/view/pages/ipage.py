import tkinter as tk
from misc.observer import Publisher


class IPage(tk.Frame):
    def __init__(self, parent, **kw):
        tk.Frame.__init__(self, parent, **kw)
        self.pub = Publisher()

    def publisher(self):
        return self.pub

    # virtual
    def trigger(self):
        pass

    # virtual
    def __collectData__(self):
        pass


class OutputPage(IPage):
    def __init__(self, parent, **kw):
        IPage.__init__(self, parent, **kw)


class InputPage(IPage):
    def __init__(self, parent, name, **kw):
        IPage.__init__(self, parent, **kw)
        self.__name = name

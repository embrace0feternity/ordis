import tkinter as tk


class MainMenu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self,
                         parent,
                         background="white",
                         border=0,
                         borderwidth=1,
                         relief='flat',
                         activeborderwidth=0,
                         font=("Arial", 11))

    def createSubMenu(self, menuName, connectTo, **kw):
        sub = tk.Menu(tearoff=False,
                      background="white",
                      border=0,
                      borderwidth=5,
                      relief='flat',
                      activeborderwidth=0,
                      font=("Arial", 11))
        names = kw["itemsNames"]
        controller = kw["controller"]
        cmdArgs = kw["commandArgs"]
        if (controller == None):
            for i in range(len(names)):
                sub.add_command(label=names[i])
        else:
            for i in range(len(names)):
                sub.add_command(
                    label=names[i], command=lambda fr=cmdArgs[i]: controller.show_frame(fr))
        connectTo.add_cascade(label=menuName, menu=sub)

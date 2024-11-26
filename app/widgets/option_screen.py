import tkinter as tk
from app.widgets.main_menu import MainMenu
from app.widgets.layout_screen import LayoutScreen
from app.widgets.pages.pages import *

# Top-left application widget


class OptionScreen(tk.Frame):
    def __init__(self, parent, stack, **kw):
        tk.Frame.__init__(self, parent, **kw)

        self.stackFrame = LayoutScreen(self, stack)
        self.stackFrame.pack_propagate(0)
        self.stackFrame.configure(width=200, height=200)
        self.stackFrame.pack(
            side="top", anchor="nw", fill="both")

        buttonFrame = tk.Frame(self)
        buttonFrame.pack(side="top", fill="x")

        buttonFrame.columnconfigure(index=0, weight=1)
        buttonFrame.columnconfigure(index=1, weight=1)

        def runCommand(obj):
            stTop = obj.visible()
            print(stTop.collectData())

        self.__runButton = tk.Button(buttonFrame,
                                     text="run",
                                     command=lambda obj=self.stackFrame: runCommand(obj))
        self.__runButton.grid(row=0, column=0, sticky="news")

        self.__terminateButton = tk.Button(buttonFrame,
                                           text="terminate",
                                           command=lambda: print("terminate"))
        self.__terminateButton.grid(row=0, column=1, sticky="news")

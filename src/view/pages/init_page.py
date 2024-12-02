from tkinter import StringVar

from widgets.horizontal_table import *
from pages.ipage import InputPage


def callback(sv):
    print(sv.get())


class InitPage(InputPage):
    def __init__(self, parent):
        InputPage.__init__(self, parent, "init option",
                           background="pink", width=300, height=600)

        table = HorizontalTable(self)
        table.pack()

        # self.__nameTracker = tk.StringVar()
        # self.__nameTracker.trace_add(
        #     "write", lambda name, index, mode, sv=self.__nameTracker: callback(sv))
        table.addDataEntry(property="chip", defaultValue="8")
        table.addDataEntry(property="channel", defaultValue="8")
        table.addDataEntry(property="block", defaultValue="2048")
        table.addDataEntry(property="page", defaultValue="128")
        table.addDataEntry(property="page size", defaultValue="4096")
        table.addDataEntry(property="ti size", defaultValue="2048")

    # override
    def collectData(self):
        print("init")

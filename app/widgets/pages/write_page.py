from tkinter import StringVar

from app.widgets.horizontal_table import *
from app.widgets.pages.ipage import InputPage


def callback(sv):
    print(sv.get())


class WritePage(InputPage):
    def __init__(self, parent):
        InputPage.__init__(self, parent, "write option",
                           background="purple")

        table = HorizontalTable(self)
        table.pack()

        self.__nameTracker = tk.StringVar()
        self.__nameTracker.trace_add(
            "write", lambda name, index, mode, sv=self.__nameTracker: callback(sv))
        table.addDataEntry(property="file name", bind=self.__nameTracker)
        table.addDataCheckbox(property="user flow")
        table.addDataEntry(property="address")
        table.addDataEntry(property="ti")

    # override
    def collectData(self):
        print("write")

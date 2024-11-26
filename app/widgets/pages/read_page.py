from tkinter import StringVar
from app.widgets.horizontal_table import *
from app.widgets.pages.ipage import InputPage


def callback(sv):
    print(sv.get())


class ReadPage(InputPage):
    def __init__(self, parent):
        InputPage.__init__(self, parent, "read option",
                           background="light blue")
        table = HorizontalTable(self)
        table.pack()

        self.__nameTracker = tk.StringVar()
        self.__nameTracker.trace_add(
            "write", lambda name, index, mode, sv=self.__nameTracker: callback(sv))
        table.addDataEntry(property="file name", bind=self.__nameTracker)
        table.addDataEntry(property="percent", defaultValue="0")
        table.addDataEntry(property="offset", defaultValue="0")

    # override
    def collectData(self):
        return 2

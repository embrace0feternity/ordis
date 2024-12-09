from tkinter import StringVar, IntVar

from view.widgets.horizontal_table import *
from view.pages.ipage import InputPage


def callback(sv):
    print(sv.get())


class CreatePage(InputPage):
    def __init__(self, parent):
        InputPage.__init__(self, parent, "create option",
                           background="grey", width=300, height=600)

        table = HorizontalTable(self)
        table.pack()

        self.__nameTracker = tk.StringVar()
        # self.__nameTracker.trace_add(
        #     "write", lambda name, index, mode, sv=self.__nameTracker: callback(sv))
        self.__timeTracker = tk.IntVar(value=0)
        self.__attributeTracker = tk.IntVar(value=61440)
        self.__reserveTracker = tk.IntVar(value=0)
        self.__limitTracker = tk.IntVar(value=0)
        table.addDataEntry(property="file name", bind=self.__nameTracker)
        table.addDataEntry(
            property="time", bind=self.__timeTracker)
        table.addDataEntry(property="attribute", bind=self.__attributeTracker)
        table.addDataEntry(property="reserve", bind=self.__reserveTracker)
        table.addDataEntry(property="limit", bind=self.__limitTracker)

    # override
    def __collectData__(self):
        return (self.__nameTracker.get(),
                self.__timeTracker.get(),
                self.__attributeTracker.get(),
                self.__reserveTracker.get(),
                self.__limitTracker.get())

    # override
    def trigger(self):
        data = self.__collectData__()
        self.pub.notify(data)

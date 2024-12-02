import tkinter as tk
from tkinter import IntVar


class HorizontalTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.__currRow = 0
        self.__bind = {}
        self.__data = {}

    def __addProperty(self, name):
        label = tk.Label(self, text=name, padx=3, pady=3)
        label.grid(row=self.__currRow, column=0, sticky="news")
        self.__currRow += 1

    def addDataLabel(self, **kw):
        label = tk.Label(self, padx=3, pady=3)
        label.grid(row=self.__currRow, column=1, sticky="news")
        self.__data[kw["property"]] = label
        self.__addProperty(kw["property"])

    def addDataCheckbox(self, **kw):
        enabled = IntVar()
        checkbox = tk.Checkbutton(self, variable=enabled)
        checkbox.grid(row=self.__currRow, column=1, sticky="w")
        self.__addProperty(kw["property"])

    def addDataEntry(self, **kw):
        entry = tk.Entry(self)
        self.rowconfigure(index=self.__currRow, weight=1)
        entry.grid(row=self.__currRow, column=1, sticky="news")
        if "bind" in kw:
            value = kw["bind"].get()
            entry.insert(0, value)
            entry.configure(textvariable=kw["bind"])
        if "defaultValue" in kw:
            if not "bind" in kw:
                entry.insert(0, kw["defaultValue"])
        self.__addProperty(kw["property"])

    def getBindDict(self):
        return self.__bind

    def getProperty(self):
        return self.__data

    def update(self, property, data):
        l = self.__data[property]
        l.configure(text=data)

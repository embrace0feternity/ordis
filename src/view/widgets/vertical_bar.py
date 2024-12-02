
import tkinter as tk
from tkinter import ttk
from tkinter.constants import *


class VerticalScrolledFrame():
    def __init__(self, parent):
        self.__canvas = canvas = tk.Canvas(parent, borderwidth=0)
        self.frame = tk.Frame(parent)
        vsb = ttk.Scrollbar(orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", expand=True, fill="both")
        canvas.create_window(0, 0, window=self.frame, anchor="nw")

        self.__canvas.update_idletasks()
        self.__canvas.configure(scrollregion=self.__canvas.bbox("all"))

import tkinter as tk
from tkinter import ttk
from view.widgets.option_screen import OptionScreen
from view.widgets.main_menu import MainMenu
from view.widgets.layout_screen import LayoutScreen
from view.pages.pages import *


class App:
    def __init__(self, parent, pubdump):

        # left frame
        leftFrame = tk.Frame(parent)

        optionScreenPageStack = (
            CrPage.CreatePage, WrPage.WritePage, RdPage.ReadPage, InPage.InitPage)
        self.__optionScreen = OptionScreen(leftFrame, optionScreenPageStack)
        self.__optionScreen.register(pubdump)
        self.__optionScreen.pack(side="top")

        self.__fsStructure = tk.Frame(leftFrame, background="red")
        self.__fsStructure.pack(side="top", fill="both", expand=True)

        leftFrame.pack(side="left", fill="y")

        # right frame
        rightFrame = tk.Frame(parent)

        self.__queue = tk.Frame(rightFrame, width=50)
        self.__queue.pack(side="top", expand=True, fill="both")

        self.__fparams = tk.Frame(rightFrame, background="red")
        self.__fparams.pack(side="top", expand=True, fill="both")

        rightFrame.pack(side="right", fill="y")

        # center frame
        notebook = ttk.Notebook(parent)
        notebook.pack(side="left", fill="both", expand=True)

        viewNotebook = tk.Frame(notebook)
        viewNotebook.pack(side="left", fill="both", expand=True)
        logNoteBook = tk.Frame(notebook)
        logNoteBook.pack(side="left", fill="both", expand=True)

        notebook.add(viewNotebook, text="view")
        notebook.add(logNoteBook, text="log")

        mainScreenPagesStorage = (SbPage.SuperBlockPage, BmPage.InodeBitmap,
                                  BmPage.DataBitmap, BmPage.BadBitmap, BmPage.MetaBitmap)
        self.__metaDataScreen = LayoutScreen(
            viewNotebook, mainScreenPagesStorage)
        self.__metaDataScreen.pack(side="top", expand=True, fill="both")

        # menu
        menu = MainMenu(parent)
        # optMenuNames = ("create", "mkdir", "write", "read",
        #                 "rmdir", "find", "format", "init")
        optMenuNames = ("create", "write", "read", "init")
        viewMenuNames = ("super block", "inode bitmap", "data bitmap", "bad bitmap",
                         "meta bitmap")
        menu.createSubMenu("Options", menu, itemsNames=optMenuNames,
                           controller=self.__optionScreen.stackFrame, commandArgs=optionScreenPageStack)
        menu.createSubMenu("View", menu, itemsNames=viewMenuNames,
                           controller=self.__metaDataScreen, commandArgs=mainScreenPagesStorage)

        parent.config(menu=menu)

from view.pages.ipage import OutputPage
from tkinter import Label


class InodeBitmap(OutputPage):
    def __init__(self, parent):
        OutputPage.__init__(self, parent)

        label = Label(self, text="Bitmap page", background="green")
        label.pack(fill="both", expand=True)


class DataBitmap(OutputPage):
    def __init__(self, parent):
        OutputPage.__init__(self, parent)

        label = Label(self, text="Bitmap page", background="brown")
        label.pack(fill="both", expand=True)


class BadBitmap(OutputPage):
    def __init__(self, parent):
        OutputPage.__init__(self, parent)

        label = Label(self, text="Bitmap page", background="blue")
        label.pack(fill="both", expand=True)


class MetaBitmap(OutputPage):
    def __init__(self, parent):
        OutputPage.__init__(self, parent)

        label = Label(self, text="Bitmap page", background="red")
        label.pack(fill="both", expand=True)

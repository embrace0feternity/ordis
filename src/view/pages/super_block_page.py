from view.widgets.horizontal_table import *
from view.pages.ipage import OutputPage


class SuperBlockPage(OutputPage):
    def __init__(self, parent):
        OutputPage.__init__(self, parent)

        table = HorizontalTable(self)
        table.pack(expand=True, fill="both")

        table.addDataLabel(property="chip")
        table.addDataLabel(property="channel")
        table.addDataLabel(property="block")
        table.addDataLabel(property="page")
        table.addDataLabel(property="page size")
        table.addDataLabel(property="ti size")
        table.addDataLabel(property="next bs")
        table.addDataLabel(property="file counter")

        table.update("chip", 8)

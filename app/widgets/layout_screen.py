import tkinter as tk


class LayoutScreen(tk.Frame):
    def __init__(self, parent, pages):
        tk.Frame.__init__(self, parent)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Set weight of 0.0 positiong in grid. There will be pages
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in pages:
            frame = F(container)
            self.frames[F] = frame

        self.show_frame(pages[0])

    def show_frame(self, frame):
        fr = self.frames[frame]
        # Set fr into 0.0 grid position
        fr.grid(row=0, column=0, sticky="nsew")
        # Show frame
        fr.tkraise()
        self.__visible = fr

    def visible(self):
        return self.__visible

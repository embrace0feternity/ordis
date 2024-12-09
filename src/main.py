import tkinter as tk
import ordis
from view.application import App
from misc.observer import PublisherDump
from misc.natah import Natah


if __name__ == "__main__":
    natah = Natah()
    pubDump = PublisherDump()
    main = tk.Tk()
    main.geometry("1440x820+200+100")
    main.minsize(600, 400)
    app = App(main, pubDump)
    l = pubDump.list()
    l[0].subscribe(natah.create)
    main.mainloop()
# class Tracker:

#     """ Toplevel windows resize event tracker. """

#     def __init__(self, toplevel):
#         self.toplevel = toplevel
#         self.width, self.height = toplevel.winfo_width(), toplevel.winfo_height()
#         self._func_id = None

#     def bind_config(self):
#         self._func_id = self.toplevel.bind("<Configure>", self.resize)

#     def unbind_config(self):  # Untested.
#         if self._func_id:
#             self.toplevel.unbind("<Configure>", self._func_id)
#             self._func_id = Noner

#     def resize(self, event):
#         if (event.widget == self.toplevel and
#            (self.width != event.width or self.height != event.height)):
#             print(f'{event.widget=}: {event.height=}, {event.width=}\n')
#             self.width, self.height = event.width, event.height


# parent = tk.Tk()
# parent.title('parent')
# fr = tk.Frame(parent)
# fr.pack(expand=True, fill="both")
# tracker = Tracker(fr)
# tracker.bind_config()

# parent.mainloop()

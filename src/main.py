import tkinter as tk
from view.application import App
from misc.natah import natah
from misc.interpreter import Interpreter

from pathlib import Path
import json
import os


def findPreset(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def parseParameters(cmakeArgs: list):
    insert = ""
    i = 1
    # print(cmakeArgs)
    for arg in cmakeArgs:
        pos = arg.find('=')
        key = arg[:pos]
        value = arg[pos+1:]
        insert += '"' + key + "\": " + '"' + value + '"'
        if i != len(cmakeArgs):
            insert += ", "
        i += 1

    print(insert)


if __name__ == "__main__":
    name = "CMakePresets.json"
    preset = findPreset(name, Path.cwd())[0]
    path = Path(f"{Path.cwd()}/build/Release/generators/CMakePresets.json")
    data = json.loads(path.read_text(encoding='utf-8'))
    configurePresetObj = data["configurePresets"][0]
    cmake_args = ["-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=q/w/e/r",
                  "-DCMAKE_BUILD_TYPE=Release"]
    if not "environment" in configurePresetObj:
        parseParameters(cmake_args)
    print("--------")
    print(configurePresetObj)
    # "environment": {
    #                 "EXAMPLE_VERSION_INFO": "1.0",
    #                 "PYTHON_EXECUTABLE": "/home/embrace0feternity/embrace0feternity/projects/ordis/.venv_ordis/bin/python3",
    #                 "CMAKE_LIBRARY_OUTPUT_DIRECTORY": "/home/embrace0feternity/embrace0feternity/projects/ordis/build/lib.linux-x86_64-cpython-312/"
    #             },

    # interpreter = Interpreter()
    # natah.setConnection("create", interpreter.create)
    # main = tk.Tk()
    # main.geometry("1440x820+200+100")
    # main.minsize(600, 400)
    # app = App(main)
    # main.mainloop()

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

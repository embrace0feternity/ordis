
class Natah:
    def __init__(self):
        self.__connections = {}

    def setConnection(self, name, handler = None):
        signal = self.Signal(handler)
        self.__connections[name] = signal

    def updateConnection(self, name, handler):
        if name in self.__connections:
            self.__connections[name].update(handler)

    def removeConnection(self, name):
        if name in self.__connections:
            signal = self.__connections[name]
            self.__connections.remove(name)
    
    def emit(self, name, args):
        if name in self.__connections:
            self.__connections[name].emit(args)

    class Signal:
        def __init__(self, handler = None):
            self.update(handler)

        def update(self, handler):
            self.__handler = handler

        def emit(self, args):
            if (self.__handler != None):
                self.__handler(args)
            else:
                print("NO HANDLER")


natah = Natah()
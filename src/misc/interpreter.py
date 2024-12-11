import ordis

class Interpreter:
    def __init__(self):
        self.__ordis = ordis.Runner()

    def create(self, dict):
        print(dict)
        self.__ordis.create(dict[0], dict[1], dict[2], dict[3], dict[4])
        


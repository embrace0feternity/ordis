import ordis
from misc.observer import Subscriber


class Natah:
    class Natah_create(Subscriber):
        def __init__(self, sub):
            self.__onUpd = sub

        def update(self, data):
            self.__onUpd(data)

    def __init__(self):
        self.__ordis = ordis.Runner()
        self.create = self.Natah_create(self.__create)

    def __create(self, data):
        print("file name", data[0])

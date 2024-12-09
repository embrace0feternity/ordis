class Publisher:
    def __init__(self):
        self.__subList = []

    def subscribe(self, sub):
        self.__subList.append(sub)

    def forget(self, sub):
        self.__subList.remove(sub)

    def notify(self, dict):
        for sub in self.__subList:
            sub.update(dict)


class Subscriber:

    # virtual
    def update(self, dict):
        pass


class PublisherDump:
    def __init__(self):
        self.__publisherList = []

    def register(self, publisher):
        self.__publisherList.append(publisher)

    def list(self):
        return self.__publisherList

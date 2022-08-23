import pickle


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None   # To avoid error of searialization file discriptor
        return attributes


read_1 = Reader ('Reader.txt')
print("read_1.read()", read_1.read())
print(read_1.__getstate__())


read_1.close

import pickle


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()


    def __getstate__(self):
        attributes = {**self.__dict__}
        attributes['fh'] = None # To avoid error of searialization file discriptor
        return attributes

    def __setstate__(self, value): # write data from file to class attributes
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])



read_1 = Reader ('Reader.txt')
#print("read_1.read()", read_1.read())
attributes = read_1.__getstate__()
read_1.close
print(attributes)
print(read_1.__setstate__(attributes))

read_1.close

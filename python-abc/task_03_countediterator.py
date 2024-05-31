class CountedIterator:
    def __init__(self, iter_object, counter=0):
        self.iter_object = iter_object
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        if self.counter <= len(self.iter_object):
            return self.iter_object[self.counter - 1]
        else:
            raise StopIteration

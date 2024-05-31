class CountedIterator:
    def __init__(self, iter_object):
        self.iter_object = iter(iter_object)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        return next(self.iter_object)

class CountedIterator:
    def __init__(self, iter_object):
        self.iter_object = iter(iter_object)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iter_object)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

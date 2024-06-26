from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, item=-1):
        print("Popped [{}] from the list.".format(self[item]))
        popped_item = super().pop(item)
        return popped_item


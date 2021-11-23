nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, nestedlist):
        self.nestedlist = nestedlist

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if len(self.nestedlist[-1]) == 0:
            raise StopIteration
        if len(self.nestedlist[self.counter]) != 0:
            self.cursor = self.nestedlist[self.counter].pop(0)
        else:
            self.counter += 1
            self.cursor = self.nestedlist[self.counter].pop(0)
        return self.cursor


for item in FlatIterator(nested_list):
    print(item)

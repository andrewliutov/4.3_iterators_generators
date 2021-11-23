nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None, [1, 3.5, ['ololo', [True, 100500]]]],
]


class FlatIterator:

    def __init__(self, nestedlist):
        self.nestedlist = nestedlist
        self.flatlist = self.flatten(nestedlist)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.flatlist) == 0:
            raise StopIteration
        else:
            self.cursor = self.flatlist.pop(0)
        return self.cursor

    def flatten(self, nestedlist):
        flatlist = []
        for element in nestedlist:
            if isinstance(element, list):
                for sub_element in self.flatten(element):
                    flatlist.append(sub_element)
            else:
                flatlist.append(element)
        return flatlist


for item in FlatIterator(nested_list):
    print(item)

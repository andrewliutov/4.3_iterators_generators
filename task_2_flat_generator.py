nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(nestedlist):
    for element in nestedlist:
        for sub_element in element:
            yield sub_element


for item in flat_generator(nested_list):
    print(item)

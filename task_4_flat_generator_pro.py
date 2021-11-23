nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None, [1, 3.5, ['ololo', [True, 100500]]]],
]


def flat_generator(nestedlist):
    for element in nestedlist:
        if isinstance(element, list):
            for sub_element in flat_generator(element):
                yield sub_element
        else:
            yield element


for item in flat_generator(nested_list):
    print(item)

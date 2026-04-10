import itertools
items = ['a', 'b']
cyclic_iterator = itertools.cycle(items)
result = list(itertools.islice(cyclic_iterator, 6))
print(result)

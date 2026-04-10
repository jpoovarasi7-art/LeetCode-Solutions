import itertools
colors = ['red', 'green', 'blue']
result = list(itertools.product(colors, repeat=2))
for combo in result:
    print(combo)

import itertools
str1="123"
items=list(str1)
result=list(itertools.permutations(items,2))
print(result)

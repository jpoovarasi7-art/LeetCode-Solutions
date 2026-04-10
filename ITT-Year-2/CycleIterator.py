from itertools import cycle
counter = 0
for item in cycle([1, 2, 3]):
   print(item, end=" ")
   counter += 1
   if counter >8:
      break

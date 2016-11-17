x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
zipped = zip(x,y)
print(*zipped)
x2, y2 = zip(*zip(x, y))
print(list(x2))
print(list(y2))

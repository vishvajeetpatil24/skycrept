str = "Hello world"
raw_str = list(map(ord,str))
data = list(zip(*[iter(raw_str)]*len(raw_str)))
print(data)
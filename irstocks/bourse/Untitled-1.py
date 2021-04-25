l = ["1","1","1","2","3","4","5","6", "3", "2"]
conter = l.count("1")
print(l.count("1"))
print(conter)
result = []
for item in l:
    if l.count(item) == 2:
        result.append(item)

myset = set(result)
result = list(myset)

print(result)
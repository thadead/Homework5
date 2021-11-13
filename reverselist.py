lst = [1,2,3,4,5,6]
for i in range(len(lst)):
    lst.insert(i, lst.pop())
print(lst)
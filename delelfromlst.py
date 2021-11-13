lst = [1,2,3,4,5,6,7,8]
k = int(input())
for i in range(k+1, len(lst)):
    lst[i - 1] = lst[i]
lst.pop()
print(lst)

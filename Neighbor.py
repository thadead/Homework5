lst = [1,2,23,4,55,66,44,33,23,45,21,2,0]
sum = 0
for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        print(lst[i])
        sum += 1
print(sum)

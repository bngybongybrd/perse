arr = [10]*5
give = []
for i in range(5):
    sweets = int(input())
    give.append(sweets)
for i in range(len(arr)):
    arr[i] -= give[i]
    arr[i] += give[i-1]
'''
temp = give[-1]
give.pop()
give.insert(0, temp)
for i in range(len(arr)):
    arr[i] += give[i]
'''
print(max(arr))

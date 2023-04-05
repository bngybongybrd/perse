arr = [int(i) for i in input().split()]
sum = 0

for i in range(len(arr)):
    if i == 0 and arr[i] != 13:
        sum += arr[i]
    elif arr[i] == 13:
        continue
    elif arr[i-1] == 13:
        continue
    else:
        sum += arr[i]

print(sum)

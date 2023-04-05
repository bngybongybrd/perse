ans = int(input())
low = 0
high = 101
x = 0
count = 1

while True:
    x = (low+high)//2
    if x == ans:
        print(count)
        break
    else:
        if ans > x:
            low = x
        else:
            high = x
    count += 1

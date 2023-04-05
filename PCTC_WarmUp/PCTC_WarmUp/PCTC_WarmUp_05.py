num = int(input())
count = 1
total = num
if num == 0:
    print(1)
else:
    while total != 0:
        num = int(input())
        total += num
        count += 1
    print(count)
    

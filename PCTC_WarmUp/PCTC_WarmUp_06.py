over100 = 0
total = 0
while True:
    num = int(input())
    if num < 0:
        break
    if num > 100:
        over100 += 1
    total += num
print(total)
print(over100)
    

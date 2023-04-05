num = int(input())
remainder = num%8
mul = num//8
if num <= 7:
    print(8)
elif remainder <= 4:
    print(mul*8)
else:
    print((mul+1)*8)

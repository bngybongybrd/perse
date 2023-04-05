n = float(input())
count = 0

while True:
    if 2**count > n:
        print(2**count)
        break
    count += 1

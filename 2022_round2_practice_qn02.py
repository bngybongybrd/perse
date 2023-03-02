w = input()
n = int(input())
s = len(w)

if s > n:
    print("MORE")
elif s < n:
    print("FEWER")
else:
    print("MATCH")

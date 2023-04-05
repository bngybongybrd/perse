x = int(input())
y = int(input())
n = int(input())
old = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = []
for i in range(n):
    while len(old) > 0:
        count = 0
        while len(old) > 0:
            if count < x:
                new.insert(0, old[0])
                old.pop(0)
                count += 1
            else:
                break
        count = 0
        while len(old) > 0:
            if count < y:
                new.insert(0, old[-1])
                old.pop()
                count += 1
            else:
                break
    new, old = [], new[::]
        
print(old[0])
        
'''
x = 9
y = any other number
n = 2
1:
987654321
2:
123456789
Ans: 1

x = 3
y = 9
n = 2
1:
456789321
2:
789321654
Ans: 7

x = 4
y = 2
n = 2
1:
765894321
2:
349218567
Ans: 3
'''

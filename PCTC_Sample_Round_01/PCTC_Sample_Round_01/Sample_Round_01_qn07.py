arr = []
for i in range(5):
    name = input()
    arr.append(name)
placing = arr.index('Ellie') + 1
if placing == 1:
    print('1st')
elif placing == 2:
    print('2nd')
elif placing == 3:
    print('3rd')
else:
    print(str(placing) + 'th')

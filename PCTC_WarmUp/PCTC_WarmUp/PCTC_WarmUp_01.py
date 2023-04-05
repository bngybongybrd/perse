total = []
for i in range(5):
    money = int(input())
    total.append(money)
subtract = int(input())-1
total.pop(subtract)
print('$'+str(sum(total)))

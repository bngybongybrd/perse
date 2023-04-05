price = float(input())
percent = int(input())/100
change = price*(percent)
if price < 10 and (price-change) >= 1:
    price -= change
elif price >= 10 and (price+change) < 100:
    price += change
print('${:.2f}'.format(price))

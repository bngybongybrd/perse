ice_cream = input()
i = 0
c = 0
m = 0
w = 0
criteria = {
    'I': 2,
    'M': 1,
    'C': 3,
    'W': 1,
}
for x in ice_cream:
    criteria[x] -= 1
for items in criteria:
    if criteria[items] != 0:
        print(items)

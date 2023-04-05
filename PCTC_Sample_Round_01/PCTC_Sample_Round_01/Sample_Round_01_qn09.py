symbol = input()
sequence = '<+&>'
dance = ''
symbol_count = 0
while len(dance) < 8:
    for i in sequence:
        if i == symbol:
            if symbol_count == 2:
                break
            else:
                symbol_count += 1
                dance += i
        elif 1 <= symbol_count < 3:
            dance += i
print(dance)

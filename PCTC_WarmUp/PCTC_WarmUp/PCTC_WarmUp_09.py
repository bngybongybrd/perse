string = input()
front, back = string.split('me')
if len(front) == 0 or len(back) == 0:
    print(-1)
else:
    print(front[-1] + back[0])

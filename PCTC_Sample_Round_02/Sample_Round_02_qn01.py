x = float(input())
y = float(input())
z = float(input())

arr = [x, y, z]
if x == y or x == z or y == z or x == y == z:
    print("WOBBLY")
elif arr == sorted(arr):
    print("UP")
elif arr == sorted(arr, reverse=True):
    print("DOWN")
else:
    print("WOBBLY")

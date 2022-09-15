while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    if x > y: x, y = y, x
    if y > z: y, z = z, y 
    other_squared = (x **2 + y**2)
    z_squared = z ** 2
    if other_squared == z_squared:
        print("right")
    else: print("wrong")
day, night, end = map(int, input().split())
speed = day - night

print((end - night -1) // (day - night)+1)
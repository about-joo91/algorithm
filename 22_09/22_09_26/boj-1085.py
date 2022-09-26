x, y, w, h = map(int, input().split())

distance_x = min(abs(w - x), abs(0 - x))
distance_y = min(abs(h - y), abs(0 - y))
print(min(distance_x, distance_y))
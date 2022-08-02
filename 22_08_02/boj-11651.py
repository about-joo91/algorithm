iter_num = int(input())
coordinates = []
for _ in range(iter_num):
    coordinates.append(list(map(int,input().split())))
coordinates = sorted(coordinates, key = lambda x: (x[1] , x[0]))
for coordinate in coordinates:
    print(' '.join(map(str, coordinate)))
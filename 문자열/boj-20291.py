import sys
input = sys.stdin.readline

N = int(input().rstrip())
extension_map = {}
for _ in range(N):
    file_name = input().rstrip()
    extension = file_name.split('.')[-1]
    if extension in extension_map:
        extension_map[extension] +=1
    else:
        extension_map[extension] = 1


for key in sorted(extension_map.keys()):
    print(key, extension_map[key])

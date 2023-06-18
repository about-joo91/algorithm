N = int(input())
visited_order = list(map(int, input().split()))
tree = [[ ] for _ in range(N)]

def make_binary_tree(arr, depth):
	mid = len(arr)//2
	tree[depth].append(arr[mid])
	if len(arr) == 1: return
	make_binary_tree(arr[:mid], depth+1)
	make_binary_tree(arr[mid+1:], depth+1)

make_binary_tree(visited_order, 0)
for nodes in tree:
	print(*nodes)

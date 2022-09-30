import sys
input = sys.stdin.readline

height_of_triangle = int(input().rstrip())
triangle = [list(map(int, input().rstrip().split())) for _ in range(height_of_triangle)]
triangle_sums = [[0] * len(triangle[i]) for i in range(height_of_triangle)]
triangle_sums[0][0] = triangle[0][0]

for row_index in range(height_of_triangle-1):
    for col_index in range(len(triangle_sums[row_index])):
        triangle_sums[row_index+1][col_index] = max(triangle_sums[row_index+1][col_index], triangle_sums[row_index][col_index]+triangle[row_index+1][col_index])
        triangle_sums[row_index+1][col_index+1] = max(triangle_sums[row_index+1][col_index+1], triangle_sums[row_index][col_index] + triangle[row_index+1][col_index+1])
print(max(triangle_sums[height_of_triangle-1]))
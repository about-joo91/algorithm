import sys
input = sys.stdin.readline

def get_sum_of_number(str):
    sum_of_num = 0
    for char in str:
        if char.isdigit():
            sum_of_num += int(char)
    return sum_of_num


if __name__ == '__main__':
    N = int(input().rstrip())
    serial_numbers = [list(input().rstrip()) for _ in range(N)]

    serial_numbers.sort(key= lambda x: (len(x), get_sum_of_number(x), x))


    for serial_number in serial_numbers:
        print("".join(serial_number))
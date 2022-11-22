import re

origin_word = re.sub('[0-9]', "", input())
check_word = input()

print(int(check_word in origin_word))
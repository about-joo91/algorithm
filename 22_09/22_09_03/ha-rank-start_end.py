# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
if not match: print("(-1, -1)")
while match:
    print('({0}, {1})'.format(match.start(), match.end()-1))
    match = pattern.search(string, match.start()+1)


fir_s = input()
sec_s = input()

has_same = False
for i in range(len(fir_s)):
    if fir_s[i:i+len(sec_s)] == sec_s:
        has_same = True
        print(f"({i}, {i+len(sec_s)-1})")

if not has_same: print("(-1, -1)")
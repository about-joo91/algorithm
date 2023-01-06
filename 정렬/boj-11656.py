S = input()

post_fixes = []


for i in range(len(S)):
    post_fixes.append(S[i:len(S)])
    
post_fixes.sort()

for post_fix in post_fixes:
    print(post_fix)
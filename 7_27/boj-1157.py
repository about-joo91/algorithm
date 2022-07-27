most_alpha = input().upper()
check_num_alpha = {}

for alpha in most_alpha:
    if alpha in check_num_alpha:
        check_num_alpha[alpha] +=1
    else:
        check_num_alpha[alpha] = 1
max_num = max(map(lambda x: x[1] , check_num_alpha.items()))
max_alphas = list(filter(lambda x : x[1] == max_num, check_num_alpha.items()))
if len(max_alphas) > 1:
    print('?')
else:
    print(max_alphas[0][0])
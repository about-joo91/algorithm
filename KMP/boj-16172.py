def get_failure_table(check_word):
    length = len(check_word)
    failure_table = [0] * length
    
    j = 0
    for i in range(1, length):
        while j > 0 and check_word[i] != check_word[j]:
            j = failure_table[j-1]
        if check_word[i] == check_word[j]:
            j+=1
            failure_table[i] = j
    return failure_table


def is_sub_string(origin_word, check_word):
    j = 0
    for i in range(len(origin_word)):
        if "0"<= origin_word[i] <= "9":
            continue
        while j > 0 and origin_word[i] != check_word[j]:
            j = failure_table[j-1]
        if origin_word[i] == check_word[j]:
            j+=1
        if j == len(check_word): return True
    return False

origin_word = input()
check_word = input()


failure_table = get_failure_table(check_word)

print(int(is_sub_string(origin_word, check_word)))
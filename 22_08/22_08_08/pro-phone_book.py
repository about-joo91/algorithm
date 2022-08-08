def solution(phone_book):
    phone_nums_by_len = {}
    phone_book.sort()
    for phone_num in phone_book:
        for key in phone_nums_by_len.keys():
            if phone_num[:key] in phone_nums_by_len[key]:
                return False
        if len(phone_num) in phone_nums_by_len:
            phone_nums_by_len[len(phone_num)].append(phone_num)
        else:
            phone_nums_by_len[len(phone_num)] = [phone_num]
    return True
        # 딕셔너리에 키값을 넣을 때  길이에 따라 분배한다.
        # 넣다가 같은 값이 있으면 false를 반환한다.
        

print(solution(["119", "97674223", "1195524421"]))
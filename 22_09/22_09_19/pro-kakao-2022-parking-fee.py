import math

def solution(fees, records):
    
    basic_time, basic_fee, fee_cond, fee = fees
    last_hour = 23*60 + 59
    record_map = {}
    answer_map = {}
    answer = []
    
    for record in records:
        time, car_num, parking_type = record.split(' ')
        time_to_minute = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        if parking_type == "IN":
            if car_num in record_map:
                record_map[car_num].append((time_to_minute, 'IN'))
            else: record_map[car_num] = [(time_to_minute, 'IN')]
        else:
            record_map[car_num].append((time_to_minute, 'OUT'))
    
    
    for idx, key in enumerate(record_map.keys()):
        stack = []
        answer_map[key] = 0
        
        while record_map[key]:

            cur_time, cur_type = record_map[key].pop()
            if not stack and cur_type == "IN":
                time_diff = last_hour - cur_time
            elif cur_type == "OUT":
                stack.append(cur_time)
                continue
            else:
                time_diff = stack.pop() - cur_time
            answer_map[key] += time_diff
            
    for key in sorted(answer_map):
        time = answer_map[key]
        if time <= basic_time:
            answer.append(basic_fee)
        else:
            cur_fee = basic_fee + math.ceil((time - basic_time)/fee_cond) * int(fee)
            answer.append(cur_fee)
    
    return answer
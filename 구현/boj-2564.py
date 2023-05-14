def location_to_distance(loc_type, loc_num):
    match loc_type:
        case 1:
            return loc_num
        case 2:
            return WIDTH + HEIGHT + (WIDTH - loc_num)
        case 3:
            return WIDTH * 2 + HEIGHT + (HEIGHT - loc_num)
        case 4:
            return WIDTH + loc_num


WIDTH, HEIGHT = map(int, input().split())
shop_count = int(input())
shop_locations = [list(map(int, input().split())) for _ in range(shop_count)]
donggeun_loc = list(map(int, input().split()))
donggeun_dist = location_to_distance(*donggeun_loc)

answer = 0
for shop_location in shop_locations:
    shop_dist = location_to_distance(*shop_location)
    clock_side_dist = abs(donggeun_dist - shop_dist)
    opposite_clock_side_dist = (WIDTH + HEIGHT) * 2 - clock_side_dist

    answer += min(clock_side_dist, opposite_clock_side_dist)

print(answer)
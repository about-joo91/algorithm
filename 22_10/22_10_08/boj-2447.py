def draw_stars_and_holes(n):
    if n == 1:
        return ['*']

    stars=draw_stars_and_holes(n//3)
    cur_stars = []
    
    for star in stars:
        cur_stars.append(star*3)
    for star in stars:
        cur_stars.append(star+' '*(n//3)+star)
    for star in stars:
        cur_stars.append(star*3)

    return cur_stars

N=int(input())
print('\n'.join(draw_stars_and_holes(N)))
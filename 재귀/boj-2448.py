def make_triangle(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    
    stars = make_triangle(n//2)
    cur_stars = []

    for star in stars:
        cur_stars.append(" "* (n//2) + star + " " * (n//2))
    
    for star in stars:
        cur_stars.append(star + " " + star)

    return cur_stars

N = 24

print("\n".join(make_triangle(N)))
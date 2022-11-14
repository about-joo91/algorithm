count = 1
while True:
    cur_input = input()
    if cur_input == "0":
        break
    R, W, L = map(int, cur_input.split())
    
    if (W**2 + L**2) ** (1/2) <= 2*R:
        print(f"Pizza {count} fits on the table.")
    else: print(f"Pizza {count} does not fit on the table.")
        
    count +=1
string = input()
Kevin = 0
Stuart = 0

vowels = ['A', 'E', 'I', 'O', 'U']
for idx, alpha in enumerate(string):
    if alpha in vowels:
        Kevin += len(string) - idx
    else:
        Stuart += len(string)- idx
if Stuart > Kevin:
    print(f"Stuart {Stuart}")
elif Stuart < Kevin:
    print(f"Kevin {Kevin}")
else:
    print("Draw")
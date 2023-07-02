N = int(input())
chongs = set(["ChongChong"])

def is_in_chongs(person1, person2):
    return person1 in chongs or person2 in chongs
for _ in range(N):
    person1, person2 = input().split()

    if is_in_chongs(person1, person2):
        chongs.add(person1)
        chongs.add(person2)

print(len(chongs))
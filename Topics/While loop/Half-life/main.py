atoms = float(input())
final_atoms = int(input())
half_life = 12
count = 0
while atoms >= final_atoms:
    atoms /= 2
    count += 1
print(count * half_life)

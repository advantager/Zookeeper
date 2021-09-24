# put your python code here
desks = 0
for _ in range(3):
    group = abs(int(input()))
    desks += (group // 2) + (group % 2)
print(desks)

# put your code here
count = 0
total = 0
number = 0
stop_number = 55
while number != stop_number:
    number = int(input())
    if number != stop_number:
        count += 1
        total += number
print(count)
print(total)
print(round(total / count))

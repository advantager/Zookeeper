number = int(input())
count = 1
factorial = 1
while count <= number:
    factorial *= count
    count += 1
print(factorial)

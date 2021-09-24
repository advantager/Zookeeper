# put your python code here
input_number = int(input())
digit_sum = 0
for i in range(3):
    digit_sum += (input_number // 10 ** i) % 10
print(digit_sum)

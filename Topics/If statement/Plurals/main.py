number = int(input())
word = input()
s = 's'
# write a condition for plurals
if abs(number) != 1:
    word += s
print(number, word)

# Save the input in this variable
ticket = input()

# Add up the digits for each half
a = int(ticket[0])
b = int(ticket[1])
c = int(ticket[2])
d = int(ticket[-1])
e = int(ticket[-2])
f = int(ticket[-3])

# Thanks to you, this code will work
if (a + b + c) == (d + e + f):
    print("Lucky")
else:
    print("Ordinary")

binary = input("Enter a binary number: ")
n = 0
power = 0
for i in reversed(binary):
    if i == '1':
        n += 2 ** power
    power += 1
print("Integer value is:", n)
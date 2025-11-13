# Entering the amount
a = int(input("Enter the amount to withdraw: "))

# Calculating number of notes
b = a // 100        # 100 rupee notes
a = a % 100
c = a // 50         # 50 rupee notes
a = a % 50
d = a // 10         # 10 rupee notes
a = a % 10          # Remaining amount (if any)

# Display results
print("100 rupee notes:", b)
print("50 rupee notes:", c)
print("10 rupee notes:", d)

if a != 0:
    print("Remaining amount that cannot be dispensed:", a)

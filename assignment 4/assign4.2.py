s = input("Enter a string: ")

digits = []  
for ch in s:
    if ch.isdigit():        
        digits.append(int(ch))   
if len(digits) == 0:
    print("No digits found in the string.")
else:
    total = sum(digits)
    avg = total / len(digits)
    maximum = max(digits)
    minimum = min(digits)

    print("Sum of digits:", total)
    print("Average:", avg)
    print("Maximum digit:", maximum)
    print("Minimum digit:", minimum)

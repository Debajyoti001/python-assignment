s = input("Enter a string: ")
i = int(input("Enter remove charecter(number position): "))
s = s[:i-1] + s[i:]
print("String after removing the character:", s)

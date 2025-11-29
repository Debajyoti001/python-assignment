s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = ""
i = 0              
j = len(s2) - 1       
while i < len(s1) and j >= 0:
    result += s1[i]
    result += s2[j]
    i += 1
    j -= 1
while i < len(s1):
    result += s1[i]
    i += 1 
while j >= 0:
    result += s2[j]
    j -= 1
print("Result:", result)


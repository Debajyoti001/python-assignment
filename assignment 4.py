s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = ""
i = 0                 # front index for s1
j = len(s2) - 1       # back index for s2

# take characters alternately
while i < len(s1) and j >= 0:
    result += s1[i]
    result += s2[j]
    i += 1
    j -= 1

# if s1 has leftover characters (keep their order)
while i < len(s1):
    result += s1[i]
    i += 1

# if s2 has leftover characters (add them in reverse order)
while j >= 0:
    result += s2[j]
    j -= 1

print("Result:", result)

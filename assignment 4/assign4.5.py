s = input("Enter words separated by space: ").split()

groups = {}

for w in s:
    key = ''.join(sorted(w))
    if key in groups:
        groups[key].append(w)
    else:
        groups[key] = [w]

result = list(groups.values())

print(result)
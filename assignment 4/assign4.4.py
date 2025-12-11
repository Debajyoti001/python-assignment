# 12 3 45 9 10 2 100

s = input("Enter space separated numbers: ")
n = s.split()

# Function to calculate digit sum
def digit_sum(n):
    return sum(int(d) for d in n)

long = []
current = [n[0]]

for i in range(1, len(n)):
    if digit_sum(n[i]) > digit_sum(n[i-1]):
        current.append(n[i])
    else:
        if len(current) > len(long):
            long = current
        current = [n[i]]

if len(current) > len(long):
    long = current

print("Longest sequence:", long)
print("Length:", len(long))
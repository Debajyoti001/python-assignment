n = int(input("How many numbers: "))
k = int(input("Enter the value of k: "))

skip = 0   # to skip the first multiple

for i in range(n):
    num = int(input("Enter number: "))
    if num % k == 0:
        if skip == 0:
            skip = 1     # skip the first multiple
        else:
            print(num, end=" ")

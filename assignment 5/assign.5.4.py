nums = [1, 2, 3, 4, 5]
k = 3
result = []

for i in range(len(nums) - k + 1):
    window = nums[i:i+k]
    avg = sum(window) / k
    var = sum((x - avg) ** 2 for x in window) / k
    result.append((avg, var))

print(result)
n = int(input())
nums = []
for i in range(1, n + 1):
    nums.append(i)
cock = nums


for j in range(1, len(nums) + 1):
    for i in range(len(nums)):
        nums[i] = (i + 1) * j
    print(" ".join(nums))
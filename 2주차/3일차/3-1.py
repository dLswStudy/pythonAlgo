nums = [int(input()) for _ in range(9)]
nums.sort()
toRemove = sum(nums) - 100
for i in range(8):
    for j in range(i+1,9):
        if nums[i]+nums[j] == toRemove:
            a = nums[i]
            b = nums[j]
nums.remove(a)
nums.remove(b)
for num in nums:
    print(num)
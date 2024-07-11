with open('numbers.txt', 'r') as file:
    nums = list(map(int, [i for i in file.readlines()]))
d = [abs(sum(nums)/len(nums) - num) for num in nums]
answer = 0
for num in nums:
    answer += abs(num - nums[d.index(min(d))])
print(answer)
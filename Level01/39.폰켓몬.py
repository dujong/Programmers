def solution(nums):
    answer = len(nums) / 2
    if answer > len(set(nums)):
        return len(set(nums))
    else:
        return int(answer)

nums = [3,3,3,2,2,4]
result = solution(nums)
print(result)
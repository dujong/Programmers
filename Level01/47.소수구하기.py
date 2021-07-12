from itertools import combinations

def solution(nums):
    nums = sorted(nums)
    boy = sum(nums[-3:])
    n = boy
    a = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2,n-1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    answer = 0
    A = list(combinations(nums, 3))

    for i in A:
        if a[i[0]+i[1]+i[2]]:
            answer +=1
    
    return answer

nums = [1,2,7,6,4]	
print(solution(nums))

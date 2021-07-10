def solution(N, stages):
    answer = {}
    num = len(stages)

    for i in range(1, N+1):
        if num != 0:
            c = stages.count(i)
            answer[i] = c/num
            num -= c
        
        else:
            answer[i] = 0
            
    return sorted(answer, key = lambda x: answer[x], reverse=True)

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))


def solution(d, budget):
    d.sort()
    count = 0
    for i in range(len(d)):
        if budget - d[i] >= 0:
            budget -= d[i]
            count += 1
        else:
            return count
    return count
    

d = [2,2,3,3]
budget = 10

result = solution(d, budget)
print(result)
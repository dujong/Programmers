def solution(n, costs):
    answer = 0
    u = [False] * n
    costs.sort(key=lambda x : x[2])
    
    for i1, i2, cost in costs:
        
        if u[i1] == False or u[i2] == False:
            answer += cost
            u[i1] = True
            u[i2] = True
            
        if sum(u) == n:
            return answer
    
n = 6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
costs.sort(key=lambda x : x[2])
print(costs)
print(solution(n, costs))

# n개의 False 리스트를 만든 후 costs를 정렬하여 연결되는 부분을 True로
# 앞과 뒤중에 False가 있으면 cost를 더하고 연결

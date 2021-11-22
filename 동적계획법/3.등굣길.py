def solution(m, n, puddles):
    dp = [[1]*m for x in range(n)]
    
    for x, y in puddles:
        dp[x-1][y-1] = 0
        
    
    answer = 0
    return dp

print(solution(4, 3, [[2,2]]))
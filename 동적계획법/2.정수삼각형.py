import copy
def solution(triangle):
    answer = copy.deepcopy(triangle)
    
    for i in range(len(triangle)-1):
        for j in range(i+1):
            
            if answer[i+1][j] > triangle[i+1][j]:
                answer[i+1][j] = triangle[i+1][j] + max(answer[i][j-1], answer[i][j])
                
            else:
                answer[i+1][j] += answer[i][j]
                
            answer[i+1][j+1] += answer[i][j]

    return max(max(answer))

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	

print(solution(triangle))

    
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        com = sorted(array[i-1:j])
        answer.append(com[k-1])
        
    return answer
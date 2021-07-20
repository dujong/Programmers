def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        mid = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            mid.append(temp)
        answer.append(mid)

    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]	
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))
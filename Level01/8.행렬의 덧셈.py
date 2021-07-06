def solution(arr1, arr2):
    result = list()
    
    for i in range(len(arr1)):
        arr3 = list()
        for j in range(len(arr1[i])):
            arr3.append(arr1[i][j] + arr2[i][j])
        result.append(arr3)
    return result

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

result = solution(arr1, arr2)
print(result)

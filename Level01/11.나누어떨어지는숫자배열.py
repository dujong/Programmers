def solution(arr, divisor):
    answer = list()

    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    
    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)

arr = [3,2,6]
divisor	= 10
arr = solution(arr, divisor)
print(arr)
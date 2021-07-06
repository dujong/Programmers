def solution(x):
    score = sum(list(map(int, str(x))))
    if x % score == 0:
        answer = True
    else:
        answer = False

    return answer

arr = 11
arr = solution(arr)
print(arr)
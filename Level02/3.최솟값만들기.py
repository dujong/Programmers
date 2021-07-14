def solution(A,B):
    siz = len(A)
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(siz):
        answer = answer + (A[0] * B[0])
        A.pop(0)
        B.pop(0)
    return answer

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A,B))
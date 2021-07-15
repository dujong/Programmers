# def solution(n):
#     answer = 0
#     a = list(range(1, n+1))
    
#     for i in range(len(a)):
#         ad = i
#         if a[i] == n:
#             answer += 1
#             break
#         for j in range(i+1, len(a)):
#             ad += j
#             if ad == n:
#                 answer += 1
#             elif ad > n:
#                 break
#     return answer

def solution(n):
    answer = 0
    for i in range(1, n+1):
        s = 0
        while s < n:
            s += i
            i += 1
        if s == n:
            answer += 1

    return answer

n = 15
print(solution(n))
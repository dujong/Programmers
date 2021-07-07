def solution(n):
    n1 = n**0.5
    if n1 % 1 == 0.0:
        return int((n1+1)**2)
    else:
        return -1

arr = 3
arr1 = solution(arr)
print(arr1)
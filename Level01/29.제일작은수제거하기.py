def solution(arr):
    if len(arr) == 1:
        return list([-1])
    arr.remove(min(arr))
    return arr

arr = [10]
arr1 = solution(arr)
print(arr1)
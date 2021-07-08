def solution1(n):
    divisorsList = []

    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            divisorsList.append(i)
            if i**2 != n:
                divisorsList.append(n // i)
    
    return divisorsList


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        value = solution1(i)
        if len(value) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

left = 24
right = 27
result = solution(left, right)
print(result)
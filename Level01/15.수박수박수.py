def solution(n):
    subak = ['수', '박']
    result = []
    for i in range(n):
        result.append(subak[i%2])
    return ''.join(result)

n = 5
n = solution(n)
print(n)
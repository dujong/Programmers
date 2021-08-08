def solution(citations):
    citations = sorted(citations)
    l = len(citations)

    for k, v in enumerate(citations):
        if v >= l-k:
            return l-k

    return 0


citations = [3, 0, 6, 1, 5]
print(solution(citations))

import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        count +=1
        temp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, temp)

        if scoville[0] >= K:
            return count

    if scoville[0] >= K:
        return count
    else:
        return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))
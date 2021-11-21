import heapq

def solution(jobs):
    answer, finish = 0, 0
    time, now = -1, 0
    possible = []
    
    while finish < len(jobs):
        
        for j in jobs:
            if time < j[0] <= now:
                heapq.heappush(possible, [j[1], j[0]])
        
        if len(possible) > 0:
            cur = heapq.heappop(possible)
            time = now
            now += cur[0]
            answer += (now - cur[1])
            finish += 1
            
        else:
            now += 1
    
    return answer // len(jobs)
import heapq

def solution(operations):
    answer = []
    heapq.heapify(answer)
    
    for x in operations:
        if 'I' in x:
            heapq.heappush(answer, int(x.split(' ')[1]))
            
        elif '-' in x:
            if len(answer) != 0:
                answer.pop(0)
            
        else:
            if len(answer) != 0:
                answer.pop(-1)
            
    if not answer:
        return [0,0]
    
    else:
        return [max(answer), min(answer)]
def solution(people, limit):
    cnt = 0
    answer = []
    people = sorted(people, reverse=True)
    
    for i in people:
        if not answer:
            answer.append(i)
            
            while sum(answer)+people[-1] <= limit:
                answer.append(people.pop())
                
            answer = []
            cnt += 1
            
    return cnt
            
        
            
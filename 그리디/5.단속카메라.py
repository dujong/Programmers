def solution(routes):
    i=0; j=0; answer=1
    
    routes.sort(key=lambda x:x[0])
    
    i, j = routes.pop(0)
    
    for x in routes:
        if j >= x[0] and j < x[1]:
            i = x[0]
            
        elif j >= x[0] and j >= x[1]:
            i = x[0]
            j = x[1]
            
        else:
            i = x[0]
            j = x[1]
            answer += 1
    
    return answer
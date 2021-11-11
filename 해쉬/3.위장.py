def solution(clothes):
    d = {}
    
    for name, cate in clothes:
        d[cate] = d.get(cate, 0) + 1
        
    answer = 1
    
    for k, v in d.items():
        answer = answer * (v+1)
        
    return answer - 1
def solution(s):
    s = list(s)
    l = len(s)
    k = int(l/2)
    
    if l % 2 == 0:
        answer = s[k-1] + s[k]
    else:
        answer = s[k]
    
    return answer

s = "qwer"	
s1 = solution(s)
print(s1)

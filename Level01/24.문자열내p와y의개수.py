import re
def solution(s):
    S = len(re.sub('[^p|P]', '', s))
    Y = len(re.sub('[^y|Y]', '', s))
    
    if S == Y:
        return True
    else:
        return False

s = "pPoooyY"
s1 = solution(s)
print(s1)
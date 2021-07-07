import re
def solution(s):
    n = int(re.sub('[^0-9]', '', s))
    if s[0] == '-':
        n *= -1
    return n

s = '1234'
s1 = solution(s)
print(s1)
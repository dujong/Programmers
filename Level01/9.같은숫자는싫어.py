import re

def solution(s):
    word1 = sorted(re.sub('[^a-z]', '',  s), reverse=True)
    word2 = sorted(re.sub('[^A-Z]', '', s), reverse=True)
    result = word1 + word2
    return ''.join(result)

s = "Zbcdefg"
s = solution(s)
print(s)

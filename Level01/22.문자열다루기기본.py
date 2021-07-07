import re

def solution(s):
    answer = re.sub('[0-9]', '', s)
    if answer == '' and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False

s = '12345'
s = solution(s)
print(s)
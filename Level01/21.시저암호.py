def solution(s, n):
    # 분리를 한다음, 소문자 대문자인지 확인!!하고 맞을 때만 +
    # 122 넘은 것이 있는지? 90을 넘은 것이 있는지 확인하고 나눠주기!
    s1 = list(map(ord, s))
    for i in range(len(s1)):
        if s1[i] < 50:
            s1[i] = s1[i]
        elif s1[i] >= 97 and s1[i] <= 122:
            s1[i] = s1[i] + n
            if s1[i] > 122:
                s1[i] = s1[i] % 122 + 96
        elif s1[i] >= 65 and s1[i] <= 90:
            s1[i] = s1[i] + n
            if s1[i] > 90:
                s1[i] = s1[i] % 90 + 64

    s2 = ''.join(list(map(chr, s1)))
    return s2

def solution123(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)


s = "a   b"
n = 4
s = solution123(s, n)
print(s)
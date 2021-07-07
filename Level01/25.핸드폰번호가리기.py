def solution(phone_number):
    answer = (len(phone_number)-4) * '*' + phone_number[-4:]
    return answer

p = "01033334444"
q = solution(p)
print(q)
def solution(seoul):
    c = seoul.index('Kim')
    result = "김서방은 " + str(c) + " 에 있다"
    return result

seoul = ["Jane", "Kim"]
seoul = solution(seoul)
print(seoul)
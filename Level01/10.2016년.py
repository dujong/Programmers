def solution(a, b):
    count = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    result = 0

    for i in range(a-1):
        result += count[i]
    result = result + b
    print(result%7)
    result = day[result%7 -1]
    return result

a = 5
b = 24
c = solution(a,b)
print(c)
def solution(s):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8' , '9']
    answer = 0

    for i in number:
        print(i)
        if s.find(i) != i:
            s = s.replace(i, n[number.index(i)])
        
    return s

s = "one4seveneight"

print(solution(s))
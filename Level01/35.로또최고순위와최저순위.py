def solution(lottos, win_nums):
    ranking = [6,6,5,4,3,2,1]
    counts = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            counts += 1
        elif i == 0:
            zero += 1
    return list([ranking[counts+zero], ranking[counts]])

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

result = solution(lottos, win_nums)
print(result)
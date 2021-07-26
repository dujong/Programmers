def solution(clothes):
    clothes_num = {}
    for i in clothes:
        if i[1] in clothes_num:
            clothes_num[i[1]] += 1
        else:
            clothes_num[i[1]] = 1

    cnt = 1
    
    for i in clothes_num.values():
        cnt *= (i+1)
    return cnt - 1

clothes = [["crowmask", "a"], ["bluesunglasses", "b"], ["smoky_makeup", "c"], ["bb", "a"], ["qwe", "b"] ,["123", "b"]]
print(solution(clothes))
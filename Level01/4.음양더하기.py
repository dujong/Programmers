def solution(absolutes, signs):
    result = 0
    for i in range(len(signs)):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]

    return result

absolutes = [1,2,3]
signs = [False,False,True]
result = solution(absolutes, signs)
print(result)
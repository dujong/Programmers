def solution(n, arr1, arr2):
    answer = list()

    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1' , '#')
        a12 = a12.replace('0' , ' ')
        answer.append(a12)
    return answer
        
    
    # for i in range(n):
    #     arr1[i] = bin(arr1[i])[2:]
    #     arr2[i] = bin(arr2[i])[2:]

    #     if len(arr1[i]) != n:
    #         arr1[i] = '0' * (n - len(arr1[i])) + arr1[i]

    #     if len(arr2[i]) != n:
    #         arr2[i] = '0' * (n - len(arr2[i])) + arr2[i]
        
    #     arr1[i] = arr1[i].replace('1', '#')
    #     arr1[i] = arr1[i].replace('0', ' ')
    #     arr2[i] = arr2[i].replace('1', '#')
    #     arr2[i] = arr2[i].replace('0', ' ')

    # for i in range(n):
    #     arr3 = ''
    #     for j in range(n):
    #         if arr1[i][j] == ' ' and arr2[i][j] == ' ':
    #             arr3 = arr3 + ' '
    #         else:
    #             arr3 = arr3 + '#'
    #     answer.append(arr3)

    
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))


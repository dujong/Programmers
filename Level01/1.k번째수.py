import numpy as np

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_ = array[commands[i][0]-1 : commands[i][1]]
        array_ = sorted(array_)
        answer.append(array_[commands[i][2]-1])
    return answer

arr1 = np.array([1, 5, 2, 6, 3, 7, 4])
commands = np.array([[2, 5, 3], [4, 4, 1], [1, 7, 3]])

result = solution(arr1, commands)
print(result)
def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x:(x*4)[:4] , reverse=True)
    answer = ''.join(numbers)
    return answer
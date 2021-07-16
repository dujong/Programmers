def solution(record):
    answer_ = []
    result = {}
    for i in record:
        answer = i.split(' ')
        if answer[0] != 'Leave':
            result[answer[1]] = answer[2]
            
            
    for i in record:
        answer = i.split(' ')
        if answer[0] == 'Enter':
            answer_.append("{}님이 들어왔습니다." .format(result[answer[1]]))
        elif answer[0] == 'Leave':
            answer_.append("{}님이 나갔습니다." .format(result[answer[1]]))
        else:
            pass
    
    return answer_

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


print(solution(record))
def solution(priorities, location):
    cnt = 0
    
    while priorities != []:
        if len(priorities) > 1:
            first = priorities.pop(0)
            location -= 1

            if first >= max(priorities):
                cnt += 1
                if location == -1:
                    return cnt
            else:
                priorities.append(first)
                if location == -1:
                    location = len(priorities) -1 
        else:
            cnt += 1
            return cnt

priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))
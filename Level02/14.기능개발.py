import math
# math.ceil
def solution(progresses, speeds):
    # answer = []

    # for i in range(len(progresses)):
    #     progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])
        
    # for i in range(1, len(progresses)):
    #     if progresses[i] < progresses[i-1]:
    #         progresses[i] = progresses[i-1]

    # for i in range(max(progresses)+1):
    #     if progresses.count(i) !=0 :
    #         answer.append(progresses.count(i))
    # return answer

    answer = []
    time = 0
    count = 0

    while len(progresses) > 0 :
        if progresses[0] + time*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            
            time += 1
    answer.append(count)

    return answer        
progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))
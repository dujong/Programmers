def solution(answers):
    su1 = [1,2,3,4,5]
    su2 = [2,1,2,3,2,4,2,5]
    su3 = [3,3,1,1,2,2,4,4,5,5]
    su1_counts = 0
    su2_counts = 0
    su3_counts = 0


    for i in range(len(answers)):
        if su1[i%5] == answers[i]:
            su1_counts += 1
        
        if su2[i%8] == answers[i]:
            su2_counts += 1

        if su3[i%10] == answers[i]:
            su3_counts += 1
    
    counts = [su1_counts, su2_counts, su3_counts]
    result = list()

    for index, score in enumerate(counts):
        if score == max(counts):
            result.append(index+1)
    
    return result



    
answers1 = [1,2,3,4,5]
answers2 = [1,3,2,4,2]

result1 = solution(answers1)
result2 = solution(answers2)

print(result1)
print(result2)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for a, b in zip(participant, completion):
        if a != b:
            return a
        
    return participant[-1]
    
    

participant = ["mislav", "stanko", "mislav", "ana"]
completion = 	["stanko", "ana", "mislav"]

result = solution(participant, completion)
print(result)
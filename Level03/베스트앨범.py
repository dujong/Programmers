def solution(genres, plays):
    set_genres = set(genres)
    answer = {}
    cnt = 0

    for i in set_genres:
        answer[i] = 0
    
    for i in genres:
        answer[i] += plays[cnt]
        cnt += 1

    # 딕셔너리 생성 완료
    # max key를 구한다
    # 그 key에 맞는 것들을 sort로 모은다
    # 2개씩 묶는다
    # 
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
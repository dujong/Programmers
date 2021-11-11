def solution(genres, plays):
    d = {}
    f = {}
    answer = []
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i], 0) + plays[i]
        f[genres[i]] = f.get(genres[i], []) + [(plays[i], i)]
        
    genres_sort = sorted(d.items(), key = lambda x:x[1], reverse=True)
    
    for gen, totalPlay in genres_sort:
        f[gen] = sorted(f[gen], key = lambda x: (- x[0], x[1]))
        answer += [idx for (play, idx) in f[gen][:2]]
        
    return answer

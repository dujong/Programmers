def solution(board, moves):
    tong = []
    answer = 0
    for i in  moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                tong.append(board[j][i-1])
                board[j][i-1] = 0
                break
     
        if len(tong) >= 2:
            a = tong[len(tong)-2]
            b = tong[len(tong)-1]

            if a == b:
                tong.pop(-1)
                tong.pop(-1)
                answer += 2
        
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,2,4]
print(solution(board, moves))

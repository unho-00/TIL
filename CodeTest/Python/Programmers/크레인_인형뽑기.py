def solution(board, moves):
    stack = []
    answer = 0

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break

        if len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
            answer += 2

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1, 5, 3, 5, 1, 2, 1, 4]))
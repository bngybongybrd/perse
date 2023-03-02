s = int(input())
p = int(input())
c = int(input())
n = int(input())
m = int(str(p))
board = ['r']*p+['_']*(s-p*2)+['b']*p

def do(fi, board):
    # left
    if board[fi] == 'r' and fi+2 <= s:
        if board[fi+1] == '_':
            board[fi], board[fi+1] = board[fi+1], board[fi]
        elif board[fi+2] == '_':
            board[fi], board[fi+2] = board[fi+2], board[fi]
    # right
    elif board[fi] == 'b' and fi-2 >= 0:
        if board[fi-1] == '_':
            board[fi], board[fi-1] = board[fi-1], board[fi]
        elif board[fi-2] == '_':
            board[fi], board[fi-2] = board[fi-2], board[fi]
    return board

for i in range(n):
    count = 0
    for j in range(len(board)):
        if board[j].isalpha():
            count += 1
        if count == m:
            fi = j
            board = do(fi, board)
            break
    count = 0
    for x in range(len(board)-1, -1, -1):
        if board[x].isalpha():
            count += 1
        if count == m:
            bi = x
            board = do(bi, board)
            break
    if i == 0 or i == n-1:
        print(''.join(board))
    m += c
    if m > p:
        m -= p

from collections import deque
a = """5
BBBBG
GRBBB
BBBBB
BBBBB
RRRRR"""

N = int(a.split("\n")[0])
gbr = []

for i in range(1,N+1):
    gbr.append(list(a.split("\n")[i]))

br = [list(map(lambda x : 'R' if x == 'G' else x ,gbr[i])) for i in range(N)]

visited_gbr = [[0]* N for _ in range(N)]
visited_br = [[0]* N for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans_gbr = 0
ans_br = 0

def bfs_gbr(x,y,color):
    global visited_gbr, ans_gbr
    que = deque()
    que.append((x,y))
    while que : 
        x, y = que.popleft()
        visited_gbr[x][y] = 1

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx > N-1 or ny > N-1 or nx < 0 or ny < 0 :
                continue
            if gbr[nx][ny] == color and visited_gbr[nx][ny] == 0 :
                que.append((nx,ny))
    ans_gbr +=1

def bfs_br(x,y,color):
    global visited_br, ans_br
    que = deque()
    que.append((x,y))
    while que : 
        x, y = que.popleft()
        visited_br[x][y] = 1

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx > N-1 or ny > N-1 or nx < 0 or ny < 0 :
                continue
            if br[nx][ny] == color and visited_br[nx][ny] == 0 :
                que.append((nx,ny))
    ans_br +=1


for i in range(N):
    for j in range(N):
        if visited_gbr[i][j] == 0 :
            bfs_gbr(i,j,gbr[i][j])

for i in range(N):
    for j in range(N):
        if visited_br[i][j] == 0 :
            bfs_br(i,j,br[i][j])

print(ans_gbr, ans_br)


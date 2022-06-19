from collections import deque
a = """2 25
1011101110111011101110111
1110111011101110111011101"""

N,M = map(int,a.split("\n")[0].split(" "))
miro = []
results = []


for i in range(1,N+1):
    miro.append(list(map(int,a.split("\n")[i])))

visited = [[0]* M for _ in range(N)]

que = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

que.append(((0,0),1))

def bfs():
    while que : 
        (x,y), d = que.popleft()
        print(x,y,d)
        if y == N-1 and x == M-1 :
            return d
        visited[y][x] = 1
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            nd = d + 1
            if nx > M-1 or ny > N-1 or nx < 0 or ny < 0 :
                continue
            if miro[ny][nx] == 1 and visited[ny][nx] == 0 :
                que.append(((nx,ny), nd))

print(bfs())
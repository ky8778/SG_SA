def numbering(i, j, cnt):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    queue = [[i, j]]
    edge_lst = []

    while queue:
        lst = queue.pop(0)
        y = lst[0]
        x = lst[1]
        field[y][x] = cnt
        for dir in range(4):
            if 0 <= y+dy[dir] <= N-1 and 0 <= x+dx[dir] <= N-1:
                if field[y+dy[dir]][x+dx[dir]] == 1:
                    queue.append([y+dy[dir], x+dx[dir]])
                elif field[y+dy[dir]][x+dx[dir]] == 0:
                    if [y,x] not in edge_lst:
                        edge_lst.append([y,x])
    edge.append(edge_lst)

def BFS(value):
    global result
    queue = edge[value-2][:]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0
    new_field = []
    for f in field:
        new_field.append(f[:])
    while queue:
        for num in range(len(queue)):
            lst = queue.pop(0)
            y = lst[0]
            x = lst[1]
            for dir in range(4):
                if 0 <= y + dy[dir] <= N - 1 and 0 <= x + dx[dir] <= N - 1:
                    if new_field[y + dy[dir]][x + dx[dir]] == value:
                        pass
                    elif new_field[y + dy[dir]][x + dx[dir]] == 0:
                        new_field[y + dy[dir]][x + dx[dir]] = value
                        queue.append([y + dy[dir], x + dx[dir]])
                    elif new_field[y + dy[dir]][x + dx[dir]] != 0:
                        if cnt < result:
                            result = cnt
                            return
        cnt += 1
        if cnt == result:
            return

N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int,input().split())))
edge = []
cnt = 1
for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            cnt += 1
            numbering(i, j, cnt)

check = 2
result = 200
for i in range(N):
    for j in range(N):
        if field[i][j] == check:
            BFS(check)
            check += 1

print(result)
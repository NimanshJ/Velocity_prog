#Aayush bhaiya aapna code yaha pe dalna
grid = [
    [3, 0,6,5,0,8,4,0,0],
    [5,2,0,0,0,0,0,0,0],
    [0,8,7,0,0,0,0,3,1],
    [0,0,3,0,1,0,0,8,0],
    [9,0,0,8,6,3,0,0,5],
    [0,5,0,0,9,0,6,0,0],
    [1,3,0,0,0,0,2,5,0],
    [0,0,0,0,0,0,0,7,4],
    [0,0,5,2,0,6,3,0,0]
    ]

def sol(grid, hori, vert, num):
    for a in range(9):
        if grid[hori][a] == num:
            return False
    for a in range(9):
        if grid[a][vert] == num:
            return False
    startHori = hori - hori % 3
    startVert = vert - vert % 3
    for q in range(3):
        for r in range(3):
            if grid[q + startHori][r + startVert] == num:
                return False
    return True

def sud(grid, hori, vert):
    if (hori == 9 - 1 and vert == 9):
        return True
    if vert == 9:
        hori += 1
        vert = 0
    if grid[hori][vert] > 0:
        return sud(grid, hori, vert + 1)
    for num in range(1, 10, 1):
        if sol(grid, hori, vert, num):
            grid[hori][vert] = num
            if sud(grid, hori, vert + 1):
                return True
        grid[hori][vert] = 0
       
sud(grid, 0, 0);

for q in range(9):
    print(grid[0][q], end = "")
print()

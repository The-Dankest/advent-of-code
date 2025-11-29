from sys import stdin

class DisjointSet:
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = parent

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

grid = [line.strip() for line in stdin.readlines()]

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
perim = [((), (), ())]

width = len(grid[0])
height = len(grid)


points = []
parents = {}
for x in range(width):
    for y in range(height):
        points.append((x, y))
        parents[(x, y)] = (x, y)


dj = DisjointSet(points, parents)

for x in range(width):
    for y in range(height):
        for dir in dirs:
            new_x = dir[0] + x
            new_y = dir[1] + y
            if 0 <= new_x < width and 0 <= new_y < height and grid[new_y][new_x] == grid[y][x]:
                dj.union((x, y), (new_x, new_y))

scores = []
for parent in parents:
    if parents[parent] == parent:
        group_type = grid[parent[1]][parent[0]]
        cells_to_visit = [parent]
        visited = set(cells_to_visit)
        area = 1
        perimeter = 0
        found_walls = set()
        while len(cells_to_visit) > 0:
            x, y = cells_to_visit.pop()
            for dir in dirs:
                new_x = dir[0] + x
                new_y = dir[1] + y
                if 0 <= new_x < width and 0 <= new_y < height:
                    if (new_x, new_y) not in visited:
                        if grid[new_y][new_x] == group_type:
                            area += 1
                            visited.add((new_x, new_y))
                            cells_to_visit.append((new_x, new_y))
                for dir2 in perim:
                    # check this and next cell
                    # if we are on the perimeter 
                    # check if either left or right are in the found_walls already
                    found_walls.add(((new_x, new_y), dir2))
                    pass
        scores.append((group_type, area, perimeter, (area * perimeter)))

for score in scores:
    print(score)
# print(sum(scores))

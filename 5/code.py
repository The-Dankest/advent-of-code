from collections import defaultdict, deque

def is_valid(rules, pages: list):
    in_pages = set(pages)
    filtered_rules = [(a, b) for a, b in rules if a in in_pages or b in in_pages]
    in_rules = set([x for y in filtered_rules for x in y if x in in_pages or y in in_pages])
    filtered_pages = [x for x in pages if x in in_rules]
    position = {item: i for i, item in enumerate(filtered_pages)}

    # Check each rule
    for a, b in filtered_rules:
        if position.get(a, float('-inf')) > position.get(b, float('inf')):
            return False
    return True


def order_pages(rules, pages):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    in_pages = set(pages)
    filtered_rules = [(a, b) for a, b in rules if a in in_pages or b in in_pages]
    
    for a, b in filtered_rules:
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []
    
    while queue:
        current = queue.popleft()
        order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    rank = {num: i for i, num in enumerate(order)}

    return sorted(pages, key=lambda x: rank.get(x, float('inf')))

rules = []

line = input()
while line != "":
    rules.append(list(map(int, line.split("|"))))
    line = input()

count = 0

while True:
    try:
        pages = list(map(int, input().split(",")))
        if not is_valid(rules, pages):
            new_pages = order_pages(rules, pages)
            count += new_pages[len(pages) // 2]
            print(is_valid(rules, new_pages))
    except EOFError:
        break

print(count)

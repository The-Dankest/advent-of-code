from functools import cmp_to_key

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
    precedence = {a: set() for a, b in rules}
    for a, b in rules:
        precedence.setdefault(a, set()).add(b)
        precedence.setdefault(b, set())
    
    def compare(x, y):
        if y in precedence.get(x, set()):
            return -1
        elif x in precedence.get(y, set()):
            return 1
        return 0

    return sorted(pages, key=cmp_to_key(compare))

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

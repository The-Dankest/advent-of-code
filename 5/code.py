def is_valid(rules, pages: list):
    in_pages = set(pages)
    in_rules = set([x for y in rules for x in y if x in in_pages or y in in_pages])
    filtered_pages = [x for x in pages if x in in_rules]
    before = [pages.pop(0)]
    nexts = {
        
    }
    for page in pages:
        # check every rule to see if the ordering matches up
    return True



rules = []

line = input()
while line != "":
    rules.append(list(map(int, line.split("|"))))
    line = input()

count = 0

while True:
    try:
        pages = list(map(int, input().split(",")))
        if is_valid(rules, pages):
            count += pages[len(pages) // 2]
    except EOFError:
        break

print(count)

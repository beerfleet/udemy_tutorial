def count_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

gen = count_to(3)
for counter in gen:
    for inner in count_to(counter):
        print(inner, end='')
    print()
        
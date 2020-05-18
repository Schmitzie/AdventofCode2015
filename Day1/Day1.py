f = open("input").read()
# print(f.read())

counter = 0
for x in f:
    if x == "(":
        counter += 1
    else:
        counter -= 1

print(counter)
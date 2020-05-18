f = open("input").read()
# print(f.read())

counter = 0
for x, val in enumerate(f):
    if counter == -1:
        print(x, counter)
        break
    elif val == "(":
        counter += 1
    else:
        counter -= 1

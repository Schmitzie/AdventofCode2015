x = 0
y = 0
counter = 0
cart = []
for i in open('input').read():
    # counter_^ = x.count('^')
    # counter_> = x.count('>')
    # counter_v = x.count('v')
    # counter_< = x.count('<')
    # ^, > = 1
    # v, < = -1

    # write arrow to x/y. Save every step.
    # Compare new step to all old steps: if duplicated, do not increment counter
    if i == '^':
        y += 1
    elif i == '>':
        x += 1
    elif i == 'v':
        y += -1
    elif i == '<':
        x += -1

    coord = x,y

    if coord not in cart:
        counter += 1
    cart.append(coord)

print(counter)
# +1 for start location
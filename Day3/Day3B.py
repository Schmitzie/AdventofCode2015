
cart = []
f = open('input').read()
santa = f[::2]
robo_santa = f[1::2]

def santa_tracker(nick):
    x = 0
    y = 0
    counter = 0

    for i in nick:
        # print(i)
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
    return counter
big_counter = santa_tracker(santa) + santa_tracker(robo_santa)

print(big_counter)
# NO +1 for start location
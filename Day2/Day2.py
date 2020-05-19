wrap = 0
total_wrap = 0
for x in open('input'):
    l,w,h = x.split('x')
    l,w,h = int(l), int(w), int(h)
    y = l,w,h
    z = min(l*w, w*h, h*l)

    wrap = (2*l*w) + (2*w*h) + (2*h*l) + z
    print(wrap)
    total_wrap += wrap
print(total_wrap)

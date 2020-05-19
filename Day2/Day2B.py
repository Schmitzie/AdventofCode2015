wrap = 0
total_wrap = 0
total = 0
for x in open('input'):
    l,w,h = x.split('x')
    l,w,h = int(l), int(w), int(h)
    y = l,w,h
    pkg_ribbon = min(2*(l+w), 2*(w+h), 2*(h+l))
    bow = l*w*h
    ribbon = pkg_ribbon+bow
    total += ribbon

print(total)
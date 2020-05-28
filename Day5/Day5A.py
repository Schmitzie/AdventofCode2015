# nice =
# if 3 vowels
# if double-letters
# if does NOT contain ab, cd, pq, or xy
# else it is naughty

from collections import Counter
naughty = 0
nice = 0
n_strings = ["ab", "cd", "pq", "xy"]
vowel_string = ["a", "e", "i", "o", "u"]
vowel_count = 0

def vowel_counter():
    for i in open('input').readlines():
        

for i in open('input').readlines():
    if any(x in i for x in n_strings):
        continue
        # naughty += 1
        # print(i)
    elif vowel_counter() >= 3:
        nice += 1


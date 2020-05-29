# nice =
# if 3 vowels
# if double-letters
# if does NOT contain ab, cd, pq, or xy
# else it is naughty

naughty = 0
nice = 0
n_strings = ["ab", "cd", "pq", "xy"]
vowels = 'aeiou'
input = open('input').read().split('\n')

def vowel_counter():
    if i in 'aeiou':



for i in input:
    if not (any(x in i for x in n_strings)):
        if vowel_counter() >= 3:
            nice += 1

#print(nice)
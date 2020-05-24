# No input file

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
# The input to the MD5 hash is some secret key (your puzzle input, given below)
# followed by a number in decimal. To mine AdventCoins, you must find Santa the
# lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
import hashlib
input = "bgvyzdsv"

# combine input with number
def combo_hash():
    counter = 0
    for x in range(10000000):
        md5_input = input + str(x)
        result = hashlib.md5(md5_input).hexdigest()
        # For 4A: if result[:5] == '00000':
        if result[:6] == '000000':
            print(x)
            break

combo_hash()
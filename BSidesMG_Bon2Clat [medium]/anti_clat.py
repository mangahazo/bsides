import string


def clat(hafatra,shift):
    clat = ''         
    for i in hafatra:
        if i not in string.ascii_letters:
            clat += i
        else:
            if i in string.ascii_lowercase:
                start = ord('a')
            else:
                start = ord('A')
            clat += chr(((ord(i) - start + shift) % 26) + start)

    return clat[-1] + clat[:-1].swapcase()

def normal_order(clat):
    return clat[1:].swapcase() + clat[0]

def anti_clat(clate, shift):
    clate = normal_order(clate)
    hafatra = ''
    for i in clate:
        if i not in string.ascii_letters:
            hafatra += i
        else:
            if i in string.ascii_lowercase:
                initial = string.ascii_lowercase.index(i) 
                hafatra+=string.ascii_lowercase[(initial-shift)%26]
            else:
                initial = string.ascii_uppercase.index(i) 
                hafatra+=string.ascii_uppercase[(initial-shift)%26]
            
    return hafatra

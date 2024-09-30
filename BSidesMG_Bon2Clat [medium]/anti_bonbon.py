def bonbon(hafatra):
    bon = ''
    bonbon = (hafatra[-1] + hafatra[:-1])[::-1]
    for i in bonbon:
        bon += chr(ord(i) ^ 0xb)
    return bon[::2]+ bon[1::2] # normal to even


def even_to_normal(bonbon):
    x = len(bonbon)//2 + len(bonbon)%2
    b = ''.join([bonbon[i:i+1]+bonbon[i+x:i+1+x] for i in range(x)])
    return b

def xor_to_xor(bon):
    bonbon = ''
    for i in bon: 
        bonbon += chr(ord(i)^0xb)
    
    return bonbon

def anti_bonbon(value):
    x = xor_to_xor(even_to_normal(value))
    return (x[-1] + x[:-1])[::-1]


initial = 'abcdefgh'
bon = bonbon(initial)
print(bon)
final = anti_bonbon(bon)
print(final)
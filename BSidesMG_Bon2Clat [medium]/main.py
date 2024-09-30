import string
from anti_bonbon import anti_bonbon
from anti_clat import anti_clat
def main():
    check()

def bonbon(hafatra):
    bon = ''
    bonbon = (hafatra[-1] + hafatra[:-1])[::-1]
    for i in bonbon:
        bon += chr(ord(i) ^ 0xb)
    return bon[::2]+ bon[1::2]

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
                                                                  
def check():                            
    
    
    # x = bonbon(clat(clat(bonbon(clat(clat(bonbon('xxx'),20),24)),2),7))
    # print('original : ', string.printable)
    # x = bonbon(clat(clat(bonbon(clat(clat(bonbon(string.printable),20),24)),2),7))
    # print('bonbonclat : ', x)
    bonbon_clat = "W_WIVNH^\\68XH^6IOJ>6P=?S6SPMx6_MOC]X>LK6"

    s = anti_bonbon(anti_clat(anti_clat(anti_bonbon(anti_clat(anti_clat(anti_bonbon(bonbon_clat), 7), 2)), 24), 20))
    print('reversed : ', s)
    

if __name__ == "__main__":
    main()

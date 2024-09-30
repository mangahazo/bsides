#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import banner

def main():
    print("Welcome to BSides Madagascar 2024")
    x = (input("Tsapao ny Vintanao:"))
    check(x)

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
                                                                  
def check(s):                                                  
    x = bonbon(clat(clat(bonbon(clat(clat(bonbon(s),20),24)),2),7))

    "W_WIVNH^\\68XH^6IOJ>6P=?S6SPMx6_MOC]X>LK6"
    
if __name__ == "__main__":
    print(clat('ABCD',m))

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:49:21 2017

@author: richard
"""


def ctof(ctemp):
    f = ctemp * (9/5) + 32
    return f
    
def main():
    value = input("enter celsius temp: ")
    a = ctof(int(value))
    print(a)
    
main()

#print(5.9800 * (9/5) + 32)    
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 15:02:58 2022

@author: Blue_
"""

#Lab1 Q1 Write a program that reads an input in fahrenheit and displays the temperature in centigrade.
# formula c= 5/9 (f-32)

def main():
    fahren=float(input('Fahrenheit is: '))
    Cel = 5/9
    fToC = Cel*(fahren-32)
    
    print(fToC,' degree c'  )
main()
    
    
    
    
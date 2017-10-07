import os
import time
from random import choice
import msvcrt

os.system('color 0A')  
os.system('title IS THIS THE MATRIX ?')
os.system('mode con:cols=14 lines=16')

ping = os.system('ping google.com')


a = 0
b = 0
lim = [10,21,32,43,54,65,76,87,98]
bot = [88,89,90,91,92,93,94,95,96,97]
matrix = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']


while ping == True :
    a = a + 11
    if a == (len(matrix)-1) :
        matrix = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        a = 0
        b = 0
        ping = os.system('ping google.com')    
    elif a in lim:
        matrix[a] = '\n'
    elif a in bot:
        b = b + 1
        a = b
    elif ping == False:
        break
    elif msvcrt.kbhit():
        break
    else :
        bin = choice('0123456789')
        matrix[a] = bin
        print 'GOING IN..'
        print
        print ''.join(matrix)
        print
        print 'Press any\nkey to exit.'
        time.sleep(0.05)
        os.system('cls')

os.system('cls')

while True :
    a = a + 11
    if a == (len(matrix)-1) :
        matrix = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\n', 
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        a = 0
        b = 0
	ping = os.system('ping google.com')
        print '\a'   
    elif a in lim:
        matrix[a] = '\n'
    elif a in bot:
        b = b + 1
        a = b
    elif msvcrt.kbhit():
        break
    else :
        bin = choice('0123456789')
        matrix[a] = bin
        print 'THE MATRIX\nHAS YOU...'
        print
        print ''.join(matrix)
        print
        print 'Press any\nkey to exit.'
        time.sleep(0.05)
        os.system('cls')
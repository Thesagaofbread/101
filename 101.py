import cv2
import random

y = input("roll the dice?")
n = ''
while y == input():
    no = random.randint(1,6)
    
    if no == 1 or 2 or 3 or 4 or 5 or 6:
        print(no)
    else:
        print('error')

    if n == input() :

        break

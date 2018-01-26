#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:25:25 2017

@author: lenaprice-johnson
"""


import imgtomusic
import matplotlib.pyplot as plt
import cv2
import sys

if __name__ == '__main__':
    print("Welcome to PyMusicDrawing!")
    while True:
        
        b = False
        
        newimg = 'z'
        while newimg.lower() != 'y' or newimg.lower() != 'n':
            newimg = input("Would you like to create a new image? (y/n)")
            if newimg.lower() == 'n':
                b = True
                break
            elif newimg.lower() == 'y':
                break
            elif newimg.lower() != 'y':
                print("Input should be y/n, try again")
        
        if b:
            break
        
        print("Time to create your own drawing! Press 'm' to switch between  squares and circles. Press 'c' to change the color values (select a number for red, blue, and green) and 's' to change the size of your brush. Remember, in RGB mode, the maximum number for red, blue, and green is 256. When you're finished, press the escape key.")
        x = __import__("Python_drawing")
        result = input("Would you like to play this drawing (1), play an already existing drawing (2), or end this program (3)?")
        if result == "1": 
            image = cv2.imread("img.jpg")
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.show()
            imgtomusic.use("img.jpg")
            
            del x 
            sys.modules.pop("Python_drawing")
            
        elif result == "2":
            filename = input("Please enter in the name of the image file you would like to use (include .jpg): ")
            plt.figure()
            img = cv2.imread(filename)
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.show()
            imgtomusic.use(filename)
            
            del x 
            sys.modules.pop("Python_drawing")
            
        else:
            print("Thanks for drawing!")
            break
        
          
          


    
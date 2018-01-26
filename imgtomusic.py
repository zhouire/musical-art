# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:46:54 2017

@author: irene
"""

import cv2
import numpy

import pygame
import pygame.midi
import time

def get_pixel_color(image, img_dim):
    #img_dim = image dimensions [x1, x2, y1, y2]
    crop_img = image[img_dim[0]:img_dim[1], img_dim[2]:img_dim[3]].copy()
    
    avg_color_per_row = numpy.average(crop_img, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    
    return avg_color

def rgb_to_tone(rgb):
    rgb_avg = numpy.average(rgb)
    return int((rgb_avg/256)*88 + 20)
    '''
    r = int((rgb[0]/256)*88 + 20)
    g = int((rgb[1]/256)*50 + 77)
    b = (rgb[1]/256)*1.5 + 0.5
    return (r,g,b)
    '''
    
def rgb_to_tone_chords(rgb):
    r = int((rgb[0]/256)*88 + 20)
    g = int((rgb[1]/256)*88 + 20)
    b = int((rgb[2]/256)*88 + 20)
    return (r,g,b)    


def playtones(tones, t):
    #tones is a list, t is a time
    
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)
    for i in tones:
        player.note_on(i, 127)
        time.sleep(t)
        player.note_off(i, 127)
    del player
    pygame.midi.quit()

def playtones_chords(tones, t):
    #tones is a list of tuples, t is the length of a quarter note
    
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)
    for i in tones:
        player.note_on(i[0], 127)
        player.note_on(i[1], 127)
        player.note_on(i[2], 127)
        #i[2] is a value between 0.5 and 2
        time.sleep(t)
        player.note_off(i[0], 127)
        player.note_off(i[1], 127)
        player.note_off(i[2], 127)
    del player
    pygame.midi.quit()


def pixel_iterate(image, pixels_in_row, pixels_in_col):
    tones = []
    
    rowlength = image.shape[1]//pixels_in_row
    collength = image.shape[0]//pixels_in_col
    for i in range(0, pixels_in_col):
        for j in range(0, pixels_in_row):
            rgb = get_pixel_color(image, [i*collength, (i+1)*collength, j*rowlength, (j+1)*rowlength])
            tones.append(rgb_to_tone(rgb))
    
    return tones

def pixel_iterate_chords(image, pixels_in_row, pixels_in_col):
    tones = []
    
    rowlength = image.shape[1]//pixels_in_row
    collength = image.shape[0]//pixels_in_col
    for i in range(0, pixels_in_col):
        for j in range(0, pixels_in_row):
            rgb = get_pixel_color(image, [i*collength, (i+1)*collength, j*rowlength, (j+1)*rowlength])
            tones.append(rgb_to_tone_chords(rgb))
    
    return tones

def use(filename):
    img = cv2.imread(filename)
    pixels_in_row = int(input("Number of pixels per row (integer <= 50): "))
    
    while pixels_in_row > 50 or type(pixels_in_row) != int:
        print("Must be integer less than or equal to 50; try again")
        pixels_in_row = int(input("Number of pixels per row (integer <= 50): "))
        
    pixels_in_col = int(input("Number of pixels per column (integer <= 50): "))

    while pixels_in_col > 50 or type(pixels_in_col) != int:
        print("Must be integer less than or equal to 50; try again")
        pixels_in_col = int(input("Number of pixels per column (integer <= 50): "))
        
    t = float(input("Length of each tone in seconds (number from " + str(0.05) + " to " + str(250/(pixels_in_row*pixels_in_col)) + "): "))
        
    while t < 0.05 or t > 250/(pixels_in_row*pixels_in_col):
        print("Must be between 0.5 and", 250/(pixels_in_row*pixels_in_col), "; try again")
        t = float(input("Length of each tone in seconds (number from " + str(0.05) + " to " + str(250/(pixels_in_row*pixels_in_col)) + "): "))
        
    style = 'z'
    while style != "y" and style != 'n':
        style = input("Y/N should each pixel be a chord? (other option: single notes) ")
        
        if style.lower() == "y":
            tones = pixel_iterate_chords(img, pixels_in_row, pixels_in_col)
            playtones_chords(tones, t)
        elif style.lower() == 'n':
            tones = pixel_iterate(img, pixels_in_row, pixels_in_col)
            playtones(tones, t)
        else:
            print("The input should be y/n; try again")
        
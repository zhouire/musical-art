# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:46:54 2017

@author: irene
"""

import cv2
import numpy
import random

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

def use():
    filenames = ["demo_pop_art.jpg", "demo_art_noveau.jpg", "demo_surrealism.jpg", "la-grande-jatte.jpg", "Rainbow_6.jpg", "starry-night.jpg"]
    files = []
    for f in filenames:
        im = cv2.imread(f)
        if f == "demo_pop_art.jpg" or f == "demo_art_noveau.jpg":
            img = cv2.resize (im, (360, 640))
        else:
            img = cv2.resize(im, (960, 540))
        files.append(img)
    
    while True:
        
        file_index = random.randint(0, 5)
        i = files[file_index]
        name = filenames[file_index]
        chord = random.randint(0,1)
        
        cv2.imshow(name, i)
        cv2.waitKey(62)
        
        if chord == 0:
            tones = pixel_iterate_chords(i, 25, 25)
            playtones_chords(tones, 0.1)
        elif chord == 1:
            tones = pixel_iterate(i, 25,25)
            playtones(tones, 0.1)
            
        cv2.destroyAllWindows()
        time.sleep(2)
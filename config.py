# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:45:18 2024

@author: Sean
"""
import pygame
import random
import math

MAPWIDTH = 800
MAPHEIGHT = 600

TILESIZE = 25

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255,0,0)
black = (0,0,0)
darkgrey = (30,30,30)

FPS = 60
REMAINING_HEALTH_LAYER = 6
HEALTH_LAYER = 5
ABOVE_PLAYER = 4
PLAYER_LAYER = 3
BLOCKS_LAYER = 2
GROUND_LAYER = 1

tilemap = [
    '.............123',
    '.............456',
    '.............789',
    '.............123',
    '.........P...456',
    '.............789',
    '................',
    '................',
    '.123............',
    '3456123.........',
    '6789456.......S.',
    '9...789.........'
    ]

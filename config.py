# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:45:18 2024

@author: Sean
"""
import pygame

MAPWIDTH = 800
MAPHEIGHT = 600

TILESIZE = 50

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
darkgrey = (30,30,30)

FPS = 120
HEALTH_LAYER = 5
ABOVE_PLAYER = 4
PLAYER_LAYER = 3
BLOCKS_LAYER = 2
GROUND_LAYER = 1

tilemap = [
    '.............123',
    '.............456',
    '............S789',
    '.S..............',
    '.........P......',
    '................',
    '................',
    '................',
    '.123............',
    '3456123.........',
    '6789456.........',
    '9.S.789.........'
    ]

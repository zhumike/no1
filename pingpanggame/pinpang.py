import pygame as pg
from pygame.locals import *
from time  import sleep
import sys

pg.init()
scr=pg.display.set_mode((600,500)) #设置屏幕大小
pg.display.set_caption(("打乒乓球")) #设置屏幕标题
pp=255,140,0
green=0,255,0
white=255,255,255
cs=255,121,21   

x=120
y=120
vx=1
vy=1
a=200

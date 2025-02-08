
import sys
from random import randint, uniform,choice
from time import sleep
import images

LIMIT=7
COLORS={'red':(255,0,0),'green':(0,255,0),'blue':(0,0,255),
        'yellow':(255,255,0),'white':(255,255,255),'maroon':(128,0,0),
        'purple':(255,0,255),'orange':(255,165,0)}
VCOLORS=list(COLORS.values())
def random_color():
    """
    Returns a random color from the predefined list of colors.
    
    The color is represented as a tuple of RGB values.
    """

    return choice(VCOLORS)
def draw_rectangle(image:images.Image, x1:int, y1:int, x2:int, y2:int, color:tuple):
    for x in range(x1,x2):
        for y in range(y1,y2):
            image.setPixel(x,y,color)
    for x in range(x1,x2):
        image.setPixel(x,y1,(30,30,30))
        image.setPixel(x,y2,(30,30,30))
    for y in range(y1+1,y2-1):
        image.setPixel(x1,y,(30,30,30))
        image.setPixel(x2,y,(30,30,30))
def splitspace_v(image:images.Image,x1:int,y1:int,x2:int,y2:int):
    '''splits a space vertically'''
    m=randint(1,2)
    dx=(x2-x1)//3*m
    draw_rectangle(image,x1,y1,x1+dx,y2,random_color())
    return x1+dx
def splitspace_h(image:images.Image,x1:int,y1:int,x2:int,y2:int):
    '''splits a space horizontally'''
    m=randint(1,2)
    dy=(y2-y1)//3*m
    draw_rectangle(image,x1,y1,x2,y1+dy,random_color())
    return y1+dy

def splitspace(image:images.Image,x1,y1,x2,y2,l:int):
    '''splits a space recursively while depth limit isn't reached and space is big enough'''
    if l==0:return    
    if x2-x1<=6 or y2-y1<=6: return
    if y2-y1<x2-x1:
        xd=splitspace_v(image,x1,y1,x2,y2)
        splitspace(image,x1,y1,xd,y2,l-1)
        splitspace(image,xd,y1,x2,y2,l-1)
    else:
        yd=splitspace_h(image,x1,y1,x2,y2)
        splitspace(image,x1,y1,x2,yd,l-1)
        splitspace(image,x1,yd,x2,y2,l-1)


image=images.Image(700,700)
try:
    limit=int(input("Enter recursive depth limit: "))
except:
    limit=LIMIT
    print("Using default limit of",limit)
if limit<2: 
    limit=LIMIT
    print("Using default limit of",limit)
splitspace(image,0,0,700,700,limit)
#print(splitspace_v(image,0,0,700,700))
image.draw()
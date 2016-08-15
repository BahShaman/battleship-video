#!/usr/bin/python

from PIL import Image, ImageDraw

#import Image, ImageDraw

H = 500
W = 500

GW = 20
GH = 20
GZ = 10

OX = 10
OY = 15

img = Image.new("RGB", (W, H), "black")
draw = ImageDraw.Draw(img)

class BShipGrid:

    def __init__(self, drawing, x, y, h, w, size):
        for i in range(0,h*size+size,h*size/size):
            #print x
            for j in range(0,w*size+size,w*size/size):
                print i,j
                draw.line((i+x, 0+y, i+x, j+y), "blue", 3)
                draw.line((0+x, j+y, i+x, j+y), "blue", 3)


bs = BShipGrid(draw,15,15,20,20,10)
bsz = BShipGrid(draw,250,15,20,20,10)
"""
for x in range(W):
    for y in range(H):
        color = (x % 255, y % 255, (x % (y+1)) % 255)
        draw.point((x,y), fill=color)

draw.line((0, H/2, W, H/2), "yellow")
draw.rectangle([(200, 60), (100, 120)], outline="#FF00FF")
draw.text((20, 40), "quickies.seriot.ch")
"""
img.save("img.png", "PNG")
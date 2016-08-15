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

    ox = 0
    oy = 0
    dataarray = ()

    def __init__(self):
        pass

    def adddata(self, col,row):
        pass

    def draw(self, drawing, x, y, h, w, size):
        self.ox = x + 15
        self.oy = y + 15
        self.drawgrid(drawing, x, y, h, w, size)
        self.drawdata(drawing, x, y, h, w, size)

    def drawdata(self, drawing, x, y, h, w, size):
        ox = self.ox
        oy = self.oy
        letter=0
        for i in range(0,h*size+size,h*size/size):
            letter=letter+1
            number=0
            #print x
            for j in range(0,w*size+size,w*size/size):
                number=number+1
                if (number == 7 and letter==7):
                    draw.rectangle([(i+ox+5, j+oy+5), (i+ox+15, j+oy+15)], fill="#FF0000")

    def drawgrid(self, drawing, x, y, h, w, size):
        ox = self.ox
        oy = self.oy
        left=0
        top=0
        letter=0
        number=0
        for i in range(0,h*size+size,h*size/size):
            letter=letter+1
            number=0
            #print x
            for j in range(0,w*size+size,w*size/size):
                number=number+1
                if not (i == 0 and j == 0):
                    if i == 0:
                        left=left+1
                        draw.text((i+x, j+y), str(left))
                    if j == 0:
                        top=top+1
                        draw.text((i+x, j+y), str(chr(top+64)))
                print i,j,letter,number
                draw.line((i+ox, 0+oy, i+ox, j+oy), "blue", 3)
                draw.line((0+ox, j+oy, i+ox, j+oy), "blue", 3)


bs = BShipGrid()
bs.adddata(7,7)
bs.draw(draw,15,15,20,20,10)
bsz = BShipGrid()
bs.adddata(6,6)
bsz.draw(draw,250,15,20,20,10)

img.save("img.png", "PNG")
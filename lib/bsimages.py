#!/usr/bin/python

from PIL import Image, ImageDraw

#import Image, ImageDraw

H = 250
W = 1000

GW = 20
GH = 20
GZ = 10

OX = 10
OY = 15

img = Image.new("RGBA", (W, H), (0,0,255,20))
draw = ImageDraw.Draw(img)

class BShipGrid:

    gridrows=10
    gridcols=10
    ox = 0
    oy = 0
    dataarray = ()

    def __init__(self):
        self.dataarray = [[0 for x in range(self.gridrows)] for y in range(self.gridcols)]
        pass

    def getdata(self):
        print self.dataarray

    def adddata(self, col,row):
        self.dataarray[col][row]=1
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
                print "number,letter",number,letter
                if (self.dataarray[number-2][letter-2]==1):
                    draw.rectangle([(i+ox+2, j+oy+2), (i+ox+18, j+oy+18)], fill="#666666")

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
bs.adddata(6,6)
bs.draw(draw,15,15,20,20,10)
bsz = BShipGrid()
bsz.adddata(1,9)
bsz.adddata(3,6)
bsz.draw(draw,750,15,20,20,10)

bs.getdata()


img.save("img.gif", "gif",transparency=0)
img.save("img.png", "PNG",)
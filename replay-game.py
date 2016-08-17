import sys
sys.path.append('lib')
from BShipGrid import BShipGrid
from PIL import Image, ImageDraw

class TheGame():
    pass

    def __init__(self):

        W = 1000
        H = 200

        self.img = Image.new("RGBA", (W, H), (0,255,0,0))
        self.drawing = ImageDraw.Draw(self.img)

        a = BShipGrid("Simon")
        
        a.markship("A1")
        a.markship("A2")
        a.markship("A3")
        
        a.markship("C3")
        a.markship("D3")
        a.markship("E3")
        a.markship("F3")
        a.markship("G3")

        a.markship("F6")
        a.markship("E6")
        a.markship("D6")
        a.markship("C6")

        a.markship("H1")
        
        b = BShipGrid("Alyssa")

        b.markship("J5")
        b.markship("J4")
        b.markship("J6")
        b.markship("J3")
        
        b.markship("E9")
        b.markship("D9")
        b.markship("C9")
        b.markship("F9")
        b.markship("G9")

        b.markship("B5")
        b.markship("C5")
        b.markship("D5")

        b.markship("E2")
        b.markship("F2")
        b.markship("D2")

        b.markship("B7")

        self.b = b
        self.a = a

    def save(self,filename):

        self.b.draw(self.drawing,10,50, 150, 150)
        self.a.draw(self.drawing,10,10, 150, 150)
        #self.img.save("test_draw_small.gif", "gif")#,transparency=0)
        self.img.save(filename+".png", "PNG",)


if __name__ == '__main__':
    g = TheGame()
    g.save("master")
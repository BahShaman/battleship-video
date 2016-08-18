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
        a.markship("I1")
        
        a.markship("G10")
        a.markship("H10")
        a.markship("I10")
        a.markship("J10")
        
        
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
        b.markship("B8")

        self.b = b
        self.a = a

    def save(self,filename):

        self.a.draw(self.drawing,10,10, 150, 150)
        self.b.draw(self.drawing,750,10, 150, 150)
        #self.img.save("test_draw_small.gif", "gif")#,transparency=0)
        self.img.save(filename+".png", "PNG",)


if __name__ == '__main__':
    g = TheGame()
    #shots = ["A3","A4","A5"]
    shots = []
    with open('./data/data.txt') as f:
        lines = f.read().splitlines()
    
    for line in lines:
        data = line.split("\t")
        print data
        shots += data[0:]

    x = 0

    sx = "%02d" % (x,)
    g.save("shots/"+sx+"-master-start-game")

    x = 1
    t = 0
    print "len of shots", len(shots)
    for shot in shots:
        t = t+1
        print t
        print shot
        if shot.find("!") > 0:
            stype = "HIT"
            cshot = shot[:-1]
        elif shot.find("*") > 0:
            stype = "SINK"
            cshot = shot[:-1]
        else:
            #if t % 2 == 1:
            print "skipping", shot
            #name="simon"
            #cshot=shot
            #stype="miss"
            #g.b.markmiss(cshot)
            continue
        if t % 2 == 1:
            name="simon"
            g.b.markshot(cshot)
        else:
            name="alyssa"
            g.a.markshot(cshot)
        print cshot
        sx = "%02d" % (x,)
        g.save("shots/"+sx+"-master-"+name+"-"+cshot+"-"+stype)
        x = x+1

        



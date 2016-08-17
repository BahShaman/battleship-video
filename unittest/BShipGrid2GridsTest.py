import unittest
import sys
sys.path.append('../lib')
from BShipGrid import BShipGrid
from PIL import Image, ImageDraw

class BShipGridBaseTest(unittest.TestCase):
    b = None
    img = None
    drawing = None

    def suite():
        suite = unittest.TestLoader().loadTestsFromTestCase(BShipGridBaseTest)
        return suite
        
    def setUp(self):
        self.a = BShipGrid("Player A")
        self.b = BShipGrid("Player B")
        W = 500
        H = 500
        self.b.adddata(0,0)
        self.b.adddata(1,1)
        self.b.adddata(1,2)
        self.b.adddata(2,3)
        self.b.adddata(3,4)
        self.b.adddata(5,6)
        self.b.adddata(9,9)
        self.b.addshot(1,1)
        self.b.addshot(1,2)
        self.b.addshot(3,4)
        self.img = Image.new("RGBA", (W, H), (0,255,0,0))
        self.drawing = ImageDraw.Draw(self.img)

    def test_firsttest(self):
        self.b.getdata()

    def test_draw_a_location1(self):
        self.a.draw(self.drawing,10,10, 200, 200)
        self.drawing.line((10,10,210,10),"yellow",1)
        #self.img.save("test_draw.gif", "gif")#,transparency=0)
        self.img.save("test_draw_a_location1.png", "PNG",)

    def test_draw_a_location2(self):
        self.a.draw(self.drawing,10,100, 200, 200)
        self.drawing.line((10,100,210,100),"yellow",1)

        #self.img.save("test_draw.gif", "gif")#,transparency=0)
        self.img.save("test_draw_a_location2.png", "PNG",)


    def tearDown(self):
        self.a = None
        self.b = None
        self.img = None
        self.drawing = None


if __name__ == '__main__':
    unittest.main()
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
        self.b = BShipGrid("Simon")
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

    def test_draw(self):
        self.b.draw(self.drawing,10,10, 100, 100)
        #self.img.save("test_draw.gif", "gif")#,transparency=0)
        self.img.save("test_draw.png", "PNG",)

    def test_draw_small(self):
        self.b.draw(self.drawing,10,10, 50, 50)
        #self.img.save("test_draw_small.gif", "gif")#,transparency=0)
        self.img.save("test_draw_small.png", "PNG",)

    def test_draw_large(self):
        self.b.draw(self.drawing,10,10, 300, 300)
        #self.img.save("test_draw_large.gif", "gif")#,transparency=0)
        self.img.save("test_draw_large.png", "PNG",)

    def test_shiprect_0_0(self):
        points = self.b.shiprect(0,0,100,100,0,0)
        print points
        self.assertEqual((25,25,35,35), points, "shiprect does not calc right")

    def tearDown(self):
        self.b = None
        self.img = None
        self.drawing = None


if __name__ == '__main__':
    unittest.main()
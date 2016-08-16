import unittest
import sys
sys.path.append('../vixen')
from vixen import Vixen
from BShipGrid import BShipGrid

class BShipGridBaseTest(unittest.TestCase):
    vixen = None

    def suite():
        suite = unittest.TestLoader().loadTestsFromTestCase(BShipGridBaseTest)
        return suite
        
    def setUp(self):
        b = BShipGrid()
        b.

if __name__ == '__main__':
    unittest.main()
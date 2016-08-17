# Source Generated with Decompyle++
# File: BShipGrid-Copy.pyc (Python 2.7)

'''
BShipGrid
'''

class BShipGrid:
    _playername = ''
    _data = None
    _gridrows = 10
    _gridcols = 10
    _textoffset = 10
    
    def __init__(self, playername):
        self._playername = playername
        self._data = [ [ 0 for x in range(self._gridrows) ] for y in range(self._gridcols) ]

    
    def getdata(self):
        return self._data

    
    def adddata(self, row, col):
        self.addship(row, col)

    
    def addship(self, row, col):
        self._data[row][col] = 1

    
    def markship(self, mark):
        print mark[0], mark[1:], '|', ord(mark[0]) - 65, int(mark[1:]) - 1
        self.addship(ord(mark[0]) - 65, int(mark[1:]) - 1)

    
    def markshot(self, mark):
        print mark[0], mark[1:], '|', ord(mark[0]) - 65, int(mark[1:]) - 1
        self.addshot(ord(mark[0]) - 65, int(mark[1:]) - 1)

    
    def addshot(self, row, col):
        self._data[row][col] = 2

    
    def setdata(self, dataarray):
        self._data = dataarray

    
    def draw(self, drawing, x, y, w, h):
        self.drawdata(drawing, x, y, w, h)
        self.drawgrid(drawing, x, y, w, h)
        self.drawshot(drawing, x, y, w, h)
        self.drawtext(drawing, x, y, w, h)

    
    def drawgrid2(self, drawing, x, y, w, h):
        ox = x
        oy = y
        gy = x + self._textoffset
        gx = y + self._textoffset
        sx = w / (self._gridrows + 1)
        sy = h / (self._gridcols + 1)
        for i in range(self._gridrows + 1):
            for j in range(self._gridcols + 1):
                l1x1 = i * sx + ox + gx
                l1y1 = j * sy + oy + gy
                l1x2 = i * sx + ox + gx
                l1y2 = j * sy + oy + gy
                print (i, j), (x + w, y + h), (gx, gy), (sx, sy), (l1x1, l1y1, l1x2, l1y2)
                drawing.line((l1x1, l1y1, l1x2, l1y2), 'blue', 2)
                drawing.line((0 + ox + gx, j * sy + oy + gy, i * sx + ox + gx, j * sy + oy + gy), 'blue', 2)
            
        

    
    def drawgrid(self, drawing, x, y, w, h):
        hlinelength = w
        vlinelength = h
        hdivisions = self._gridrows + 1
        vdivisions = self._gridcols + 1
        hdivsize = w / hdivisions
        vdivsize = h / vdivisions
        for i in range(hdivisions):
            for j in range(vdivisions):
                hxstrt = x + self._textoffset + i * vdivsize
                hystrt = y + self._textoffset + j * hdivsize
                hxstop = x + self._textoffset + i * vdivsize + hlinelength
                hystop = y + self._textoffset + j * hdivsize
                print 'h', (i, j), (x, y), (hxstrt, hystrt, hxstop, hystop)
                print 'i*hdivsize', i * hdivsize
                vxstrt = x + self._textoffset + i * vdivsize
                vystrt = y + self._textoffset + j * hdivsize
                vxstop = x + self._textoffset + i * vdivsize
                vystop = y + self._textoffset + j * hdivsize + vlinelength
                print 'v', (i, j), (x, y), (vxstrt, vystrt, vxstop, vystop)
                drawing.line((hxstrt, hystrt, hxstop, hystop), 'blue', 2)
                drawing.line((vxstrt, vystrt, vxstop, vystop), 'red', 2)
            
        

    
    def drawdata(self, drawing, x, y, w, h):
        ox = x
        oy = y
        gy = x + self._textoffset
        gx = y + self._textoffset
        sx = w / (self._gridrows + 1)
        sy = h / (self._gridcols + 1)
        for i in range(10):
            for j in range(10):
                if self._data[i][j] > 0:
                    print 'SHIP'
                    drawing.rectangle([
                        (i * sx + ox + gx, j * sy + oy + gy),
                        (i * sx + ox + gx + sx, j * sy + oy + gy + sy)], fill = '#666666')
        

    
    def drawtext(self, drawing, x, y, w, h):
        ox = x
        oy = y
        gy = x
        gx = y
        px = -5
        py = -3
        sx = w / (self._gridrows + 1)
        sy = h / (self._gridcols + 1)
        for i in range(self._gridrows + 1):
            for j in range(self._gridcols + 1):
                if i == 0:
                    if j == 0 or i == 0:
                        drawing.text((i * sx + ox + gx + px, j * sy + oy + gy + py), str(j))
                    if j == 0:
                        drawing.text((i * sx + ox + gx + px, j * sy + oy + gy + py), str(chr(i + 64)))
                    
        

    
    def drawshot(self, drawing, x, y, w, h):
        ox = x
        oy = y
        gy = x + self._textoffset
        gx = y + self._textoffset
        px = (w / (self._gridrows + 1)) * 0.5
        py = (h / (self._gridcols + 1)) * 0.5
        sx = w / (self._gridrows + 1)
        sy = h / (self._gridcols + 1)
        for i in range(10):
            for j in range(10):
                if self._data[i][j] > 1:
                    print 'HIT'
                    drawing.ellipse([
                        (i * sx + ox + gx + px, j * sy + oy + gy + py),
                        (i * sx + ox + gx + sx - px, j * sy + oy + gy + sy - py)], fill = '#FF0000')
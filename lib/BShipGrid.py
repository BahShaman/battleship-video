# Source Generated with Decompyle++
# File: BShipGrid-Copy.pyc (Python 2.7)
from PIL import ImageFont


'''
BShipGrid
'''

class BShipGrid:
    _playername = ''
    _data = None
    _gridrows = 10
    _gridcols = 10
    _textoffset = 10
    _gridfont = None
    _namefont = None
    
    def __init__(self, playername):
        self._playername = playername
        self._data = [ [ 0 for x in range(self._gridrows) ] for y in range(self._gridcols) ]
        #self._gridfont = ImageFont.load("./verdana.ttf")
#        self._gridfont = ImageFont.truetype("verdana.ttf",14)
#        self._gridfont = ImageFont.truetype("Verdana",14)
        self._gridfont = ImageFont.load_default()
        #self._namefont = ImageFont.truetype("verdana.ttf",20)

    
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
            
    def hgridline(self, x, y, w, h, n):
        hlinelength = w
        vlinelength = h
        hdivsize = w / self._gridrows
        vdivsize = h / self._gridrows
        #calulate each point
        hxstrt = x + self._textoffset
        hystrt = y + self._textoffset + n * hdivsize
        hxstop = x + self._textoffset + hlinelength
        hystop = y + self._textoffset + n * hdivsize
        #print 'h', (i, j), (x, y), (hxstrt, hystrt, hxstop, hystop)
        #print 'i*hdivsize', i * hdivsize
        return (hxstrt, hystrt, hxstop, hystop)

    def vgridline(self, x, y, w, h, n):
        hlinelength = w
        vlinelength = h
        hdivsize = w / self._gridrows
        vdivsize = h / self._gridrows
        #calculate each point
        vxstrt = x + self._textoffset + n * vdivsize
        vystrt = y + self._textoffset 
        vxstop = x + self._textoffset + n * vdivsize
        vystop = y + self._textoffset + vlinelength
        #print 'v', (i, j), (x, y), (vxstrt, vystrt, vxstop, vystop)
        return (vxstrt, vystrt, vxstop, vystop)
    
    def shiprect(self, x, y, w, h, row,col):
        hdivsize = w / self._gridrows
        vdivsize = h / self._gridrows

        x1 = x + self._textoffset + col * hdivsize
        y1 = y + self._textoffset + row * vdivsize
        x2 = x + self._textoffset + col * hdivsize + hdivsize
        y2 = y + self._textoffset + row * vdivsize + vdivsize
        return (x1,y1, x2,y2)

    def shotrect(self, x, y, w, h, row,col):
        hdivsize = w / self._gridrows
        vdivsize = h / self._gridrows

        shotscale=.2
        print "hdvivesize and with scale",hdivsize, hdivsize * shotscale

        x1 = int(x + self._textoffset + col * hdivsize + hdivsize * shotscale)
        y1 = int(y + self._textoffset + row * vdivsize + vdivsize * shotscale)
        x2 = int(x + self._textoffset + col * hdivsize + hdivsize - hdivsize * shotscale)
        y2 = int(y + self._textoffset + row * vdivsize + vdivsize - vdivsize * shotscale)
        print "returning rect from shot",(x1,y1, x2,y2)
        return (x1,y1, x2,y2)

    def htextcoord(self, x, y, w, h, row, col):
        hdivsize = w / self._gridrows
        vdivsize = h / self._gridrows
        x1 = int(x + (col+1) * hdivsize - hdivsize)
        y1 = int(y + (row+1) * vdivsize - vdivsize/2)
        print "returning coord from text",(x1,y1)
        return [(x1,y1)]


    def vtextcoord(self, x, y, w, h, row, col):
        hdivsize = w / self._gridrows
        vdivsize = h / self._gridrows
        x1 = int(x + (col+1) * hdivsize - hdivsize/2)
        y1 = int(y + (row+1) * vdivsize - vdivsize)
        print "returning coord from htext",(x1,y1)
        return [(x1,y1)]


    def namecoord(self, x, y, w, h):
        pass

    def drawgrid(self, drawing, x, y, w, h):
        hdivisions = self._gridrows + 1
        vdivisions = self._gridcols + 1
        for i in range(hdivisions):
            for j in range(vdivisions):
                hline = self.hgridline(x,y,w,h,j)
                vline = self.vgridline(x,y,w,h,i)
                drawing.line(hline, 'blue', 2)
                drawing.line(vline, 'blue', 2)

    
    def drawdata(self, drawing, x, y, w, h):
        for i in range(self._gridrows):
            for j in range(self._gridcols):
                if self._data[i][j] > 0:
                    print 'SHIP'
                    rect = self.shiprect(x,y,w,h,i,j)
                    drawing.rectangle(rect, fill = '#666666')
        

    
    def drawtext(self, drawing, x, y, w, h):
        for i in range(self._gridrows):
            for j in range(self._gridcols):
                if j == 0 or i == 0:
                    if i == 0:
                        coord = self.vtextcoord(x,y,w,h,i,j)
                        drawing.text(coord, str(j+1))
                    if j == 0:
                        coord = self.htextcoord(x,y,w,h,i,j)
                        drawing.text(coord, str(chr(i + 1 + 64)), font=self._gridfont)                    
            
    
    def drawshot(self, drawing, x, y, w, h):
        for i in range(self._gridrows):
            for j in range(self._gridcols):
                if self._data[i][j] > 1:
                    print 'HIT'
                    rect = self.shotrect(x,y,w,h,i,j)
                    print "drawing rect from ", x,y,w,h,i,j,rect
                    #drawing.rectangle(rect, fill = '#00FF00')
                    drawing.ellipse(rect, fill = '#FF0000')



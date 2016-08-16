
"""
BShipGrid
"""
class BShipGrid:

    _playername = ""
    _data = None
    _gridrows = 10
    _gridcols = 10
    _textoffset = 10

    def __init__(self,playername):
        self._playername = playername
        self._data = [[0 for x in range(self._gridrows)] for y in range(self._gridcols)]
    
    def getdata(self):
        return self._data

    def adddata(self,row,col):
        self.addship(row,col)

    def addship(self,row,col):
        self._data[row][col]=1

    def addshot(self,row,col):
        self._data[row][col]=2

    def setdata(self,dataarray):
        self._data = dataarray
    
    def draw(self,drawing,x,y,w,h):
        self.drawdata(drawing,x,y,w,h)
        self.drawgrid(drawing,x,y,w,h)
        self.drawshot(drawing,x,y,w,h)
        self.drawtext(drawing,x,y,w,h)

    def drawgrid(self,drawing,x,y,w,h):
        ox = x
        oy = y
        gy = x + self._textoffset
        gx = y + self._textoffset
        sx = x + w / (self._gridrows+1)
        sy = y + h / (self._gridcols+1)
        for i in range(self._gridrows+1):
            for j in range(self._gridcols+1):
                #print i,j
                drawing.line((i*sx+ox+gx, 0+oy+gy, i*sx+ox+gx, j*sy+oy+gy), "blue", 2)
                drawing.line((0+ox+gx, j*sy+oy+gy, i*sx+ox+gx, j*sy+oy+gy), "blue", 2)

    def drawdata(self,drawing,x,y,w,h):
        ox = x
        oy = y
        gy = x + self._textoffset
        gx = y + self._textoffset
        sx = x + w / (self._gridrows+1)
        sy = y + h / (self._gridcols+1)
        for i in range(10):
            for j in range(10):
                #print i,j
                if self._data[i][j] > 0:
                    print "SHIP"
                    drawing.rectangle([(i*sx+ox+gx, j*sy+oy+gy), (i*sx+ox+gx+sx, j*sy+oy+gy+sy)], fill="#666666")

    def drawtext(self,drawing,x,y,w,h):
        ox = x
        oy = y
        gy = x 
        gx = y 
        px = -5
        py = -3
        sx = x + w / (self._gridrows+1)
        sy = y + h / (self._gridcols+1)
        for i in range(self._gridrows+1):
            for j in range(self._gridcols+1):
                if not (i == 0 and j == 0):
                    if i == 0:
                        drawing.text((i*sx+ox+gx+px, j*sy+oy+gy+py), str(j))
                    if j == 0:
                        drawing.text((i*sx+ox+gx+px, j*sy+oy+gy+py), str(chr(i+64)))

    def drawshot(self,drawing,x,y,w,h):
        ox = x
        oy = y
        gy = x + self._textoffset
        gx = y + self._textoffset
        px = 4
        py = 4
        sx = x + w / (self._gridrows+1)
        sy = y + h / (self._gridcols+1)
        for i in range(10):
            for j in range(10):
                #print i,j
                if self._data[i][j] > 1 :
                    print "HIT"
                    drawing.ellipse([(i*sx+ox+gx+px, j*sy+oy+gy+py), (i*sx+ox+gx+sx-px, j*sy+oy+gy+sy-py)], fill="#FF0000")

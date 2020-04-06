import numpy as np

class Map:

    def __init__(self):
        self.ngang = 0
        self.doc = 0
        self.soDinh = 0
        self.xStart = 0
        self.yStart = 0
        self.xEnd = 0
        self.yEnd = 0
        self.listdagiac=[]
        self.danhSachDon = []

    def getX(self):
        return self.ngang

    def getY(self):
        return self.doc

    def getStart(self):
        return self.xStart, self.yStart

    def getEnd(self):
        return self.xEnd, self.yEnd

    def getDon(self):
        return self.danhSachDon

    def setDon(self, danhSachDon):
        self.danhSachDon = danhSachDon
    
    def setDaGiac(self,list):
        self.listdagiac=list

    def getDaGiac(self):
        return self.listdagiac

    def setMap(self, ngang, doc, soDinh, xStart, yStart, xEnd, yEnd):
        self.ngang = ngang
        self.doc = doc
        self.soDinh = soDinh
        self.xStart = xStart
        self.yStart = yStart
        self.xEnd = xEnd
        self.yEnd = yEnd





# Ham noi 2 dinh thanh 1 canh cua da giac
def draw_line(mat, x0, y0, x1, y1, inplace=False):
    if not (0 <= x0 < mat.shape[0] and 0 <= x1 < mat.shape[0] and
            0 <= y0 < mat.shape[1] and 0 <= y1 < mat.shape[1]):
        raise ValueError('Invalid coordinates.')
    if not inplace:
        mat = mat.copy()
    if (x0, y0) == (x1, y1):
        mat[x0, y0] = 1
        return mat if not inplace else None
    # Swap axes if Y slope is smaller than X slope
    transpose = abs(x1 - x0) < abs(y1 - y0)
    if transpose:
        mat = mat.T
        x0, y0, x1, y1 = y0, x0, y1, x1
    # Swap line direction to go left-to-right if necessary
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0
    # Write line ends
    mat[x0, y0] = 1
    mat[x1, y1] = 1
    # Compute intermediate coordinates using line equation
    x = np.arange(x0 + 1, x1)
    y = np.round(((y1 - y0) / (x1 - x0)) * (x - x0) + y0).astype(x.dtype)
    # Write intermediate coordinates
    mat[x, y] = 1
    if not inplace:
        return mat if not transpose else mat.T


# Ham tao hinh da giac tu cac toa do dinh duoc luu trong list
def createPology(matrix, list):
    t = 0
    for i in range(0, len(list), 2):
        if (i == len(list) - 2):
            matrix = draw_line(matrix, list[0], list[1], list[i], list[i + 1])
        else:
            matrix = draw_line(matrix, list[i], list[i + 1], list[i + 2], list[i + 3])
    return matrix


# Tao ma tran rong voi cac toa do deu bang 0
def createMatrixEmpty(map):
    matrix = np.zeros((map.getX(), map.getY()), dtype = int)
    return matrix


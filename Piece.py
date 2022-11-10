from Tetris import main
x = main()
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = x.shape_colors[x.shapes.index(shape)]
        self.rotation = 0
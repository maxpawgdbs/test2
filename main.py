from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from random import randint
import sys


class NewWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.do_draw = False
        self.window()

    def window(self):
        self.setWindowTitle("Title")
        self.resize(500, 500)
        self.move(300, 300)

        self.button = QPushButton("Click on me", self)
        self.button.resize(150, 50)
        self.button.move(175, 225)
        self.button.clicked.connect(self.function)

    def function(self):
        self.do_draw = True
        self.update()

    def paintEvent(self, event):
        if self.do_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_krug(qp)
            qp.end()

    def draw_krug(self, qp):
        for i in range(20):
            radius = randint(20, 100)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            pos = QPoint(randint(1, 500), randint(1, 500))

            qp.setBrush(color)
            qp.drawEllipse(pos, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewWindow()
    window.show()
    sys.exit(app.exec_())

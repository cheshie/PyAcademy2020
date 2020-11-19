from random import randint, random

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from pyqtgraph import PlotWidget, plot, QtCore
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from numpy import arange

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.graphWidget.setXRange(0, 100)
        self.graphWidget.setYRange(0, 100)
        self.graphWidget.setBackground('w')
        self.mypen = pg.mkPen(color=(255, 0, 0), width=1.5, style=QtCore.Qt.DashLine)

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        p1 = self.draw_random_point()
        p2 = self.draw_random_point()

        self.path = list(self.bresenham(p1, p2))
        self.dataline = self.graphWidget.plot([0], [0], pen=self.mypen, symbol='o', symbolSize=5, symbolBrush=("#FF0000"))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updater)
        self.timer.start(50)
    #

    def draw_random_point(self):
        coords = ([randint(0, 100)], [randint(0, 100)])
        color = "%06x" % randint(0, 0xFFFFFF)
        self.graphWidget.plot(coords[0], coords[1], pen=self.mypen, symbol='o', symbolSize=30, symbolBrush=(color))
        return coords
    #

    def updater(self):
        x, y = 200, 200
        if len(self.path):
            x,y = self.path[0]
            self.path.pop(0)
        self.dataline.setData([x], [y])
    #

    def bresenham(self, p1, p2):
        """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
        Input coordinates should be integers.
        The result will contain both the start and the end point.
        """

        x0, y0 = p1
        x1, y1 = p2
        x0, y0 = x0[0], y0[0]
        x1, y1 = x1[0], y1[0]

        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2 * dy - dx
        y = 0

        for x in range(dx + 1):
            yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy
    #


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()

    # p1 = main.draw_random_point()
    # p2 = main.draw_random_point()

    # print(crds)
    # main.draw_path(crds)
    # main.start()

    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
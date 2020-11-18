from pyqtgraph.Qt import QtGui, QtCore
#from PyQt5.QtGui import
import pyqtgraph as pg
import sim1


# Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()

## Create some widgets to be placed inside
cnv = pg.PlotWidget(title="Simple sine wave") # canvas?

# graphWidget.setBackground('w') ?

cnv.setXRange(0, 5)
cnv.setYRange(0, 5)


#plot.plot([5], [5], QtGui.QBrush(QtGui.QColor(QtCore.qrand() % 256, QtCore.qrand() % 256, QtCore.qrand() % 256)))
pen1 = pg.mkPen(color=(255, 0, 0))
#brush1 =
pg.plot([2.5, 3, 4], [2.5, 3, 4], pen1)



## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(cnv, 0, 0)   # button goes in upper-left
# w.setCentralWidget(cnv)


## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()
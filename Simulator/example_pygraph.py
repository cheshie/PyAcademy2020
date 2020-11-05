from pyqtgraph.Qt import QtGui, QtCore
#from PyQt5.QtGui import
import pyqtgraph as pg
import sim1


# Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()

## Create some widgets to be placed inside
plot = pg.PlotWidget(title="Simple sine wave")

plot.plot([5], [5], QtGui.QBrush(QtGui.QColor(QtCore.qrand() % 256, QtCore.qrand() % 256, QtCore.qrand() % 256)))


## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(plot, 0, 0)   # button goes in upper-left


## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()
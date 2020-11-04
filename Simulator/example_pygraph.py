from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg


# Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()

## Create some widgets to be placed inside
plot = pg.PlotWidget(title="Simple sine wave")

## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(plot, 0, 0)   # button goes in upper-left

#
import numpy as np
x = np.linspace(0,10,1000)
y = np.sin(x)

plot.plot(x, y)


## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()
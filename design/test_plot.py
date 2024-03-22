import sys
import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create three canvas widgets that display the figures
        sc1 = MplCanvas(self, width=5, height=4, dpi=100)
        sc2 = MplCanvas(self, width=5, height=4, dpi=100)
        sc3 = MplCanvas(self, width=5, height=4, dpi=100)

        # Plot signals on each canvas with titles and legends
        x = np.linspace(0, 10, 100)
        sc1.axes.plot(x, np.sin(x), label='Sine')
        sc1.axes.set_title('Sine Wave')
        sc1.axes.legend()

        sc2.axes.plot(x, np.cos(x), label='Cosine')
        sc2.axes.set_title('Cosine Wave')
        sc2.axes.legend()

        sc3.axes.plot(x, np.tan(x), label='Tangent')
        sc3.axes.set_title('Tangent Wave')
        sc3.axes.legend()

        # Create a toolbar for each canvas
        toolbar1 = NavigationToolbar(sc1, self)
        toolbar2 = NavigationToolbar(sc2, self)
        toolbar3 = NavigationToolbar(sc3, self)

        # Create a layout and add the canvas and toolbar to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar1)
        layout.addWidget(sc1)
        layout.addWidget(toolbar2)
        layout.addWidget(sc2)
        layout.addWidget(toolbar3)
        layout.addWidget(sc3)

        # Create a placeholder widget to hold the layout
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

import matplotlib
from matplotlib.backend_bases import FigureCanvasBase

matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure



class _MplCanvas(FigureCanvasBase):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(_MplCanvas, self).__init__(fig)
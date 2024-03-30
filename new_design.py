import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDesktopWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt

class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spirometer XLT 0.1")
        self.setGeometry(0, 0, 800, 600)  # Initial size (optional)
        self.showMaximized()  # Maximize the window

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a button
        self.button = QPushButton('Collect Data', self)
        self.button.setFixedSize(200, 40)  # Setting fixed size
        self.button.setStyleSheet("background-color: white; color: black; border: none; padding: 5px 5px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 0px 0px; cursor: pointer; border-radius: 8px;")
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        

        self.button.clicked.connect(self.collect_and_plot_data)

        self.fig_dp, self.ax_dp = plt.subplots()
        self.canvas_dp = FigureCanvas(self.fig_dp)
        layout.addWidget(self.canvas_dp)

        self.fig_flow, self.ax_flow = plt.subplots()
        self.canvas_flow = FigureCanvas(self.fig_flow)
        layout.addWidget(self.canvas_flow)

        self.fig_volume, self.ax_volume = plt.subplots()
        self.canvas_volume = FigureCanvas(self.fig_volume)
        layout.addWidget(self.canvas_volume)

        self.fig_flow_volume, self.ax_flow_volume = plt.subplots()
        self.canvas_flow_volume = FigureCanvas(self.fig_flow_volume)
        layout.addWidget(self.canvas_flow_volume)

    def collect_and_plot_data(self):
        self.plot_data()

    def plot_data(self):
        # Generate some sample data
        time = np.linspace(0, 10, 100)
        dp = np.sin(time)
        flow_rate = np.cos(time)
        volume = np.tan(time)
        flow_rate_volume = np.sqrt(time)

        # Plot Differential Pressure vs. Time
        self.ax_dp.plot(time, dp)
        self.ax_dp.set_title('Differential Pressure - Time')
        self.ax_dp.set_xlabel('Time')
        self.ax_dp.set_ylabel('Differential Pressure')

        # Plot Flow Rate vs. Time
        self.ax_flow.plot(time, flow_rate)
        self.ax_flow.set_title('Flow Rate - Time')
        self.ax_flow.set_xlabel('Time')
        self.ax_flow.set_ylabel('Flow Rate')

        # Plot Volume vs. Time
        self.ax_volume.plot(time, volume)
        self.ax_volume.set_title('Volume - Time')
        self.ax_volume.set_xlabel('Time')
        self.ax_volume.set_ylabel('Volume')

        # Plot Flow Rate vs. Volume
        self.ax_flow_volume.plot(volume, flow_rate_volume)
        self.ax_flow_volume.set_title('Flow Rate - Volume')
        self.ax_flow_volume.set_xlabel('Volume')
        self.ax_flow_volume.set_ylabel('Flow Rate')

        # Refresh canvas
        self.canvas_dp.draw()
        self.canvas_flow.draw()
        self.canvas_volume.draw()
        self.canvas_flow_volume.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlotWindow()
    window.show()
    sys.exit(app.exec_())

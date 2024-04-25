from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QSizePolicy, QMessageBox
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils import get_ports, get_baudrates
from serial_connection import SerialConnection
from exporter import Exporter

class SerialPlotter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spirometer XLT 0.1")
        self.setGeometry(100, 100, 1000, 900)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        self.port_combo = get_ports()
        self.baudrate_combo = get_baudrates()

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_serial)

        self.export_start_button = QPushButton("Start Export")
        self.export_start_button.clicked.connect(self.start_export)

        layout.addWidget(self.port_combo)
        layout.addWidget(self.baudrate_combo)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.export_start_button)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.serial_connection = SerialConnection()
        self.exporter = Exporter(self)

        self.animation = FuncAnimation(self.figure, self.update_plot, interval=100)

    def connect_serial(self):
        port = self.port_combo.currentText()
        baudrate = int(self.baudrate_combo.currentText())
        self.serial_connection.connect(port, baudrate)

        if self.serial_connection.is_connected:
            self.connect_button.setText("Disconnect")
            self.export_start_button.setEnabled(True)
            self.serial_connection.start_reading(self.update_data)
        else:
            self.connect_button.setText("Connect")
            self.export_start_button.setEnabled(False)

    def update_data(self, value):
        self.serial_connection.append_data(value)

    def update_plot(self, frame):
        self.serial_connection.update_plot(self.ax)

    def start_export(self):
        self.exporter.export_data()

    def closeEvent(self, event):
        self.serial_connection.close_connection()
        event.accept()

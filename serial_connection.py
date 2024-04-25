import serial
from threading import Thread
import numpy as np

class SerialConnection:
    def __init__(self):
        self.serial = None
        self.is_connected = False
        self.data = {1: [], 2: [], 3: [], 4: []}  # Create separate data lists for each subplot

    def connect(self, port, baudrate):
        if self.serial is None or not self.serial.is_open:
            try:
                self.serial = serial.Serial(port, baudrate, timeout=1)
                self.is_connected = True
            except serial.SerialException as e:
                print(f"Error opening serial port: {e}")

    def start_reading(self, update_data):
        def read_serial():
            while self.is_connected:
                data = self.serial.readline().decode().strip()
                if data:
                    try:
                        # Split data to update all four plots
                        values = [float(val) for val in data.split(",")]
                        update_data(values)
                    except ValueError:
                        pass
        
        self.thread = Thread(target=read_serial)
        self.thread.start()

    def append_data(self, values):
        for i in range(4):
            self.data[i + 1].append(values[i])

    def update_plot(self, ax1, ax2, ax3, ax4):
        # Limit data length for each plot
        for i in range(4):
            self.data[i + 1] = self.data[i + 1][-50:]

        # Update the first subplot
        ax1.clear()
        ax1.plot(self.data[1])


        # Update the second subplot
        ax2.clear()
        ax2.plot(self.data[2])


        # Update the third subplot
        ax3.clear()
        ax3.plot(self.data[3])

        # Update the fourth subplot
        ax4.clear()
        ax4.plot(self.data[4])
        # ax4.set_xlabel("Time")
        # ax4.set_ylabel("Value 4")

    def close_connection(self):
        if self.serial is not None and self.serial.is_open:
            self.serial.close()
        self.is_connected = False

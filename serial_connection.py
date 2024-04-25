import serial
from threading import Thread

class SerialConnection:
    def __init__(self):
        self.serial = None
        self.is_connected = False
        self.data = []

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
                        value = float(data)
                        update_data(value)
                    except ValueError:
                        pass
        
        self.thread = Thread(target=read_serial)
        self.thread.start()

    def append_data(self, value):
        self.data.append(value)

    def update_plot(self, ax):
        y_data = self.data[-50:]
        ax.clear()
        ax.plot(y_data)
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")

    def close_connection(self):
        if self.serial is not None and self.serial.is_open:
            self.serial.close()
        self.is_connected = False

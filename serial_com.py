import serial

def read_data_from_arduino(port, baudrate=9600):
    serial = serial.Serial(port, baudrate)

    try:
        while True:
            line = serial.readline().decode().strip()
            print(line)
            
            
    except KeyboardInterrupt:
        serial.close()

if __name__ == "__main__":
    port = "COM4"
    baudrate = 9600

    read_data_from_arduino(port, baudrate)

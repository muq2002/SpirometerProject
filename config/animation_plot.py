import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimationPlot:

    def animate(self, i, dataList, ser):
        arduinoData_string = ser.readline().decode('ascii')

        try:
            arduinoData_float = float(arduinoData_string)
            dataList.append(arduinoData_float)

        except:                          
            pass

        dataList = dataList[-50:]
        
        ax.clear()
        self.getPlotFormat()
        ax.plot(dataList)

    def getPlotFormat(self):
        ax.set_ylim([0, 1200]) # 10 Bit = 0-1023 
        ax.set_title("Arduino Data")
        ax.set_ylabel("Value")
dataList = []
                                                        
fig = plt.figure()
ax = fig.add_subplot(111)

realTimePlot = AnimationPlot()

ser = serial.Serial("COM7", 9600)
time.sleep(2)

ani = animation.FuncAnimation(fig, realTimePlot.animate,
                               frames=100, fargs=(dataList, ser), interval=100) 

plt.show()
ser.close()

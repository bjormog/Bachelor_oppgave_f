
import traceback
from PyQt5 import QtWidgets,QtCore,QtGui, uic
from pandas import Interval
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
from PyQt5.QtCore import QTimer,QDateTime

import sys
import os
import threading 
import time
import psutil


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('Bachelor.ui', self) 

        self.pushButton_2.clicked.connect(self.ploting)
        self.pushButton_3.clicked.connect(self.reset_action)
        
        
        self.graphicsView.setYRange(max = 10,min = 0)
        self.graphicsView_2.setYRange(max = 10,min = 0)
        self.data_list = []
        

        

    def ploting(self):
        self.timer = QtCore.QTimer(self)
        #self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start(1000)
        

    def update_plot_data(self):
        try:
            cpu = "%0.2f" % psutil.cpu_percent(1)
            self.data_list.append(float(cpu))
            print(float(cpu))
            self.graphicsView.plot().setData(self.data_list,pen='g')
            self.graphicsView_2.plot().setData(self.data_list,pen='g')
        except Exception as e:
            print(traceback.print_exc())


        #for i in range(10):
                                   
            #x = [i]
            #y = [i]
            #self.graphicsView.plot(x,y)
        #self.graphicsView_2.plot(x,y)
        



    def reset_action(self):        
        self.graphicsView.clear()
        self.graphicsView_2.clear()       
    


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
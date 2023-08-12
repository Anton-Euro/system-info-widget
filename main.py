import sys
from PySide6 import QtCore, QtWidgets
from gui import Ui_MainWindow
import psutil
import subprocess
import time
import configparser

app = QtWidgets.QApplication([])
mainwindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainwindow)

mainwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
mainwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
mainwindow.setWindowFlag(QtCore.Qt.Tool)

config = configparser.ConfigParser()
config.read('config.ini', encoding='UTF-8')
color = config['main']['color']
x = int(config['main']['x'])
y = int(config['main']['y'])

widget_config = [
    config['widget_config']['cpu'], 
    config['widget_config']['gpu'], 
    config['widget_config']['gpu_mem'],
    config['widget_config']['mem'],
    config['widget_config']['battery'],
]
try:
    widget_config = list(map(lambda x: 1 if x == 'true' else 0, widget_config))
except:
    print('Error')
    exit(0)

if widget_config[0] == 1:
    ui.cpu.setStyleSheet(f'color: {color};')
if widget_config[1] == 1:
    ui.gpu.setStyleSheet(f'color: {color};')
if widget_config[2] == 1:
    ui.gpu_memory.setStyleSheet(f'color: {color};')
if widget_config[3] == 1:
    ui.memory.setStyleSheet(f'color: {color};')
if widget_config[4] == 1:
    ui.battery.setStyleSheet(f'color: {color};')

if x > app.screens()[0].geometry().width() - 371:
    x = app.screens()[0].geometry().width() - 371
if y > app.screens()[0].geometry().height() - 218:
    y = app.screens()[0].geometry().height() - 218
    
mainwindow.setGeometry(x, y, 371, 218)

mainwindow.show()

class Worker(QtCore.QObject):
    def work(self):
        import wmi
        w = wmi.WMI(namespace="root\\wmi")
        while True:
            if widget_config[0] == 1:
                try:
                    ui.cpu.setText(f"CPU: {psutil.cpu_percent()} % ({int(float(w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10 - 273.15))} °C)")
                except:
                    ui.cpu.setText(f"CPU: not work")
            if widget_config[1] == 1:
                try:
                    gpu_temp, _ = subprocess.Popen(["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000).communicate()
                    gpu_load, _ = subprocess.Popen(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000).communicate()
                    ui.gpu.setText(f"GPU: {gpu_load.decode('UTF-8').split(']')[-1].split()[0].strip()} % ({gpu_temp.decode('UTF-8').split('u')[-1].strip()} °C)")
                except:
                    ui.gpu.setText(f"GPU: not work")
            if widget_config[2] == 1:
                try:
                    gpu_mem, _ = subprocess.Popen(["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000).communicate()
                    gpu_mem = gpu_mem.decode('UTF-8').split(']')[-1].split()
                    ui.gpu_memory.setText(f"GPU(MEM): {round(float(gpu_mem[0])/1024, 1)}/{round(float(gpu_mem[2])/1024, 1)}GB ({round((float(gpu_mem[0])*100)/float(gpu_mem[2]),1)}%)")
                except:
                    ui.gpu_memory.setText(f"GPU(MEM): not work")
            if widget_config[3] == 1:
                try:
                    mem = psutil.virtual_memory()
                    ui.memory.setText(f"MEM: {round(mem.used/1024/1024/1024, 1)}/{round(mem.total/1024/1024/1024, 1)}GB ({mem.percent} %)")
                except:
                    ui.memory.setText(f"MEM: not work")
            if widget_config[4] == 1:
                try:
                    ui.battery.setText(f"BATTERY: {psutil.sensors_battery().percent} %")
                except:
                    ui.battery.setText(f"BATTERY: not work")
            time.sleep(1)

worker = Worker()
theard = QtCore.QThread()
worker.moveToThread(theard)
theard.started.connect(worker.work)
theard.start()

sys.exit(app.exec())
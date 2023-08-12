from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)
import configparser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding='UTF-8')
        widget_count = 0

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(371, 218)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)

        if self.config['widget_config']['cpu'] == 'true':
            self.cpu = QLabel(self.centralwidget)
            self.cpu.setObjectName(u"cpu")
            self.cpu.setGeometry(QRect(10, 10, 361, 31))
            self.cpu.setFont(font)
            widget_count += 1

        if self.config['widget_config']['gpu'] == 'true':
            self.gpu = QLabel(self.centralwidget)
            self.gpu.setObjectName(u"gpu")
            self.gpu.setGeometry(QRect(10, 10 + (30 * widget_count), 361, 31))
            self.gpu.setFont(font)
            widget_count += 1

        if self.config['widget_config']['gpu_mem'] == 'true':
            self.gpu_memory = QLabel(self.centralwidget)
            self.gpu_memory.setObjectName(u"gpu_memory")
            self.gpu_memory.setGeometry(QRect(10, 10 + (30 * widget_count), 361, 31))
            self.gpu_memory.setFont(font)
            widget_count += 1
        
        if self.config['widget_config']['mem'] == 'true':
            self.memory = QLabel(self.centralwidget)
            self.memory.setObjectName(u"memory")
            self.memory.setGeometry(QRect(10, 10 + (30 * widget_count), 361, 31))
            self.memory.setFont(font)
            widget_count += 1

        if self.config['widget_config']['battery'] == 'true':
            self.battery = QLabel(self.centralwidget)
            self.battery.setObjectName(u"battery")
            self.battery.setGeometry(QRect(10, 10 + (30 * widget_count), 361, 31))
            self.battery.setFont(font)
            widget_count += 1

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"widget", None))
        if self.config['widget_config']['cpu'] == 'true':
            self.cpu.setText(QCoreApplication.translate("MainWindow", u"CPU: 0 % (0 \u00b0C)", None))
        if self.config['widget_config']['gpu'] == 'true':
            self.gpu.setText(QCoreApplication.translate("MainWindow", u"GPU: 0 % (0 \u00b0C)", None))
        if self.config['widget_config']['gpu_mem'] == 'true':
            self.gpu_memory.setText(QCoreApplication.translate("MainWindow", u"GPU(MEM): 0/0GB (0 %)", None))
        if self.config['widget_config']['mem'] == 'true':
            self.memory.setText(QCoreApplication.translate("MainWindow", u"MEM: 0/0GB (0 %)", None))
        if self.config['widget_config']['battery'] == 'true':
            self.battery.setText(QCoreApplication.translate("MainWindow", u"BATTERY: 0 %", None))
        
    # retranslateUi


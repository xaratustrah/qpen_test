"""
QPen test

Feb 2015 Xaratustrah

"""

from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt
from mainwindow_ui import Ui_MainWindow


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Signals
        self.connect_signals()

    def connect_signals(self):
        self.pushButton.clicked.connect(self.paintEvent)
        return

    def paintEvent(self, e):
    #def my_paintEvent(self):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)

import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui", self)
        self.movie = QMovie("background.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.startButton.setStyleSheet("QPushButton{background: rgba(255,255,255, 150);}")
        self.categoryButton.setStyleSheet("QPushButton{background: rgba(255,255,255, 150);}")
        self.exitButton.clicked.connect(sys.exit)


def window():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedWidth(660)
    widget.setFixedHeight(560)
    widget.show()
    sys.exit(app.exec())


window()

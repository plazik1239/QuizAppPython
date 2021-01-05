import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Quiz Application')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
startMsg = QLabel('<h1> Welcome in Quiz App', parent=window)
startMsg.move(15, 15)

window.show()

sys.exit(app.exec_())

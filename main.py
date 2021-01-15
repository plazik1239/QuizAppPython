import sys
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from Question import Questions, Question


class PlayWindow(QMainWindow):

    def __init__(self, category):
        super().__init__()
        loadUi("PlayWindow.ui", self)
        self.player = Player()
        self.movie = QMovie("background.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.setFixedHeight(560)
        self.setFixedWidth(660)
        self.i = 0  # number of question
        if category == "all":
            self.header.setText("All Categories")
            self.questions = Questions()
        else:
            self.header.setText(category)
            self.questions = Questions()
        self.question = self.questions.getQuestion(self.i)
        self.questionLabel.setText(self.question.prompt)
        self.pushButtonA.clicked.connect(lambda: self.checkAnswer("A"))
        self.pushButtonB.clicked.connect(lambda: self.checkAnswer("B"))
        self.pushButtonC.clicked.connect(lambda: self.checkAnswer("C"))
        self.pushButtonD.clicked.connect(lambda: self.checkAnswer("D"))

    def checkAnswer(self, answer):
        if answer == self.question.answer:
            self.player.points += 1
        self.i += 1
        print(self.player.points)
        self.nextQeustion()

    def nextQeustion(self):
        self.question = self.questions.getQuestion(self.i)
        self.questionLabel.setText(self.question.prompt)
        self.labelNrQ.setText("Question " + str(self.i + 1))


class CategoryWindow(QMainWindow):

    def __init__(self):
        super(CategoryWindow, self).__init__()
        self.dialog = None
        loadUi("CategoryWindow.ui", self)
        self.movie = QMovie("background.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.setFixedHeight(560)
        self.setFixedWidth(660)
        self.backButton.clicked.connect(self.back)
        self.Button1.clicked.connect(lambda: self.play("Pokemon"))
        self.Button2.clicked.connect(lambda: self.play("Games"))
        self.Button3.clicked.connect(lambda: self.play("Music"))

    def back(self):
        self.close()
        main_window.showNormal()

    def play(self, text):
        self.dialog = PlayWindow(text)
        self.dialog.show()
        self.close()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.dialog = PlayWindow("all")
        self.dialog1 = CategoryWindow()
        self.setFixedHeight(560)
        self.setFixedWidth(660)
        loadUi("MainWindow.ui", self)
        self.movie = QMovie("background.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.exitButton.clicked.connect(sys.exit)
        self.startButton.clicked.connect(self.play)
        self.categoryButton.clicked.connect(self.category)

    def play(self):
        self.dialog.show()
        self.close()

    def category(self):
        self.dialog1.show()
        self.close()


class Player:
    def __init__(self):
        self.points = 0


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())

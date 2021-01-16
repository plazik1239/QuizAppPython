import sys
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from Question import Questions


class ScoreWindow(QMainWindow):

    def __init__(self, score):
        super().__init__()
        loadUi("UI_Windows/ScoreWindow.ui", self)
        if score < 6:
            jpg = "lowScore.gif"
        elif score > 6:
            jpg = "good score.gif"
        else:
            jpg = "ok.gif"
        self.movie = QMovie("Resources/"+jpg)
        self.label.setMovie(self.movie)
        self.movie.start()
        self.scoreLabel.setText("Twój wynik: " + str(score))
        self.backButton.clicked.connect(sys.exit)
        self.MainMenu.clicked.connect(lambda: self.toMenu())

    def toMenu(self):
        main_window.showNormal()
        player.points = 0
        self.destroy(True, True)


class PlayWindow(QMainWindow):

    def __init__(self, category):
        super().__init__()
        loadUi("UI_Windows/PlayWindow.ui", self)
        self.dialog = None
        self.movie = QMovie("Resources/background.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.setFixedHeight(560)
        self.setFixedWidth(660)
        self.i = 0  # number of question
        if category == "all":
            self.header.setText("All Categories")
        else:
            self.header.setText(category)
        self.questions = Questions(category)
        self.question = self.questions.getQuestion(0)
        self.questionLabel.setText(self.question.prompt)
        self.pushButtonA.clicked.connect(lambda: self.checkAnswer("A"))
        self.pushButtonB.clicked.connect(lambda: self.checkAnswer("B"))
        self.pushButtonC.clicked.connect(lambda: self.checkAnswer("C"))
        self.pushButtonD.clicked.connect(lambda: self.checkAnswer("D"))

    def checkAnswer(self, answer):
        if answer == self.question.answer:
            player.points += 1
        self.i += 1
        if self.i == 10:
            self.final(player.points)
        else:
            self.nextQeustion()

    def nextQeustion(self):
        self.question = self.questions.getQuestion(self.i)
        self.questionLabel.setText(self.question.prompt)
        self.labelNrQ.setText("Question " + str(self.i + 1))

    def final(self, score):
        self.dialog = ScoreWindow(score)
        self.dialog.show()
        self.i = 0
        self.destroy(True, True)


class CategoryWindow(QMainWindow):

    def __init__(self):
        super(CategoryWindow, self).__init__()
        self.dialog = None
        loadUi("UI_Windows/CategoryWindow.ui", self)
        self.movie = QMovie("Resources/background.gif")
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
        self.destroy(True, True)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.dialog = None
        self.dialog1 = CategoryWindow()
        self.setFixedHeight(560)
        self.setFixedWidth(660)
        loadUi("UI_Windows/MainWindow.ui", self)
        self.movie = QMovie("Resources/background.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.exitButton.clicked.connect(sys.exit)
        self.startButton.clicked.connect(self.play)
        self.categoryButton.clicked.connect(self.category)

    def play(self):
        self.dialog = PlayWindow("all")
        self.dialog.show()
        self.close()

    def category(self):
        self.dialog1.show()
        self.close()


class Player:
    def __init__(self):
        self.points = 0


player = Player()
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())

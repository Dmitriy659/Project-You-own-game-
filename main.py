from PyQt5.QtGui import QColor
from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel, QLineEdit, QGridLayout, QVBoxLayout, QFrame, \
    QColorDialog, QHBoxLayout, QFontDialog, QMessageBox, QDesktopWidget
from PyQt5.QtCore import Qt
import datetime as dt


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()

        self.setWindowTitle('СВОЯ ИГРА')
        self.setFixedSize(550, 200)

        # основные элементы программы, их настройки
        self.b = True
        self.sc1 = 0
        self.sc2 = 0
        self.k = 0
        self.team_name1 = ''
        self.team_name2 = ''
        self.accounting = 0

        col = QColor(255, 255, 255)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(0, 0, 2000, 2000)
        self.frm.hide()

        self.main_layout = QVBoxLayout(self)

        self.horizontlayout = QHBoxLayout(self)

        self.horizontlayout2 = QHBoxLayout(self)

        self.verticallayout2 = QVBoxLayout(self)

        self.verticallayout3 = QVBoxLayout(self)

        self.layout2 = QHBoxLayout(self)

        self.horizontlayout.addLayout(self.horizontlayout2)
        self.horizontlayout2.addLayout(self.verticallayout2)
        self.horizontlayout2.addLayout(self.verticallayout3)

        self.inf1 = QLabel(self)
        self.inf1.move(30, 30)
        self.inf1.resize(180, 30)
        self.inf1.setText('Название первой команды')

        self.name1_line = QLineEdit(self)
        self.name1_line.move(210, 30)
        self.name1_line.resize(150, 25)

        self.inf2 = QLabel(self)
        self.inf2.move(30, 60)
        self.inf2.resize(180, 30)
        self.inf2.setText('Название второй команды')

        self.first_move1 = QPushButton(self)
        self.first_move1.move(390, 30)
        self.first_move1.resize(160, 30)
        self.first_move1.setText('Эта команда ходит первая')
        self.first_move1.clicked.connect(self.first_m_1)

        self.first_move2 = QPushButton(self)
        self.first_move2.move(390, 60)
        self.first_move2.resize(160, 30)
        self.first_move2.setText('Эта команда ходит первая')
        self.first_move2.clicked.connect(self.first_m_2)

        self.name2_line = QLineEdit(self)
        self.name2_line.move(210, 60)
        self.name2_line.resize(150, 25)

        self.label = QLabel(self)
        self.label.move(10, 100)
        self.label.setText('Если названия команд введены и вы готовы играть, нажмите на кнопку')
        self.label.resize(420, 25)

        self.end_label = QLabel(self)
        self.end_label.move(700, 350)
        self.end_label.setText('')
        self.end_label.resize(800, 70)
        self.end_label.setFont(QtGui.QFont("Times", 40, QtGui.QFont.Bold))
        self.end_label.hide()

        self.start = QPushButton(self)
        self.start.move(150, 130)
        self.start.resize(100, 50)
        self.start.setText('START')
        self.start.clicked.connect(self.game)

        self.team1 = QLabel(self)
        self.team1_score = QLabel(self)
        self.team1.hide()
        self.team1_score.hide()

        self.team2 = QLabel(self)
        self.team2_score = QLabel(self)
        self.team2.hide()
        self.team2_score.hide()

        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.name1 = QLabel(self)
        self.name1.setText('Информатика')
        self.name1.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
        self.grid.addWidget(self.name1, 0, 0)
        self.name1.hide()

        self.name2 = QLabel(self)
        self.name2.setText('Python')
        self.name2.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
        self.grid.addWidget(self.name2, 1, 0)
        self.name2.hide()

        self.lang = QLabel(self)
        self.lang.setText('Языки програмированния')
        self.lang.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
        self.grid.addWidget(self.lang, 2, 0)
        self.lang.hide()

        self.ai = QLabel(self)
        self.ai.setText('Искусственный интеллект')
        self.ai.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
        self.grid.addWidget(self.ai, 3, 0)
        self.ai.hide()

        self.cell_1_100 = QPushButton(self)
        self.cell_1_100.setText('100')
        self.cell_1_100.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.grid.addWidget(self.cell_1_100, 0, 1)
        self.cell_1_100.clicked.connect(self.c1_100)
        self.cell_1_100.hide()

        self.cell_1_200 = QPushButton(self)
        self.cell_1_200.setText('200')
        self.grid.addWidget(self.cell_1_200, 0, 2)
        self.cell_1_200.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_1_200.clicked.connect(self.c1_200)
        self.cell_1_200.hide()

        self.cell_1_300 = QPushButton(self)
        self.cell_1_300.setText('300')
        self.grid.addWidget(self.cell_1_300, 0, 3)
        self.cell_1_300.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_1_300.clicked.connect(self.c1_300)
        self.cell_1_300.hide()

        self.cell_1_400 = QPushButton(self)
        self.cell_1_400.setText('400')
        self.grid.addWidget(self.cell_1_400, 0, 4)
        self.cell_1_400.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_1_400.clicked.connect(self.c1_400)
        self.cell_1_400.hide()

        self.cell_1_500 = QPushButton(self)
        self.cell_1_500.setText('500')
        self.grid.addWidget(self.cell_1_500, 0, 5)
        self.cell_1_500.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_1_500.clicked.connect(self.c1_500)
        self.cell_1_500.hide()

        self.cell_2_100 = QPushButton(self)
        self.cell_2_100.setText('100')
        self.grid.addWidget(self.cell_2_100, 1, 1)
        self.cell_2_100.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_2_100.clicked.connect(self.c2_100)
        self.cell_2_100.hide()

        self.cell_2_200 = QPushButton(self)
        self.cell_2_200.setText('200')
        self.grid.addWidget(self.cell_2_200, 1, 2)
        self.cell_2_200.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_2_200.clicked.connect(self.c2_200)
        self.cell_2_200.hide()

        self.cell_2_300 = QPushButton(self)
        self.cell_2_300.setText('300')
        self.grid.addWidget(self.cell_2_300, 1, 3)
        self.cell_2_300.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_2_300.clicked.connect(self.c2_300)
        self.cell_2_300.hide()

        self.cell_2_400 = QPushButton(self)
        self.cell_2_400.setText('400')
        self.grid.addWidget(self.cell_2_400, 1, 4)
        self.cell_2_400.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_2_400.clicked.connect(self.c2_400)
        self.cell_2_400.hide()

        self.cell_2_500 = QPushButton(self)
        self.cell_2_500.setText('500')
        self.grid.addWidget(self.cell_2_500, 1, 5)
        self.cell_2_500.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_2_500.clicked.connect(self.c2_500)
        self.cell_2_500.hide()

        self.cell_3_100 = QPushButton(self)
        self.cell_3_100.setText('100')
        self.grid.addWidget(self.cell_3_100, 2, 1)
        self.cell_3_100.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_3_100.clicked.connect(self.c3_100)
        self.cell_3_100.hide()

        self.cell_3_200 = QPushButton(self)
        self.cell_3_200.setText('200')
        self.grid.addWidget(self.cell_3_200, 2, 2)
        self.cell_3_200.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_3_200.clicked.connect(self.c3_200)
        self.cell_3_200.hide()

        self.cell_3_300 = QPushButton(self)
        self.cell_3_300.setText('300')
        self.grid.addWidget(self.cell_3_300, 2, 3)
        self.cell_3_300.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_3_300.clicked.connect(self.c3_300)
        self.cell_3_300.hide()

        self.cell_3_400 = QPushButton(self)
        self.cell_3_400.setText('400')
        self.grid.addWidget(self.cell_3_400, 2, 4)
        self.cell_3_400.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_3_400.clicked.connect(self.c3_400)
        self.cell_3_400.hide()

        self.cell_3_500 = QPushButton(self)
        self.cell_3_500.setText('500')
        self.grid.addWidget(self.cell_3_500, 2, 5)
        self.cell_3_500.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_3_500.clicked.connect(self.c3_500)
        self.cell_3_500.hide()

        self.cell_4_100 = QPushButton(self)
        self.cell_4_100.setText('100')
        self.grid.addWidget(self.cell_4_100, 3, 1)
        self.cell_4_100.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_4_100.clicked.connect(self.c4_100)
        self.cell_4_100.hide()

        self.cell_4_200 = QPushButton(self)
        self.cell_4_200.setText('200')
        self.grid.addWidget(self.cell_4_200, 3, 2)
        self.cell_4_200.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_4_200.clicked.connect(self.c4_200)
        self.cell_4_200.hide()

        self.cell_4_300 = QPushButton(self)
        self.cell_4_300.setText('300')
        self.grid.addWidget(self.cell_4_300, 3, 3)
        self.cell_4_300.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_4_300.clicked.connect(self.c4_300)
        self.cell_4_300.hide()

        self.cell_4_400 = QPushButton(self)
        self.cell_4_400.setText('400')
        self.grid.addWidget(self.cell_4_400, 3, 4)
        self.cell_4_400.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_4_400.clicked.connect(self.c4_400)
        self.cell_4_400.hide()

        self.cell_4_500 = QPushButton(self)
        self.cell_4_500.setText('500')
        self.grid.addWidget(self.cell_4_500, 3, 5)
        self.cell_4_500.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.cell_4_500.clicked.connect(self.c4_500)
        self.cell_4_500.hide()

        self.main_layout.addLayout(self.grid)
        self.main_layout.addLayout(self.horizontlayout)

        self.verticallayout2.addWidget(self.team1)

        self.verticallayout3.addWidget(self.team2)

        self.change_background = QPushButton(self)
        self.change_background.setText('Изменить')
        self.change_background.clicked.connect(self.showDialog)
        self.change_background_label = QLabel(self)
        self.change_background_label.setText('Изменить фон')

        self.change_font = QPushButton(self)
        self.change_font.setText('Изменить')
        self.change_font.clicked.connect(self.showDialog_font)
        self.change_font_label = QLabel(self)
        self.change_font_label.setText('Изменить шрифт')

        self.turn = QLabel(self)
        self.turn.move(850, 215)
        self.turn.resize(400, 30)
        self.turn.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.turn.hide()

        self.change_font.hide()
        self.change_font_label.hide()
        self.change_background.hide()
        self.change_background_label.hide()

        self.question = QLabel(self)
        self.question.move(10, 225)
        self.question.resize(1800, 200)
        self.question.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.question.hide()

        self.answer_team1 = QPushButton(self)
        self.answer_team1.move(10, 490)
        self.answer_team1.resize(520, 40)
        self.answer_team1.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.answer_team1.clicked.connect(self.plus_score_team1)
        self.answer_team1.hide()

        self.answer_team2 = QPushButton(self)
        self.answer_team2.move(1250, 490)
        self.answer_team2.resize(520, 40)
        self.answer_team2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.answer_team2.clicked.connect(self.plus_score_team2)
        self.answer_team2.hide()

        self.nobody_answer = QPushButton(self)
        self.nobody_answer.move(630, 490)
        self.nobody_answer.resize(520, 40)
        self.nobody_answer.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.nobody_answer.setText('Никто не ответил')
        self.nobody_answer.clicked.connect(self.nobody)
        self.nobody_answer.hide()

        self.ans = QPushButton(self)
        self.ans.move(1300, 580)
        self.ans.setText('Показать ответ')
        self.ans.resize(200, 30)
        self.ans.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
        self.ans.clicked.connect(self.show_ans)
        self.ans.hide()

        self.ans_label = QLabel(self)
        self.ans_label.move(1180, 640)
        self.ans_label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.ans_label.resize(700, 100)
        self.ans_label.hide()

    def game(self):
        # начало основной игры, здесь закрывается начальное окно, и появляются основные элементы игры
        self.team_name1 = self.name1_line.text()
        self.team_name2 = self.name2_line.text()

        self.answer_team1.setText('Ответила команда {}'.format(self.team_name1))
        self.answer_team2.setText('Ответила команда {}'.format(self.team_name2))

        self.team1.setText('Команда {}'.format(self.team_name1))
        self.team2.setText('Команда {}'.format(self.team_name2))

        self.team1_score.setText('Счет: {}'.format(str(self.sc1)))
        self.team2_score.setText('Счет: {}'.format(str(self.sc2)))
        self.team1_score.move(10, 630)
        self.team2_score.move(954, 630)
        self.team1_score.resize(300, 40)
        self.team2_score.resize(300, 40)
        self.team1_score.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.team2_score.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))

        self.change_background_label.resize(250, 30)
        self.change_font_label.resize(250, 30)

        self.change_background_label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.change_font_label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))

        self.team1.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.team2.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))

        self.change_background_label.move(10, 900)
        self.change_background.move(9, 950)

        self.change_font_label.move(750, 900)
        self.change_font.move(750, 950)

        self.inf1.close()
        self.name1_line.close()
        self.name2_line.close()
        self.inf2.close()
        self.label.close()
        self.start.close()
        self.first_move2.close()
        self.first_move1.close()

        self.show_all()

        self.setFixedSize(1900, 1000)

        if self.b:
            self.turn.setText('Ходит команда {}'.format(self.team_name1))
        else:
            self.turn.setText('Ходит команда {}'.format(self.team_name2))

        self.frm.show()

    def showDialog(self):
        # изменение фона
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())

    def showDialog_font(self):
        # изменение шрифта названия команд
        font, ok = QFontDialog.getFont()
        if ok:
            self.team1.setFont(font)
            self.team2.setFont(font)

    def keyPressEvent(self, event):
        # найстройка горячих клавиш, их подключение к соответствующим кнопками
        if event.key() == Qt.Key_F:
            self.showDialog()
        if event.key() == Qt.Key_S:
            self.showDialog_font()

    def show_all(self):
        # показ основных элементов игры
        self.name1.show()
        self.name2.show()
        self.lang.show()
        self.ai.show()
        self.team2.show()
        self.team2_score.show()
        self.team1.show()
        self.team1_score.show()
        self.change_font.show()
        self.change_background_label.show()
        self.change_background.show()
        self.change_background_label.show()
        self.change_font_label.show()
        self.turn.show()
        self.cell_1_100.show()
        self.cell_1_200.show()
        self.cell_1_300.show()
        self.cell_1_400.show()
        self.cell_1_500.show()
        self.cell_2_100.show()
        self.cell_2_200.show()
        self.cell_2_300.show()
        self.cell_2_400.show()
        self.cell_2_500.show()
        self.cell_3_100.show()
        self.cell_3_200.show()
        self.cell_3_300.show()
        self.cell_3_400.show()
        self.cell_3_500.show()
        self.cell_4_100.show()
        self.cell_4_200.show()
        self.cell_4_300.show()
        self.cell_4_400.show()
        self.cell_4_500.show()

    def first_m_1(self):
        # настройка первого хода, передача хода другой команде
        self.b = True

    def first_m_2(self):
        # настройка первого хода, передача хода другой команде
        self.b = False

    def answer(self):
        # появление вопроса, кнопок для присуждения баллов, кнопки ответа
        self.question.show()
        self.answer_team1.show()
        self.answer_team2.show()
        self.nobody_answer.show()
        self.ans.show()

    def after_answer(self):
        # скрытие вопроса, кнопок для присуждения баллов, кнопки ответа, ответа
        self.question.hide()
        self.answer_team1.hide()
        self.answer_team2.hide()
        self.nobody_answer.hide()
        self.ans.hide()
        self.ans_label.hide()

    def closeEvent(self, event):
        # появление при закрытии окна, которое просит подтверждение действия
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        # расчет размеров экрана, чтобы окна при выходе появлялось по центру
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def c1_100(self):
        # настройка вопроса
        self.question.setText('Изобретатель системы кодирования информации, использующий два символа: точку и тире.')
        self.ans_label.setText('Морзе')
        self.answer()
        self.k = 100
        self.transition()
        self.cell_1_100.setEnabled(False)

    def c1_200(self):
        # настройка вопроса
        self.question.setText('Специальный указатель, показывающий место на экране, где появится следующий символ.')
        self.ans_label.setText('Курсор')
        self.answer()
        self.k = 200
        self.transition()
        self.cell_1_200.setEnabled(False)

    def c1_300(self):
        # настройка вопроса
        self.question.setText('Устройство, предназначенное для вычислений, обработки информации и управления работой '
                              'компьютера')
        self.ans_label.setText('Процессор')
        self.answer()
        self.k = 300
        self.transition()
        self.cell_1_300.setEnabled(False)

    def c1_400(self):
        # настройка вопроса
        self.question.setText('Операция преобразования знаков или групп знаков одной знаковой системы в знаки или '
                              'группы знаков другой знаковой системы.')
        self.ans_label.setText('Кодирование')
        self.answer()
        self.k = 400
        self.transition()
        self.cell_1_400.setEnabled(False)

    def c1_500(self):
        # настройка вопроса
        self.question.setText('Является минимальным адресуемым элементом на жестком диске, который содержит несколько '
                              'секторов.')
        self.ans_label.setText('Кластер')
        self.answer()
        self.k = 500
        self.transition()
        self.cell_1_500.setEnabled(False)

    def c2_100(self):
        # настройка вопроса
        self.question.setText('Для чего используют нижние подчеркивания в именах классов?')
        self.ans_label.setText('Заменяет пробел')
        self.answer()
        self.k = 100
        self.transition()
        self.cell_2_100.setEnabled(False)

    def c2_200(self):
        # настройка вопроса
        self.question.setText('Как передаются аргументы функций в Python (by value or reference)?')
        self.ans_label.setText('По ссылкам')
        self.answer()
        self.k = 200
        self.transition()
        self.cell_2_200.setEnabled(False)

    def c2_300(self):
        # настройка вопроса
        self.question.setText('В каких областях питон имеет преимущество?')
        self.ans_label.setText('Понятный и простой язык программирования,есть\n динамическая типизация, нет операторных'
                               ' скобок')
        self.ans_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.answer()
        self.k = 300
        self.transition()
        self.cell_2_300.setEnabled(False)

    def c2_400(self):
        # настройка вопроса
        self.question.setText('Что делает питон объектно-ориентированным?')
        self.ans_label.setText('Фокусируется на использовании объектов и классов\n для создания приложений.')
        self.ans_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.answer()
        self.k = 400
        self.transition()
        self.cell_2_400.setEnabled(False)

    def c2_500(self):
        # настройка вопроса
        self.question.setText('Перечислите минимум 4 асинхронных веб-фреймворков')
        self.ans_label.setText('Например: Tornado,Sanic,Vibora,Quart,FastAPI')
        self.ans_label.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))
        self.answer()
        self.k = 500
        self.transition()
        self.cell_2_500.setEnabled(False)

    def c3_100(self):
        # настройка вопроса
        self.question.setText('Кто является автором языка программирования Паскаль?\n1) Андрей Ершов\n2) Блез '
                              'Паскаль\n3) Никлаус Вирт\n4) Николай Паскаль')
        self.ans_label.setText('3')
        self.answer()
        self.k = 100
        self.transition()
        self.cell_3_100.setEnabled(False)

    def c3_200(self):
        # настройка вопроса
        self.question.setText('В какие годы программы писались на языке машинных кодов из 0 и 1?\n1) 40-ые годы'
                              '\n2) 50-ые годы\n3) 30-ые годы\n4) 80-ые годы')
        self.ans_label.setText('1')
        self.answer()
        self.k = 200
        self.transition()
        self.cell_3_200.setEnabled(False)

    def c3_300(self):
        # настройка вопроса
        self.question.setText('В какой период времени был разработан язык Паскаль?\n1) 40-х - начале 50-х годов'
                              '\n2) 60-х -начале 70-х годов\n3) 80-х - начале 90-х годов\n4) 90-х - начале 95-х годов')
        self.ans_label.setText('2')
        self.answer()
        self.k = 300
        self.transition()
        self.cell_3_300.setEnabled(False)

    def c3_400(self):
        # настройка вопроса
        self.question.setText('Языки близкие к процессору называются языками....\n1) Среднего уровня'
                              '\n2) Низкого уровня\n3) Высокого уровня\n4) Максимального уровня')
        self.ans_label.setText('2')
        self.answer()
        self.k = 400
        self.transition()
        self.cell_3_400.setEnabled(False)

    def c3_500(self):
        # настройка вопроса
        self.question.setText('Для преобразования мнемокода с языка ассемблера в машинный код и используется:'
                              '\n1) Интегратор\n2) Транслятор\n3) Отладчик\n4) Сумматор')
        self.ans_label.setText('2')
        self.answer()
        self.k = 500
        self.transition()
        self.cell_3_500.setEnabled(False)

    def c4_100(self):
        # настройка вопроса
        self.question.setText('В каком году был первый запуск БЭСМ?\n1) 1952\n2) 1959\n3) 1948\n4) 1963')
        self.ans_label.setText('1')
        self.answer()
        self.k = 100
        self.transition()
        self.cell_4_100.setEnabled(False)

    def c4_200(self):
        # настройка вопроса
        self.question.setText('Родина андроидной работотехники...\n1) Япония\n2) Китай\n3) Корея\n4) США')
        self.ans_label.setText('1')
        self.answer()
        self.k = 200
        self.transition()
        self.cell_4_200.setEnabled(False)

    def c4_300(self):
        # настройка вопроса
        self.question.setText('В чем заключается суть теста Тьюринга?\n1) Если машина сможет убедить человека, '
                              'что тот общается с живым собеседником, значит машина мыслит\n'
                              '2) Если машина не сможет убедить человека, что тот общается с живым собеседником, '
                              'значит машина мыслит\n'
                              '3) Если машина сможет переиграть человека в шахматы, значит машина мыслит\n4) Ни в '
                              'чем')
        self.ans_label.setText('1')
        self.answer()
        self.k = 300
        self.transition()
        self.cell_4_300.setEnabled(False)

    def c4_400(self):
        # настройка вопроса
        self.question.setText('Виды нейронных сетей?\n1) Однослойная сеть прямого распространения, многослойная сеть '
                              'прямого распространения, рекуррентная\n2) Однослойная, многослойная, двухслойная\n'
                              '3) Однородная и гибридная\n4) Свёрточные, развёртывающие, вариационные')
        self.ans_label.setText('1')
        self.answer()
        self.k = 400
        self.transition()
        self.cell_4_400.setEnabled(False)

    def c4_500(self):
        # настройка вопроса
        self.question.setText('Что такое нейрон в (ИНС)?\n1) Это элементарная структурная единица искусственной '
                              'нейронной сети.\n2) Специальная клетка, одной из ключевых задач которой является '
                              'передача -электрохимического импульса по всей нейронной сети\n'
                              '3) Математическая модель, которая анализирует сложные данные, имитируя человеческий '
                              'мозг, и имеет аппаратное и программное воплощение')
        self.ans_label.setText('1')
        self.answer()
        self.k = 500
        self.transition()
        self.cell_4_500.setEnabled(False)

    def transition(self):
        # после выбора вопроса происходит переход хода
        if self.b:
            self.b = False
            self.turn.setText('Ходит команда {}'.format(self.team_name2))
        else:
            self.b = True
            self.turn.setText('Ходит команда {}'.format(self.team_name1))

    def show_ans(self):
        # показ ответа
        self.ans_label.show()

    def plus_score_team1(self):
        # присваивание первой команде баллов
        self.sc1 += self.k
        self.team1_score.setText('Счет: {}'.format(str(self.sc1)))
        self.after_answer()
        self.accounting += 1
        if self.accounting == 20:
            self.end()
        self.ans_label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))

    def plus_score_team2(self):
        # присваивание второй команде баллов
        self.sc2 += self.k
        self.team2_score.setText('Счет: {}'.format(str(self.sc2)))
        self.after_answer()
        self.accounting += 1
        if self.accounting == 20:
            self.end()
        self.ans_label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))

    def nobody(self):
        # никто не получает баллы
        self.after_answer()
        self.accounting += 1
        if self.accounting == 20:
            self.end()
        self.ans_label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))

    def end(self):
        # после ответа на все вопросы, сравниваются результаты, и выходит результат
        self.end_label.show()
        self.turn.hide()
        # после завершения игры результат записывается в файл
        f = open('result.txt', 'a')
        date = dt.datetime.now()
        if self.sc1 > self.sc2:
            self.end_label.setText('Выиграла команда {}'.format(self.team_name1))
            f.write('\n{} Выиграла команда {}'.format(date, self.team_name1))
        elif self.sc1 < self.sc2:
            self.end_label.setText('Выиграла команда {}'.format(self.team_name2))
            f.write('\n{} Выиграла команда {}'.format(date, self.team_name2))
        elif self.sc1 == self.sc2:
            self.end_label.setText('Ничья')
            f.write('\n{} Ничья'.format(date))
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())


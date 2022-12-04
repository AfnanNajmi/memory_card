#create a memory card application
#import
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, 
    QRadioButton, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout,
    QButtonGroup)
from random import shuffle, randint

#template
class Question():
    def __init__(self,questions,right_answer,wrong1,wrong2,wrong3):
        self.questions = questions
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('1 + 1', '2', '1', '3', '5'))
questions_list.append(Question('3 + 3', '6', '7', '-10', '2'))
questions_list.append(Question('5 + 5', '10', '11', "13", 'asd'))
questions_list.append(Question('Most Dangerous Animal', 'Mosquito', 'Great White Shark', "Hippo", 'Pig'))
questions_list.append(Question('The country with the largest population?', 'China', 'India', "United States", 'Indonesia'))
questions_list.append(Question('The hardest rock', 'diamond', 'talc', "calcite", 'Dwayne Johnson'))
questions_list.append(Question('Most Dangerous Animal', 'Mosquito', 'Great White Shark', "Hippo", 'Pig'))
questions_list.append(Question('The Richest Person', 'Elon Musk', 'Jeff Bezos', "Bill Gates", 'Gautam Adani'))
questions_list.append(Question('Most Streamed Songs', 'Shape of you', 'Blinding lights', "Despacito", 'Old Town Road'))
questions_list.append(Question('The #1 Movie', 'Avatar', 'Avengers:Endgame', "Titanic", 'Star Wars Ep. VII'))

#windows
my_app = QApplication([])
my_win = QWidget()

my_win.setWindowTitle("Memory Card")
my_win.resize(400,200) #size of window
my_win.move(700,300) #location of window

#widgets

question = QLabel("Which nationality does not exist?")
optionA = QRadioButton("Enets")
optionB = QRadioButton("Chulyms")
optionC = QRadioButton("Smurfs")
optionD = QRadioButton("Aleuts")
button = QPushButton("Answer")
rating = QLabel("Rating Score")

RadioGroup = QButtonGroup()
RadioGroup.addButton(optionA)
RadioGroup.addButton(optionB)
RadioGroup.addButton(optionC)
RadioGroup.addButton(optionD)


#layouts
groupAnsBox = QGroupBox("Answer options")

ans_main_layout = QVBoxLayout()
ans_h1 = QHBoxLayout()
ans_h2 = QHBoxLayout()

ans_h1.addWidget(optionA)
ans_h1.addWidget(optionB)
ans_h2.addWidget(optionC)
ans_h2.addWidget(optionD)

ans_main_layout.addLayout(ans_h1)
ans_main_layout.addLayout(ans_h2)

groupAnsBox.setLayout(ans_main_layout)

#result panel
result_panel = QGroupBox("Test result")
result_info = QLabel("True/False")
correct_ans = QLabel("Here, we will put correct answer!")

result_layout = QVBoxLayout()
res_h1 = QHBoxLayout()
res_h2 = QHBoxLayout()
res_h3 = QHBoxLayout()

res_h1.addWidget(result_info, alignment= (Qt.AlignVCenter))
res_h2.addWidget(correct_ans, alignment= (Qt.AlignCenter))


result_layout.addLayout(res_h1)
result_layout.addLayout(res_h2)
result_layout.addLayout(res_h3)

result_panel.setLayout(result_layout)

#name layout
card_layout = QVBoxLayout()
card_h1 = QHBoxLayout()
card_h2 = QHBoxLayout()
card_h3 = QHBoxLayout()
card_h4 = QHBoxLayout()

card_h1.addWidget(question, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
card_h2.addWidget(groupAnsBox)
card_h2.addWidget(result_panel)
result_panel.hide()
card_h3.addWidget(rating, alignment= Qt.AlignLeft)
rating.hide()

card_h4.addStretch(1)
card_h4.addWidget(button, stretch= 3)
card_h4.addStretch(1)

card_layout.addLayout(card_h1)
card_layout.addLayout(card_h2)
card_layout.addLayout(card_h3)

my_win.setLayout(card_layout)

#functions
def show_result():
    """ show answer panel """
    groupAnsBox.hide()
    result_panel.show()
    rating.setText("Total correct = {}/{}".format(my_win.score, my_win.total))
    button.setText("Next Question")

def show_question():
    """ show answer panel """
    groupAnsBox.show()
    result_panel.hide()
    button.setText("Answer")
    RadioGroup.setExclusive(False)
    optionA.setChecked(False)
    optionB.setChecked(False)
    optionC.setChecked(False)
    optionD.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    """ a temporary function """
    if button.text() == "Answer":
        show_result()
    else:
        show_question()

answers = [optionA, optionB, optionC, optionD]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.questions)
    correct_ans.setText(q.right_answer)
    show_question()

def show_correct(res):
    """ show result """
    result_info.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        my_win.score +=1
        show_correct("Correct!")
        print("Statistics\n-Total questions:", my_win.total, "\n-Right answers:", my_win.score)
        print("Rating:", (my_win.score/my_win.total*100), "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked() :
            show_correct("Incorrect!")
            print("Rating:", (my_win.score/my_win.total*100), "%")


def next_question():
    """ Asks the next questions in the list """
    my_win.total += 1
    my_win.cur_question = my_win.cur_question + 1 #move on to the next question
    if my_win.cur_question >= len(questions_list):
            my_win.cur_question = 0
    q = questions_list[my_win.cur_question]
    ask(q)

def click_OK():
    if button.text() == "Answer":
        check_answer()
    else:
        next_question()


my_win.cur_question = -1
my_win.score = 0
my_win.total = 1
button.clicked.connect(click_OK)
next_question()



#execute window
my_win.show()
my_app.exec()
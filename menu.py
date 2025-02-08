from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QPushButton, QVBoxLayout, QApplication)
from data import data



def show_menu():
    global window_menu
    def save_data():
        data.append(
            {
                'question': question.text(),
                'right_answer': right_answer.text(),
                'wrong_answers': [wrong_answer1.text(), wrong_answer2.text(),wrong_answer3.text()]
            }
        )
        window_menu.close()

    window_menu = QWidget()
    window_menu.resize(400, 300)
    window_menu.setWindowTitle('Створення нового питання')

    v_line = QVBoxLayout()

    question = QLineEdit()
    question.setPlaceholderText('Введіть Питання')
    right_answer = QLineEdit()
    right_answer.setPlaceholderText('Введіть правильну відповідь')
    wrong_answer1 = QLineEdit()
    wrong_answer1.setPlaceholderText('Введіть НЕ правильну відповідь')
    wrong_answer2 = QLineEdit()
    wrong_answer3 = QLineEdit()
    wrong_answer2.setPlaceholderText('Введіть НЕ правильну відповідь')
    wrong_answer3.setPlaceholderText('Введіть НЕ правильну відповідь')

    btn_save = QPushButton('Зберегти питання')

    v_line.addWidget(question)
    v_line.addWidget(right_answer)
    v_line.addWidget(wrong_answer1)
    v_line.addWidget(wrong_answer2)
    v_line.addWidget(wrong_answer3)
    v_line.addWidget(btn_save)

    window_menu.setLayout(v_line)

    btn_save.clicked.connect(save_data)
    window_menu.show()

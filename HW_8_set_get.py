from json import load
from random import shuffle


class Question:
    @classmethod
    def __check_value(cls, value):
        return type(value) == str and value.isdigit()

    @classmethod
    def __check_bool(cls, value):
        return type(value) == bool

    def __init__(self, question_text, correct_answer):
        self.__complexity = 0
        self.__points = 0
        self.__is_correct = False
        self.__user_answer = ''
        self.__question_text = question_text
        self.__question_asked = False
        self.__result_str = ''
        if self.__check_value(correct_answer):
            self.__correct_answer = correct_answer

    @property
    def get_points(self):
        return self.__points

    @get_points.setter
    def get_points(self, complexity):
        if self.__check_value(complexity):
            self.__complexity = int(complexity)
            self.__points = int(complexity)*10
        else:
            raise ValueError('Переданное значение не является числовым')

    @property
    def is_correct(self):
        return self.__is_correct

    @is_correct.setter
    def is_correct(self, user_answer):
        if self.__check_value(user_answer):
            self.__user_answer = user_answer
            if self.__correct_answer == self.__user_answer:
                self.__is_correct = True
        else:
            raise ValueError('Ответ должен быть числовым')

    @property
    def build_feedback(self):
        return self.__result_str

    @build_feedback.setter
    def build_feedback(self, question_asked):
        if self.__check_bool(question_asked):
            self.__question_asked = question_asked
            if self.__is_correct and self.__question_asked:
                self.__result_str = f'Ответ верный, получено {self.__points} баллов'
            else:
                self.__result_str = f'Ответ не верный, верный ответ {self.__correct_answer}'
        else:
            raise ValueError('Не передано состояние вопроса')

    def build_question(self):
        return_str = f'Вопрос: {self.__question_text}\nСложность {self.__complexity}/5'
        return return_str


def read_file(name_file):
    with open(name_file) as file:
        return load(file)


def main():
    questions_list = read_file('question.json')
    shuffle(questions_list)
    print('Игра начинается')
    result_points = 0
    counter = 0
    for question in questions_list:
        user = Question(question['q'], question['a'])
        user.get_points = question['d']
        print(user.build_question())
        answer = input('Введите ответ: ')
        user.is_correct = answer
        counter += 1
        result_points += user.get_points
        user.build_feedback = True
        print(user.build_feedback)
    print(f"""Вот и всё!
Отвечено {counter} вопроса из {len(questions_list)}
Набрано баллов: {result_points}""")


if __name__ == '__main__':
    main()

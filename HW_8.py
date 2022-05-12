from json import load
from random import shuffle


class Question:
    def __init__(self, question_text, question_complexity, correct_answer, questions_asked=False, user_answer=None):
        self.question_text = question_text
        self.question_complexity = question_complexity
        self.correct_answer = correct_answer
        self.questions_asked = questions_asked
        self.user_answer = user_answer
        self.user_points = int(self.question_complexity)*10

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.user_points

    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        return self.user_answer.lower() == self.correct_answer.lower()

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return_str = f'Вопрос: {self.question_text}\nСложность {self.question_complexity}/5\nВведите ответ: '
        return return_str

    def build_feedback(self):
        """
        Возвращает:
        Ответ верный, получено __ баллов
        """
        if self.is_correct() and self.questions_asked:
            return f'Ответ верный, получено {self.get_points()} баллов'
        return f'Ответ не верный, верный ответ {self.correct_answer}'


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
        user = Question(question['q'], question['d'], question['a'])
        user.user_answer = input(user.build_question())
        user.questions_asked = True
        print(user.build_feedback())
        if user.is_correct():
            counter += 1
            result_points += user.get_points()
    print(f"""Вот и всё!
Отвечено {counter} вопроса из {len(questions_list)}
Набрано баллов: {result_points}""")


if __name__ == '__main__':
    main()

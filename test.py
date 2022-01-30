data = {
    "Сколько байт в килобайте ?": 1024,
    "В каком году Гагарин полетел в космос?": 1961,
    "Скольк дней в високосном году ?": 366,
    "Какая дата Куликовской битвы ?": 1380,
    "Сколько цветов в радуге ?": 7
}

# some_index = 0
# current_questions = list(data.keys())[some_index]
# print(current_questions)




class Quiz:
    def __init__(self, data):
        self.questions_and_answers = data
        self.current_question_index = 0

    def get_current_true_answer(self):
        print(1)
        return list(self.questions_and_answers.values())[self.current_question_index]

quiz = Quiz(data)



true_answer = quiz.get_current_true_answer()
print(true_answer)





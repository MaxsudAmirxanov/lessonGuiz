
data = {
    "Сколько байт в килобайте ?": 1024,
    "В каком году Гагарин полетел в космос?": 1961,
    "Скольк дней в високосном году ?": 366,
    "Какая дата Куликовской битвы ?": 1380,
    "Сколько цветов в радуге ?": 7
}


class Quiz:
    def __init__(self):
        self.point = 0
        self.some_index = 0
        self.questions_answers = data



    def ask_question(self):
        "Задать вопрос"
        current_questions = list(self.questions_answers.keys())[self.some_index]
        return current_questions



    def check_the_answer(self, user_answer):
        "Проверка ответа"
        true_answer = list(self.questions_answers.values())[self.some_index]
        self.some_index += 1
        return true_answer


             
game = Quiz()

number = 0
loop = True
while loop:
    number += 1
    current_questions = game.ask_question()
    print(current_questions)

    new_loop = True
    while new_loop:
        try:
            user_answer = int(input("Введите ответ:\n"))
        except ValueError:
            print('Введите число !')
        else:
            new_loop = False
    

    true_answer = game.check_the_answer(user_answer)
    if user_answer == true_answer:
        game.point += 1
        print("Вы ответили правильно ")
    else:
        print(f"Ответ неверный, правильный ответ {true_answer}")

    if number == 5:
        loop = False


print(f"Вы дали {game.point} верных ответов, из {len(data)}!\
        \nКонец игры !!!")

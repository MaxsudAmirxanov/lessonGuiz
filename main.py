
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
        global new_current_questions
        new_current_questions = current_questions

        return True



    def check_the_answer(self, user_answer):
        "Проверка ответа"
        true_answer = list(self.questions_answers.values())[self.some_index]

        global new_true_answer
        new_true_answer = true_answer
        self.some_index += 1
        
        if user_answer == true_answer:
            self.point += 1 
            return True
        else:
            return False

             
game = Quiz()

number = 0
loop = True
while loop:
    number += 1
    if game.ask_question():
        print(new_current_questions)


    new_loop = True
    while new_loop:
        try:
            user_answer = int(input("Введите ответ:\n"))
        except ValueError:
            print('Введите число !')

        else:
            new_loop = False
    

    if game.check_the_answer(user_answer):
        print("Вы ответили правильно ")
    else:
        print(f"Ответ неверный, правильный ответ {new_true_answer}")

    if number == 5:
        loop = False



print(f"Вы дали {game.point} верных ответов, из {len(data)}!\
        \nКонец игры !!!")

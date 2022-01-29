from multiprocessing.connection import answer_challenge


data = {
    1: {"Сколько байт в килобайте ?": 1024},
    2: {"В каком году Гагарин полетел в космос?": 1961},
    3: {"Скольк дней в високосном году ?": 366},
    4: {"Какая дата Куликовской битвы ?": 1380},
    5: {"Сколько цветов в радуге ?": 7}
}


class Quiz:
    def __init__(self):
        self.point = 0
        self.order_question = 0
        self.questions_answers = data



    def ask_question(self):
        "Задать вопрос"

        self.order_question += 1

        question_and_answer = self.questions_answers[self.order_question]
        for answer in question_and_answer.keys():
            print(answer)



    def check_the_answer(self, user_answer):
        "Проверка ответа"
        true_question_and_answer = self.questions_answers[self.order_question]    
        for true_answer in true_question_and_answer.values(): 
            global new_true_answer
            new_true_answer = true_answer
        
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
    game.ask_question()


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


max_data = max(data)
print(f"Вы дали {game.point} верных ответов, из {max_data}!\
        \nКонец игры !!!")

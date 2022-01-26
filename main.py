from re import T


data = {
    1: {"Сколько байт в килобайте ?": 1024},
    2: {"В каком году Гагарин полетел в космос?": 1961},
    3: {"Скольк дней в високосном году ?": 366},
    4: {"Какая дата Куликовской битвы ?": 1380},
    5: {"Сколько цветов в радуге ?": 7}
}

new_nuber = 0


class Quiz:
    def __init__(self):
        self.true_answer = 0
        self.new_number = 0

    def ask_question(self):
        "Задать вопрос"

        self.new_number += 1

        question_and_answer = data[self.new_number]
        for answer in question_and_answer.keys():
            print(answer)


    def check_the_answer(self, user_answer):
        "Проверка ответа"
        v = data[self.new_number]    
        for i in v.values():
            pass
        if user_answer == i:
            print("Вы ответили правильно ")
            self.true_answer += 1 
        else:
            print(f"Ответ неверный, правильный ответ {i}")



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
    game.check_the_answer(user_answer)

    if number == 5:
        loop = False


max_data = max(data)
print(f"Вы дали {game.true_answer} верных ответов из {max_data}!\
        \nКонец игры !!!")

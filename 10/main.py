import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


API_KEY = ""

def send_msg(user_id, message, keyboard=None):
    if keyboard is not None:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0, 'keyboard': keyboard.get_keyboard()})
    else:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

def first_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("Пройти опрос", VkKeyboardColor.PRIMARY)
    send_msg(user_id, "Вы желаете пройти опрос?", keyboard)

def second_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("Мужчина", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Женщина", VkKeyboardColor.NEGATIVE)
    send_msg(user_id, "Ваш пол?", keyboard)

def third_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("Уже", VkKeyboardColor.POSITIVE)
    keyboard.add_button("Нет", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_openlink_button("Перейти", "https://notabug.org/n3rovik")
    send_msg(user_id, "Желаете ли вы посетить NotABug разработчика?", keyboard)

def fourth_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("ПК", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Ноутбук")
    send_msg(user_id, "Вы предпочитаете работать за ноутбуком или настольным ПК?", keyboard)

def fifth_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("Утром", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Вечером", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Ночью", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Днём", VkKeyboardColor.SECONDARY)
    send_msg(user_id, "В какое время суток вы считаете себя наиболее продуктивным?", keyboard)

def sixth_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("Плохо", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Отлично", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Хорошо", VkKeyboardColor.SECONDARY)
    send_msg(user_id, "Как настроение?", keyboard)

def seventh_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("Нет", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Да", VkKeyboardColor.POSITIVE)
    send_msg(user_id, "Вы учитесь/работаете?", keyboard)

def eight_question(user_id):
    keyboard = VkKeyboard(True)
    keyboard.add_button("Начальное общее", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Основное общее", VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button("Среднее общее", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Высшее", VkKeyboardColor.POSITIVE)
    send_msg(user_id, "Какое у вас образование?", keyboard)

vk = vk_api.VkApi(token=API_KEY)
longpoll = VkLongPoll(vk)
users = []
questions = []

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.text == "Начать":
                try:
                    users.index(event.user_id)
                except:
                    users.append(event.user_id)
                    questions.append(0)
                    keyboard = VkKeyboard(True)
                    keyboard.add_button("Привет", VkKeyboardColor.PRIMARY)
                    send_msg(event.user_id, "Приветствую.", keyboard)

            if event.text == "Привет":
                send_msg(event.user_id, "Привет вездекодерам!")
                questions[users.index(event.user_id)] += 1

            match questions[users.index(event.user_id)]:
                case 9:
                    send_msg(event.user_id, "Спасибо, что приняли участие в нашем опросе. Удачного дня!")
                case 8:
                    eight_question(event.user_id)
                    questions[users.index(event.user_id)] += 1
                case 7:
                    seventh_question(event.user_id)
                    questions[users.index(event.user_id)] += 1
                case 6:
                    sixth_question(event.user_id)
                    questions[users.index(event.user_id)] += 1
                case 5:
                    fifth_question(event.user_id)
                    questions[users.index(event.user_id)] += 1
                case 4:
                    fourth_question(event.user_id)
                    questions[users.index(event.user_id)] += 1
                case 3:
                    third_question(event.user_id)
                    questions[users.index(event.user_id)] += 1   
                case 2:
                    second_question(event.user_id)
                    questions[users.index(event.user_id)] += 1
                case 1:
                    first_question(event.user_id)
                    questions[users.index(event.user_id)] += 1     
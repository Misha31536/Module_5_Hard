import time
class User: # объект класса User обладает следующими атрибутами :
            # Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = password
        self.age = int(age)


class UrTube: # объект класса UrTube
              # Атриубуты: users(список юзеров с ключем nickname заначениями (password, age)
              # videos(список видео с ключем title и значениями (duration, time_now, adult_mode)
              # current_user - текущий пользователь
    def __init__(self, users, videos, current_user):
        self.users = {}
        self.videos = {}
        self.current_user = current_user


    def initiation(self): # вызывающая функция
        choise_flag = "1" # для смены пользователя или завершения работы программы
        while choise_flag == "1":
            print("Войдите для просмотра видео")
            nickname = input("Введите ник: ")
            password = input("Введите пароль: ")
            for users_key in database.users.keys(): # перебираем все имена юзеров
                if nickname == users_key: # сравниваем есть ли в базе уже такой юзер
                    database.login(nickname, hash(password)) # если есть вызываем метод логин
                    break
            else:
                print("Пользователь не найден, необходима регистрация")
                user = User(input("Введите ник: "), input("Введите пароль: "), input("Введите возраст: "))
                database.register(user.nickname, hash(user.password), user.age) # вызываем метод регистрация
                database.login(user.nickname, hash(user.password)) # автоматически логинимся
                choise_flag = input('Хотите сменить пользователя? Введите 1=Да/0=Нет: ')

    def register(self, nickname, password, age): # метод регистрация
        self.users[nickname] = [hash(password), age] # Вносим юзера в базу

    def login(self, nickname, password): # метод логин
        if password == database.users[nickname][0]: # сравниваем введенный пароль с паролем пользователя в списке пользователей
            print(f'Добро пожаловать {nickname}')
            database.current_user = nickname # указываем кто сейчас активный пользователь
            print(f' Текущий авторезированный пользователь {database.current_user}')
            database.get_videos(input("Введите название видео для поиска: "))

        else:
            print("Пароли не совпадают")


    def log_out(self):
        database.current_user = None

    def add(self, other ): # метод добавления видео
        for title_key in database.videos.keys(): # если такое видео есть ничего не делаем
            if other.title == title_key:
                break
        else:
            self.videos[other.title] = [other.duration, other.time_now, other.adult_mode] # если видео с таким названием
            # нет добавляем в список видео

    def get_videos(self, other): # метод поиска видео
        i = 0 # ищем виде в которых есть запрашиваемый текст и выводим их на печать если ни одного не нашли то i ост = 0
        for title_key in database.videos.keys():
            if other.casefold() in title_key.casefold() or other == "*":
                print(title_key)
                i += 1
        else:
            if i == 0: # выполняется если нет ни одного совпадения
                return database.get_videos(input("Такое видео не найдено хотите повторить поиск? "
                                          "Введите повторно название видео или введите "
                                          "* что бы показать все доступные видео: "))
            else: # после вывода всех найденных видео предлагает выбрать одно для просмотра
                database.watch_video(input('Для просмотра ведите точное название фильма из перечисленных выше: '))

    def watch_video(self, other): # метод смотреть видео
        if database.current_user == None: # проверяем есть ли активный пользователь
            print("Для просмотра видео нужно авторизироваться")
        else:
            for title_key in database.videos.keys():
                if other == title_key: # проверяем правильно ли ввел пользователь видео которое хочет посмотреть
                    if database.users[database.current_user][1] < 18 and database.videos[other][2] == True:
                        print("Для просмотра видео вам должно быть больше 18")
                        break
                    else:
                        print(f'Приготовьтесь к просмотру. Продолжительность видео {database.videos[title_key][0]} сек')
                        for i in range(int(database.videos[title_key][0])):
                            time.sleep(1)
                            print(i + 1)
                        database.log_out()
                        print(f' Сеанс завершен. Текущий пользователь {database.current_user}')
                        break


class Video:

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


if __name__ == '__main__':
    database = UrTube({}, {}, None)
    database.add(Video('Лучший язык программирования 2022 года', '5', 0, False))
    database.add(Video('Для чего программистам девушка?', '6', 0, True))
    database.add(Video('Для чего программистам девушка?', '3', 0, True))
    database.add(Video('Для чего программистам дедушка?', '4', 0, False))
    database.add(Video('Для чего программистам бабушка?', '5', 0, False))
    database.register('vasya_pupkin', 'lolkekcheburek', 13)
    database.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    database.initiation()

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class UrTube:

    def __init__(self, users, videos, current_user):
        self.users = {}
        self.videos = {}
        self.current_user = current_user

    def register(self, nickname, password, age):
        self.users[nickname] = [password, age]

    def login(self, nickname, password):
        print(f'Добро пожаловать {nickname}')
        database.current_user = nickname
        print(f' Текущий авторезированный пользователь {database.current_user}')

    def log_out(self):
        database.current_user = None

    def add(self, other ):
        for title_key in database.videos.keys():
            if other.title == title_key:
                break
        else:
            self.videos[other.title] = [other.duration, other.time_now, other.adult_mode]

    def get_videos(self, other):
        for title_key in database.videos.keys():
            i = 0
            if other.casefold() in title_key.casefold() or other == "*":
                print(title_key)
                i += 1
        else:
            if i == 0:
                return database.get_videos(input("Такое видео не найдено хотите повторить поиск? "
                                          "Введите повторно название видео или введите "
                                          "* что бы показать все доступные видео: "))


class Video:

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


if __name__ == '__main__':
    database = UrTube({}, {}, None)
    choise_flag = "1"
    while choise_flag == "1":
        print("Войдите для просмотра видео")
        nickname = input("Введите ник: ")
        password = input("Введите пароль: ")
        for users_key in database.users.keys():
            if nickname == users_key:
                database.login(nickname, password)
                break
        else:
            print("Пользователь не найден, необходима регистрация")
            user = User(input("Введите ник: "), input("Введите пароль: "), input("Введите возраст: "))
            database.register(user.nickname, hash(user.password), user.age)
            database.login(user.nickname, user.password)
            choise_flag = input('Хотите сменить пользователя? Введите 1=Да/0=Нет: ')


        print(database.users.items())
    database.add(Video('Лучший язык программирования 2022 года', '20', 0, False))
    database.add(Video('Для чего программистам девушка?', '5', 0, True))
    database.add(Video('Для чего программистам девушка?', '5', 0, True))
    database.add(Video('Для чего программистам дедушка?', '5', 0, False))
    database.add(Video('Для чего программистам бабушка?', '5', 0, False))
print(database.videos.items())
database.get_videos(input("Введите название видео: "))


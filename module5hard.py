# Дополнительное практическое задание по модулю: "Классы и объекты"

# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

# Задание "Свой YouTube"

import time

"""
Класс пользователя, содержит атрибуты: логин, пароль и возраст
"""
class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

"""
Класс видео, содержит атрибуты: название, длятельность видео, возрастное ограничение а также секунду остановки
"""
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

"""
Класс UrTube, содержит атрибуты users - список зарегистрированных пользователей, videos - список загруженных видео и
 current_user - текущий пользователь. И методы: register - регистрация пользователя, log_in - аутентификация 
 пользователя, log_out - сброс текущего пользователя, add - добавление видео в базу, get_videos - поиск в базе видео, 
watch - просмотр видео, со встроенными в него проверками: вошел-ли пользователь в систему, соответствует-ли его 
возраст требуемым возрастным ограничениям и есть-ли запрашиваемое видео в базе.
"""
class UrTube():

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
            if any(user.nickname == nickname for user in self.users):
                print("Пользователь {} уже существует".format(nickname))
                return
            new_user = User(nickname, hash(password), age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user
                return True
        return False

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                return

            self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                else:

                    video.time_now = 0
                    for i in range(video.time_now, video.duration + 1):
                        print(i, end=' ')
                        time.sleep(1)
                    print("Конец видео")
                    break
        else:
            print("Видео не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


















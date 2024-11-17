import time
from shutil import which
from urllib.parse import uses_query


class User:
    def __init__(self, nickname, password, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __contains__(self, item):
        return item in self.title

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = []

    def long_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                return f'Пользователь {nickname} уже существует'
        self.users.append(User(nickname, password, age))

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        search_word = word.lower()
        found_videos = []
        for video in self.videos:
            if search_word in video.title.lower():
                found_videos.append(video)
        return found_videos

    def watch_video(self, name_film):
        film = self.get_videos(name_film)

        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')

        for video in self.videos:
            if video.adult_mode:
                print('Вам нет 18 лет, пожалуйста, покиньте страницу')

        if len(film) == 0:
            print('Видео не найдено')
        else:
            for i in range(film[0].duration):
                time.sleep(1)
                print(f'{i + 1}', end=' ')
            print('Видео закончилось')


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



# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
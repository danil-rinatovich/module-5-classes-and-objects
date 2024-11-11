import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        time_now = 0
        adult_mode = False


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def long_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if user[nickname] == nickname:
                print(f'Пользователь {nickname} уже существует')
            else:
                self.users.append(user)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_video(self, word):
        search_word = word.lower()
        return self.videos[search_word]

    def watch_video(self, name_film):
        start = time.time()
        if name_film in self.videos:
            return
        else:
            end = int(time.time() - start)
            print(end)


    def __repr__(self):
        return

    def __contains__(self, item):
        return

    def __eq__(self, other):
        return

    def __str__(self):
        return



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
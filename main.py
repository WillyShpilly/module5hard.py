
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password_hash = hash(password)
        self.age = age

    def __repr__(self):
        return f"{self.nickname}"


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password_hash == password_hash:
                print(f'Пользователь {nickname} вошел в систему!')
                return
        print(f'Введен неверный логин или пароль')

    def add_user(self, nickname, password):
        self.users[nickname] = hash(password)

    def log_out(self):
        if self.current_user:
            print(f'Пользователь {self.current_user.nickname} вышел из системы!')
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь с таким именем - "{nickname}" уже существует!')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def get_videos(self, search_word):
        search_word = search_word.lower()
        matching_videos = [video.title for video in self.videos if search_word in video.title.lower()]
        return matching_videos

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
            else:
                print(f'Видео "{video.title}" уже было дабавлено ранее!')

    def watch_video(self, title):
        if self.current_user is None:
            print(f'Войдите в аккаунт, что бы смотреть видео')
            return
        else:
            for video in self.videos:
                if video.title == title:
                    if self.current_user.age < 18:
                        print(f'Вам нет 18 лет, пожалуйста покиньте страницу!')
                    else:
                        print(f"Начинаем просмотр видео: {title}")
                        long_watch = []
                        for second in range(1, video.duration + 1):
                            print(f"\rПросмотр видео '{title}': {second} секунда", end='')
                            time.sleep(1)
                            long_watch.append(second)
                        print("\n" + " ".join(map(str, long_watch)), "Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1)
ur.add(v2)
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
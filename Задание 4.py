import time

user_hour = int(input('Введите количество часов: '))
user_minute = int(input('Введите количество минут: '))
user_second = int(input('Введите количество часов: '))
full_time = user_hour * 3600 + \
    + user_minute * 60 + user_second

while full_time >= 0:
    print('Время пошло!')
    time.sleep(1)
    print('Осталось часов: ', full_time // 3600)
    print('Осталось минут: ', (full_time % 3600) // 60)
    print('Осталось секунд', full_time % 3600 % 60)

    full_time -= 1

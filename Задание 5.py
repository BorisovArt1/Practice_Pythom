import random

names = ['Алексей', 'Евгений', 'Мария', 'Анна', 'Иван']
classes = ['Воин', 'Маг', 'Лучник' , 'Паладин']
characteristic = ['Ловкость', 'Интеллект', 'Сила', 'Выносливость', 'Удача']

parametrs = {
    'Ловкость': (1, 10),
    'Интеллект': (1, 10),
    'Сила': (1, 10),
    'Выносливость': (1, 10),
    'Удача': (1, 10)
}

def gen_parametr(min_level,max_level):
    return random.randint(min_level, max_level)

def gen_parametrs ():
    ch_dictionary = {}
    for parametr in characteristic:
        min_level, max_level = parametrs[parametr]
        ch_dictionary[parametr] = gen_parametr(min_level, max_level)
        return ch_dictionary

def gen_abilities():
    num_of_abilities = random.randint(1, 5)
    abilities = random.sample(characteristic, num_of_abilities)
    return abilities

def gen_person():
    name = random.choice(names)
    age = random.randint(18, 78)
    c_class = random.choice(classes)
    characteristic = gen_parametrs()
    ablilties = gen_abilities()

    person = {
        'имя': name,
        'возраст': age,
        'класс': c_class,
        'параметры': characteristic,
        'способности': ablilties
    }

    return person

number_of_players = int(input('Введите количество игроков: '))
for i in range (number_of_players):
    person = gen_person()
    print(person)
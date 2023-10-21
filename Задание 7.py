import random

name_of_republics = ["Армения", "Казахстан", "Абхазия", "Алжир", "Беларусь",
                     "Грузия"]

branch = ["Сельское хозяйство", "Легкая промышленность", "Тяжелая промышленность группы А",
          "Тяжелая промышленность группы Б", "Военно-промышленный косплекс",
          "Наука", "Химическая промышленность"]

print("Введите количество союзных республик")
num_of_republics = int(input())
union_republics = {}
name_of_republics_1_1 = []

j = 0
while j <= 6:
    union_republics[branch[j]] = random.choices(["Избыточно развитая", "Сбалансированно развитая", "Слабо развитая"],
                                               k=num_of_republics)
    j += 1
print("Названия республик:  ")

for i in range(num_of_republics):
    name_of_republics_1_1.append(random.choice(name_of_republics))
print(*name_of_republics_1_1)

print("\n Статистика промышленность и как она развита в определенной стране \
(через запятую указывается развитие для каждой страны):  ")
print(union_republics)

minimum = 0
maximum = 0
average = 0
key_dict = ''
country = 0

for key, value in union_republics.items():
    for i in range(len(value)):
        if value[i] == "Слабо развитая":
            minimum += 1
    if minimum > maximum:
        maximum = minimum
        key_dict += key + ','
    elif minimum == maximum:
        key_dict = key + ','
        country = maximum
    minimum = 0

print("\n Самая отстающая отрасль в республиках: ", key_dict)
print("Отрасль", *key_dict.split(), "отстает у ", country, "стран")
max_average = 0
key_dict_average = ''

for key, value in union_republics.items():
    for i in range(len(value)):
        if value[i] == "Избыточно развитая":
            average += 1
    if average > max_average:
        max_average = average
        key_dict_average = key + ','
    elif average == maximum:
        key_dict_average += key + ','
        country = maximum
    average = 0

print("\n Самая избыточно развитая отрасль в республиках: ", key_dict_average)
print("Отрасль", *key_dict_average.split(), "Избыточно развита у", country, "стран")
num = 0
max_balanced = 0
key_dict_balanced = 0

for key, value in union_republics.items():
    for i in range(len(value)):
        if value[i] == "Сбалансированно развитая":
            num += 1
        if num > max_balanced:
            max_balanced = num
            key_dict_balanced = key + ','
            country = max_balanced
        if num == maximum:
            key_dict_balanced += key + ','
            country = maximum
    num = 0

print("\n Самая сбалансированная отрасль в республиках: ", key_dict_balanced)
print("Отрасль", *key_dict_balanced.split(), "сбалансированна у ", country, "стран\n")

weak_develop = 0
average_develop = 0
strong_develop = 0

for j in range(num_of_republics):
    for key, value in union_republics.items():
        for i in range(len(value)):
            if j == 1:
                if value[j] == "Слабо развитая":
                    weak_develop += 1
                if value[j] == "Сбаласированно развитая":
                    average_develop += 1
                if value[j] == "Избыточно развитая":
                    strong_develop += 1
    print(name_of_republics_1_1[i], "Слабо развитых отраслей", weak_develop,
          "Сбалансированно развитых", average_develop,
          "Избыточно развитых", strong_develop)
    weak_develop = 0
    average_develop = 0
    strong_develop = 0

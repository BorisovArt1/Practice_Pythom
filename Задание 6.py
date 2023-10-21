import math

print ("Укажите количество наименований товаров ")
num_col = int(input())

print("Введите заказ, каждое наименование должно быть на новой строке")
array_materials = []

for i in range(num_col):
    zakaz = input().split()
    array_materials.append(zakaz)

brus_50 = 0
brus_100 = 0
doska_25 = 0
doska_50 = 0
fanera = 0

for j in range(len(array_materials)):
    if array_materials[j][1] == "брус" and array_materials[j][2] == "50":
        lenght_b50 = float(array_materials[j][3][:-1])
        colvo_b50 = int(array_materials[j][0][:-1])
        if lenght_b50 <= 1.5:
            brus_50 += math.ceil(colvo_b50 / math.ceil(3 / lenght_b50))
        else:
            brus_50 += colvo_b50

    if array_materials[j][1] == "брус" and array_materials[j][2] == "100":
        lenght_b100 = float(array_materials[j][3][:-1])
        colvo_b100 = int(array_materials[j][0][:-1])
        if lenght_b100 <= 3:
            brus_100 += math.ceil(colvo_b100 / math.ceil(6 / lenght_b100))
        else:
            brus_100 += colvo_b100

    if array_materials[j][1] == "доска" and array_materials[j][2] == "25":
        lenght_d25 = float(array_materials[j][3][:-1])
        colvo_d25 = int(array_materials[j][0][:-1])
        if lenght_d25 <= 3:
            doska_25 += math.ceil(colvo_d25 / math.ceil(6 / lenght_d25))
        else:
            doska_25 += colvo_d25

    if array_materials[j][1] == "доска" and array_materials[j][2] == "50":
        lenght_d50 = float(array_materials[j][3][:-1])
        colvo_d50 = int(array_materials[j][0][:-1])
        if lenght_d50 <= 3:
            doska_50 += math.ceil(colvo_d50 / math.ceil(6 / lenght_d50))
        else:
            doska_50 += colvo_d50

    if array_materials[j][1] == "фанера":
        s_fanera = array_materials[j][2][:-1].split("*")
        square = float(s_fanera[0]) * float(s_fanera[1])
        colvo_fanera = int(array_materials[j][0][:-1])
        if square <= 1.125:
            fanera += math.ceil(colvo_fanera / math.ceil (2.25 / square))
        else:
            fanera += colvo_fanera

if brus_50 > 0:
    print(str(brus_50) + "х", "брус 50 3м")
if brus_100 > 0:
    print(str(brus_100) + "х", "брус 100 6м")
if doska_25 > 0:
    print(str(doska_25) + "х", "доска 25 6м")
if doska_50 > 0:
    print(str(doska_50) + "х", "доска 50 6м")
if fanera > 0:
    print(str(fanera) + "х", "фанера 1.5х1.5")
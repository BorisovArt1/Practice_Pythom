print ("Введите слова для проверки в строку через пробел: ")
line = input()
array_dic = line.split()

print("Введите предложение, которое нужно проверить: ")
suggestion = input()
array_suggestion = suggestion.split()

for i in range(len(array_suggestion)):
    for j in range(len(array_dic)):
        quantity = 0
        check_in = False
        if len(array_suggestion[i]) == len(array_dic[j]):
            for h in range(len(array_dic[j])):
                if array_dic[j][h] == array_suggestion[i][h]:
                    quantity += 1
                    check_in = True
                else:
                    error = quantity
                    continue
        if len(array_suggestion[i]) == (quantity + 1) and  check_in:
            word = array_suggestion[i]
            print_ = ""
            for k in range(len(word)):
                if k == error:
                    if k!= 0:
                        print_ = print_ + (' ')
                    print_ = print_ + (word[k])

                    if k != len(word):
                        print_ = print_ + (' ')
                else:
                    print_ = print_ + (word[k])
            print(print_)
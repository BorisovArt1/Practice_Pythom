import random
def generate_phrase(nouns, verbs, phrase_type):
    if phrase_type == 'сгс':
        return f'{random.choice(nouns)} {random.choice(verbs)}'
    elif phrase_type == 'гсс':
        return f'{random.choice(verbs)} {random.choice(nouns)}'
    elif phrase_type == 'ссг':
        return f'{random.choice(nouns)} {random.choice(nouns)}'

def generate_phrases(nouns, verbs, phrase_type, num_phrases):
    phrases = []
    for i in range(num_phrases):
        phrases.append(generate_phrase(nouns, verbs, phrase_type))
    return phrases

nouns = []
verbs = []

print('Введите существительное (стоп-слово - "стоп")')
while True:
    noun = input()
    if noun == 'стоп':
        break
    nouns.append(noun)

print('Введите глагол(стоп-слово - "стоп")')
while True:
    verb = input()
    if verb == 'стоп':
        break
    verbs.append(verb)

phrase_type = input('Введите тип фраз, которые нужно сгенерировать')
num_phrases = int(input('Введите кол-во фраз, которые нужно сгенерировать'))

phrases = generate_phrases(nouns, verbs, phrase_type, num_phrases)

print('Сгенерированные фразы:')
for phrase in phrases:
    print(phrase)


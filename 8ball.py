import random, sys     
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'To pewne!'
    elif answerNumber == 2:
        return 'Zdecydowanie tak!'
    elif answerNumber == 3:
        return 'Tak'
    elif answerNumber == 4:
        return 'Odpowiedź nie jest pewna'
    elif answerNumber == 5:
        return 'Zapytaj później'
    elif answerNumber == 6:
        return 'Skoncentruj się i zapytaj ponownie'
    elif answerNumber == 7:
        return 'Moja odpowiedź brzmi NIE'
    elif answerNumber == 8:
        return 'To nie wygląda zbyt dobrze'
    elif answerNumber == 9:
        return 'Bardzo wątpliwe'
    

print('Jestem magiczną bilą nr 8')
print('Aby wyjść, wpisz "wyjdź"')
while True:
    r = random.randint(1,9)
    print('Jakie jest twoje pytanie?')
    d = input()
    fortune = getAnswer(r)
    if d != '':
        print (fortune)
    if d == '':
        print('Nie rozumiem pytania.')
    if d == 'wyjdź':
        sys.exit()
        break



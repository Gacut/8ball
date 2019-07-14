import random, sys     

print('''

			        ____
			    ,dP9CGG88@b,
			  ,IP  _   Y888@@b,
			 dIi  (_)   G8888@b
			dCII  (_)   G8888@@b
			GCCIi     ,GG8888@@@
			GGCCCCCCCGGG88888@@@
			GGGGCCCGGGG88888@@@@...
			Y8GGGGGG8888888@@@@P.....
			 Y88888888888@@@@@P......
			 `Y8888888@@@@@@@P'......
			    `@@@@@@@@@P'.......
			        """"........

	  __  __             _         ___    _           _ _ 
	 |  \/  |           (_)       / _ \  | |         | | |
	 | \  / | __ _  __ _ _  ___  | (_) | | |__   __ _| | |
	 | |\/| |/ _` |/ _` | |/ __|  > _ <  | '_ \ / _` | | |
	 | |  | | (_| | (_| | | (__  | (_) | | |_) | (_| | | |
	 |_|  |_|\__,_|\__, |_|\___|  \___/  |_.__/ \__,_|_|_|
	                __/ |                                 
	               |___/                                  
               			Made by Gacut
               			Inspiration: Automate boring stuff with Python - All Siegwart
               			8ball logo made by: http://asciiart.eu
               			Ascii text: http://patorjk.com


''')


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



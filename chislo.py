import random

ptk = 0
name = input('Привет! Как тебя зовут?\n')
number = random.randint(1, 20)
print ('Отлично, {0}. Угадай, какое число я загадал. От 1 до 20'.format(name))

while ptk < 5:
    ch = int(input('Введи число: '))
    ptk += 1

    if ch < number:
        print ('Твое число меньше того, что я загадал.')

    if ch > number:
        print ('Твое число больше загаданного мной.')

    if ch == number:
        break

if ch == number:
    print ('Ух ты, {0}! Ты угадал число, использовав {1} попыток!'.format(name, guesses_made))
else:
    print ('А вот и не угадал! Я загадал число {0}'.format(number))
import random
import logging
logging.basicConfig(level=logging.INFO, filename="py.log", format="%(asctime)s %(levelname)s %(message)s")

while True:
    try:
        n = int(input('Введите число '))
        k = int(input('Введите число попыток '))
        logging.info(f'Введено число {n}')
        logging.info(f'Введено число попыток {k}')
        if n < 1:
            print('Число должно быть больше 1')
            logging.exception('Введённое число меньше еденицы ')
        elif k < 0:
            print('Число должно быть натуральным')
            logging.exception('Введённое число не натуральное ')
        else:
            logging.info('Всё нормально')
            break

    except ValueError:
        print("Необходимо ввести ЧИСЛО ")
        logging.exception("Ошибка")

s = list(range(1,n+1))

comp = random.choice(s)
logging.info(f"Компьютер загадал число {comp}")

p = 1 # Первая попытка
while True:
    while True:
        try:
            x = int(input('Какое число загадал comp? '))
            logging.info(f'попытка {p} Пользователь выбрал число {x}')
            break
        except ValueError:
            print("Необходимо ввести число!")
    if p < k:
        if x < comp:
            print('Ваше число меньше числа comp')
        elif x > comp:
            print('Ваше число больше числа comp')
        elif x == comp:
            print('Вы угадали! Поздравляю!')
            logging.info(f'Число {comp} угадано ')
            break
    else:
        print('Число неверное, ваши попытки закончились')
        logging.info('попытки закончились')
        break
    p += 1

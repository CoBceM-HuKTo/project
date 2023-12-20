
import keyboard, random, time

list_of_problems = []
list_of_solutions = []
file = open('problems.txt', encoding="utf-8").readlines()
for i in file:
    list_of_problems.append(i[:str(i).index('-')].replace(' ', ''))
    list_of_solutions.append(i[str(i).index('-') + 1:].replace(' ', '').replace('\n', ''))
s = 0
d = 0
problems = random.randint(1, 20)
now_problems = []
for i in range(problems):
    pr = random.randint(1, len(list_of_problems) - 1)
    now_problems.append(list_of_problems[pr])

print('Нажмите "ss" чтобы запустить систему')
print('Нажмите "ee" чтобы закончить работу системы')
print('Нажмите "dd" чтобы провести диагностику системы')
print('Нажмите "ff" чтобы устранить проблемы')

while True:
    if keyboard.read_key() == "s" and s != 1:
        print("> Система запущена")
        s += 1
    elif keyboard.read_key() == "d" and s == 1:
        print('> Дагностика... Пожалуйста, подождите...')
        for i in now_problems:
            time.sleep(random.randint(1, 4) / 4)
            print(f'> Обнаружена проблема: "{i}"')
        print(f'> Итого: {problems} проблем')
        print('> Диагностика завершена')
        d = 1
    elif keyboard.read_key() == "f" and s == 1 and d >= 1:
        for i in now_problems:
            time.sleep(random.randint(1, 4) / 4)
            print(f'> Для проблемы "{i}", найдено решение: "{list_of_solutions[list_of_problems.index(i)]}"')
        print('> Все решения найдены')
    elif keyboard.read_key() == "f" and s == 1 and d == 0:
        print('> Проведите диагностику')
    elif keyboard.read_key() == "e" and s == 1:
        print("> Система завершила работу")
        break
    elif s == 0:
        print('> Пожалуйста, запустите систему')
    elif s >= 1 and keyboard.read_key() == "s":
        print('> Система перезапущена')
        d = 0
    else:
        print('> Попробуйте ещё раз или выполните другое действие')

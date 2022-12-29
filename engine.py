import time
import random
import os

locs = ['Опушка леса', 'Родник']
locate = 0
inv = []


def interface():
    global locate, locs, inv
    while True:
        count = 1
        move = int(input('1.О персонаже. 2.О локации. 3.Инвентарь. 4.Перемещение.\n...'))
        if move == 1:
            with open('config.txt', encoding='utf-8') as r:
                print('*'*7, '...Персонаж...', '*'*7)
                print(r.read())
                print('*'*7, '.'*8, '*'*7)
        if move == 2:
            print('*'*7, '...Локация...', '*'*7)
            print(locs[locate])
            print('Опасность:', random.randint(1, 5))
            print('*'*7, '.'*7, '*'*7)
        if move == 3:
            if len(inv) == 0:
                print('*'*7, '...Инвентарь...', '*'*7)
                print('Пусто.')
                print('*'*7, '.'*9, '*'*7)
            else:
                print('*'*7, '...Инвентарь...', '*'*7)
                print(inv)
                print('*'*7, '.'*9, '*'*7)
        if move == 4:
            print('Ты отправляешься в...\n')
            for i in locs:
                print(count, i)
                count+=1
            m = int(input('...'))
            locate = m-1

def login():
    name = input('Как тебя зовут?\n...')
    old = input('Сколько тебе лет?\n...')
    race = input('Рассовая пренадлежность:\n...')
    with open('config.txt', 'w', encoding='utf-8') as r:
        r.write('Имя:'+name+'\n'+'Раса:'+race+'\n'+'Возраст:'+old)
        r.close()



def start():
    login()
    print('Преодолевая жуткую головную боль, ты поднимаешься на ноги и осматриваешься...')
    time.sleep(2)
    print('Ты на опушке леса.')
    interface()


start()




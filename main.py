from random import randint


def attack(char_name, char_class):
    phrase = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return (f'{char_name} {phrase} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {phrase} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {phrase} {5 + randint(-3, -1)}')
    return 1


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return 1


def special(char_name, char_class):
    if char_class == 'warrior':
        skill = 'применил специальное умение «Выносливость'
        return (f'{char_name} {skill} {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return 1


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    attackph = 'attack — чтобы атаковать противника'
    defenceph = 'defence — чтобы блокировать атаку противника'
    specialph = 'special — чтобы использовать свою суперсилу'
    print('Потренируйся управлять своими навыками.')
    print(f'Введи одну из команд: {attackph}, {defenceph} или {specialph}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    var = 'Воитель — warrior'
    mag = 'Маг — mage'
    hel = 'Лекарь — healer'
    charpick = 'Введи название персонажа, за которого хочешь играть'
    inputinf = f'{charpick}: {var}, {mag}, {hel}: '
    while approve_choice != 'y':
        char_class = input(f'{inputinf}')
        if char_class == 'warrior':
            varabil = 'Сильный, выносливый и отважный'
            print(f'Воитель — дерзкий воин ближнего боя. {varabil}.')
        if char_class == 'mage':
            mageabil = 'Обладает высоким интеллектом'
            print(f'Маг — находчивый воин дальнего боя. {mageabil}.')
        if char_class == 'healer':
            healabil = 'Черпает силы из природы, веры и духов'
            print(f'Лекарь — могущественный заклинатель. {healabil}.')
            press = 'Нажми (Y), чтобы подтвердить выбор, '
            press1 = 'или любую другую кнопку, чтобы выбрать другого персонажа'
        approve_choice = input(f'{press}{press1}').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()

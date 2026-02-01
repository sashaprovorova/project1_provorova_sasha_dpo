# labyrinth_game/constants.py
ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. '
        'На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с '
        'запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 
                  'north': 'treasure_room', 'east': 'hidden_kitchen'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет'
        ' после девяти". Введите ответ цифрой или словом.', '10')
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. На стене видна '
          'надпись: "Осторожно — ловушка".',
          'exits': {'west': 'entrance'},
          'items': ['rusty_key'],
          'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" '
          'три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. Где-то '
          'здесь может быть ключ от сокровищницы.',
          'exits': {'east': 'hall', 'north': 'armory', 'west': 'chamber', },
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" '
          '(ответ одно слово)', 'резонанс')  
    },
    'armory': {
          'description': 'Старая оружейная комната. На стене висит меч, рядом — '
          'небольшая бронзовая шкатулка.',
          'exits': {'south': 'library'},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    'treasure_room': {
          'description': 'Комната, на столе большой сундук. Дверь заперта — '
          'нужен особый ключ.',
          'exits': {'south': 'hall'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число'
          ' пятикратного шага, 2*5= ? )', '10')
    },
    'chamber': {
          'description': 'Просторная холодная спальня с затемненным портретом'
          ' на стене и разбитым окном. Ветер колышет разбросанные по полу письма.',
          'exits': {'east': 'library'},
          'items': ['picture', 'letter'],
          'puzzle': ('На одном из писем загадка: Сколько людей изображено на портрете?',
                      '1')
    },
    'hidden_kitchen': {
          'description': 'Только кухонный инвентарь так и остался не тронутым, все '
          'остальное же давно было съедено крысами',
          'exits': {'west': 'hall'},
          'items': ['knife'],
          'puzzle': None
    }
}


COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "look": "осмотреть текущую комнату", 
    "take <item>": "поднять предмет", 
    "use <item>": "использовать предмет из инвентаря", 
    "inventory": "показать инвентарь", 
    "solve": "попытаться решить загадку в комнате", 
    "quit": "выйти из игры", 
    "help": "показать это сообщение"
}

PUZZLE_REWARDS = {
    "hall": None,
    "library": "treasure_key",
    "trap_room": None,
    "chamber": None,
    "treasure_room": None,
}

ANSWER_ALIASES = {
    "10": {"10", "десять"},
    "1": {"1", "один", "одна", "одно"},
    "шаг шаг шаг": {"шаг шаг шаг", "шаг, шаг, шаг", "шаг-шаг-шаг"},
    "резонанс": {"резонанс"},
}

DIRECTIONS = {"north", "south", "east", "west"}

EVENT_PROBABILITY = 10
EVENT_TYPES = 3
TRAP_DEFEAT_THRESHOLD = 3
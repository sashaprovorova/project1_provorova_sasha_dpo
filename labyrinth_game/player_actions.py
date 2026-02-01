from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


def show_inventory(game_state): 
    """ Печатает содержимое инвентаря игрока. """
    
    player_inventory = game_state['player_inventory']
    if player_inventory: 
        print(f"Инвентарь: {player_inventory}")
    else: 
        print("Инвентарь пуст")

def get_input(prompt="> "):
    """ Безопасно читает ввод пользователя, 
    при Ctrl+C/Ctrl+D возвращает quit. """
    
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        # print("\nВыход из игры.")
        return "quit"
  
def move_player(game_state, direction): 
    """ Перемещает игрока по направлению, проверяя доступность 
    выхода и условия входа в treasure_room. """
    
    current_room = game_state["current_room"]
    exits = ROOMS[current_room]["exits"]

    if direction not in exits:
        print("Нельзя пойти в этом направлении.")
        return 

    next_room = exits[direction]
    if (next_room == "treasure_room" 
        and "rusty_key" not in game_state["player_inventory"]):
        print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
        return

    if next_room == "treasure_room" and "rusty_key" in game_state["player_inventory"]:
        print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")

    game_state["current_room"] = next_room
    game_state["steps_taken"] += 1
    describe_current_room(game_state)
    random_event(game_state)
        

def take_item(game_state, item_name): 
    """ Поднимает предмет из комнаты в инвентарь, если он доступен. """
    
    if item_name == "treasure_chest":
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return
    
    current_room = game_state["current_room"]
    items = ROOMS[current_room]["items"]

    if item_name in items:
        game_state["player_inventory"].append(item_name)
        items.remove(item_name)
        print("Вы подняли:", item_name)
    else:
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name): 
    """ Использует предмет из инвентаря и применяет 
    его эффект (если он предусмотрен). """
    
    inventory = game_state["player_inventory"]

    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажигаете факел и вокруг становится чуть светлее.")
    elif item_name == "sword":
        print("Вы крепко сжимаете меч и чувствуете быстро прибавляющуюся уверенность.")
    elif item_name == "bronze_box":
        if "rusty_key" not in inventory:
            print("Вы открываете шкатулку.")
            inventory.append("rusty_key")
    else:
        print("Вы не знаете, как использовать этот предмет.")
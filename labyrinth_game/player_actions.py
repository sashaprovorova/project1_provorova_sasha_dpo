from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


def show_inventory(game_state): 
    player_inventory = game_state['player_inventory']
    if player_inventory: 
        print(f"Инвентарь: {player_inventory}")
    else: 
        print("Инвентарь пуст")

def get_input(prompt="> "):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        # print("\nВыход из игры.")
        return "quit"
  
def move_player(game_state, direction): 
    current_room = game_state["current_room"]
    exits = ROOMS[current_room]["exits"]

    if direction in exits:
        game_state["current_room"] = exits[direction]
        game_state["steps_taken"] += 1
        describe_current_room(game_state)
        random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")

def take_item(game_state, item_name): 
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
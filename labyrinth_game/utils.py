import math

from labyrinth_game.constants import ANSWER_ALIASES, PUZZLE_REWARDS, ROOMS


def describe_current_room(game_state): 
    current_room = game_state['current_room']
    room_info = ROOMS[current_room]

    print(f"== {current_room.upper()} ==")
    print(room_info["description"])

    items = room_info["items"]
    if items: 
        print("Заметные предметы:", ", ".join(items))

    exits = room_info["exits"]
    print("Выходы:", ", ".join(exits.keys()))

    puzzle = room_info["puzzle"]
    if puzzle: 
        print("Кажется, здесь есть загадка (используйте команду solve).")   

def solve_puzzle(game_state): 
    current_room = game_state["current_room"]
    room_info = ROOMS[current_room]

    if not room_info["puzzle"]:
        print("Загадок здесь нет.")
        return

    puzzle = room_info["puzzle"]
    question = puzzle[0]
    correct_answer = str(puzzle[1]).strip().lower()
    
    print(question)

    user_answer = input("Ваш ответ: ").strip().lower()
    accepted_answers = ANSWER_ALIASES.get(correct_answer, {correct_answer})

    if user_answer in accepted_answers:
        print("Верно! Загадка решена.")
        room_info["puzzle"] = None 

        reward = PUZZLE_REWARDS.get(current_room)
        if reward and reward not in game_state["player_inventory"]:
            game_state["player_inventory"].append(reward)
            print(f"Награда получена: {reward}")
        return
    elif current_room == "trap_room":
        trigger_trap(game_state)
    else:
        print("Неверно. Попробуйте снова.")
    

def attempt_open_treasure(game_state): 
    current_room = game_state["current_room"]

    if current_room != "treasure_room":
        print("Здесь нет сундука с сокровищами.")
        return

    room_info = ROOMS[current_room]
    items = room_info["items"]

    if "treasure_key" in game_state["player_inventory"]:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        if "treasure_chest" in items:
            items.remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    answer = input("Сундук заперт. Ввести код? (да/нет): ").strip().lower()
    if answer != "да":
        print("Вы отступаете от сундука.")
        return

    if not room_info["puzzle"]:
        print("Кода нет — загадка уже решена или отсутствует.")
        return

    _, correct_code = room_info["puzzle"]
    user_code = input("Введите код: ").strip().lower()
    correct_code = str(correct_code).strip().lower()
    accepted_codes = ANSWER_ALIASES.get(correct_code, {correct_code})

    if user_code in accepted_codes:
        print("Код верный! Замок открыт.")
        room_info["puzzle"] = None
        if "treasure_chest" in items:
            items.remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
    else:
        print("Неверный код.")

def show_help(commands):
    print("\nДоступные команды:")
    for cmd, desc in commands.items(): 
        print(f"  {cmd:<16} {desc}")

def pseudo_random(seed, modulo): 
    if modulo <= 0:
        return 0

    x = math.sin(seed * 12.9898) * 43758.5453
    div = x - math.floor(x)
    return int(div * modulo)

def trigger_trap(game_state): 
    print("Ловушка активирована! Пол стал дрожать...")

    inventory = game_state["player_inventory"]
    steps = game_state["steps_taken"]

    if inventory:
        random_idx = pseudo_random(steps, len(inventory))
        lost_item = inventory.pop(random_idx)
        print(f"Вы потеряли предмет: {lost_item}")
        return

    roll = pseudo_random(steps, 10)  
    if roll < 3:
        print("Вы провалились и проиграли.")
        game_state["game_over"] = True
    else:
        print("Вам удалось удержаться. Вы уцелели.")

def random_event(game_state): 
    steps = game_state["steps_taken"]

    happens = pseudo_random(steps, 10)
    if happens != 0:
        return

    event_type = pseudo_random(steps + 1, 3) 

    current_room = game_state["current_room"]
    room_info = ROOMS[current_room]

    if event_type == 0:
        print("Вы находите на полу монетку.")
        room_items = room_info["items"]
        if "coin" not in room_items:
            room_items.append("coin")
        return
    
    if event_type == 1:
        print("Вы слышите неизвестный шорох...")
        if "sword" in game_state["player_inventory"]:
            print("Вы достаёте меч, отпугивая существо в темноте.")
        return
    
    if event_type == 2:
        if (current_room == "trap_room" 
            and "torch" not in game_state["player_inventory"]):
            print("Вы чувствуете опасность... это ловушка!")
            trigger_trap(game_state)



from labyrinth_game.constants import ROOMS
from labyrinth_game.player_actions import get_input


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

    user_answer = get_input("Ваш ответ: ").strip().lower()

    if user_answer == correct_answer:
        print("Верно! Загадка решена.")
        room_info["puzzle"] = None 

        if "treasure_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("treasure_key")
            print("Награда получена: treasure_key")
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

    if user_code == correct_code:
        print("Код верный! Замок открыт.")
        room_info["puzzle"] = None
        if "treasure_chest" in items:
            items.remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
    else:
        print("Неверный код.")


def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")
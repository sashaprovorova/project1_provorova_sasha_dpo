#!/usr/bin/env python3
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)


def process_command(game_state, command): 
    parts = command.split()
    instruction = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    match instruction:
        case "look":
            describe_current_room(game_state)

        case "inventory":
            show_inventory(game_state)

        case "go":
            if not arg:
                print("Укажите направление: go north/south/east/west")
                return
            move_player(game_state, arg)

        case "take":
            if not arg:
                print("Укажите предмет: take <item>")
                return
            take_item(game_state, arg)

        case "use":
            if not arg:
                print("Укажите предмет: use <item>")
                return
            use_item(game_state, arg)
        case "solve":
            if game_state["current_room"] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)

        case "help":
            show_help()

        case "quit" | "exit":
            game_state["game_over"] = True
            print("Выход из игры.")

        case _:
            print("Неизвестная команда.")

def main() -> None:
    game_state = {
        'player_inventory': [],
        'current_room': 'entrance', 
        'game_over': False, 
        'steps_taken': 0 
    }
    
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state["game_over"]: 
        instruction = get_input("> ").strip()
        if not instruction: 
            continue
        process_command(game_state, instruction)

if __name__ == "__main__":
    main()
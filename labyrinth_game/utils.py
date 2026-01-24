from labyrinth_game.constants import ROOMS


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
    


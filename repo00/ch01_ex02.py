# v0.0.5

# TODO: show_theme_message

# TODO: show_game_mission

# TODO: reset_health_meter

# TODO: occupy_huts

# TODO: process_user_choice

def reveal_occupants(idx, huts):
    """"Print the occupants of the hut"""
    msg = ""
    print("Revealing occupants...")
    for i in range(len(huts)):
        occupant_info ="<%d:%s>" % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

# TODO: enter_hut

def run_application():
    """Top level control function for running the application"""
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")

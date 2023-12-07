from assets.interface import *
from assets.settings import *

# Code uses case match, which requies python 3.10+


def activate_game():
    title_game()

    while True:
        user_choice = start_menu()
        
        match user_choice:
            case "1": start_game_menu()
            case "2": settings_menu()
            case "3": exit()

if __name__ == "__main__":
    activate_game()
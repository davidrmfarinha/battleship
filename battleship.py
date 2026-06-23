import sys
import os
import random
from readchar import readkey, key
from time import sleep, time
from termcolor import colored
from nava import play
import shutil

game_title = [
    "███████╗ ██████╗██╗  ██╗██╗███████╗███████╗███████╗    ██╗   ██╗███████╗██████╗ ███████╗███████╗███╗   ██╗██╗  ██╗███████╗███╗   ██╗",
    "██╔════╝██╔════╝██║  ██║██║██╔════╝██╔════╝██╔════╝    ██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║██║ ██╔╝██╔════╝████╗  ██║",
    "███████╗██║     ███████║██║█████╗  █████╗  █████╗      ██║   ██║█████╗  ██████╔╝███████╗█████╗  ██╔██╗ ██║█████╔╝ █████╗  ██╔██╗ ██║",
    "╚════██║██║     ██╔══██║██║██╔══╝  ██╔══╝  ██╔══╝      ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  ██║╚██╗██║██╔═██╗ ██╔══╝  ██║╚██╗██║",
    "███████║╚██████╗██║  ██║██║██║     ██║     ███████╗     ╚████╔╝ ███████╗██║  ██║███████║███████╗██║ ╚████║██║  ██╗███████╗██║ ╚████║",
    "╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝",
]

battleship = [
    "                                              |__                                                ",
    "                                              |\/                                                ",
    "                                              ---                                                ",
    "                                              / | [                                              ",
    "                                       !      | |||                                              ",
    "                                     _/|     _/|-++'                                             ",
    "                                 +  +--|    |--|--|_ |-                                          ",
    "                              { /|__|  |/\__|  |--- |||__/                                       ",
    "                             +---------------___[}-_===_.'____                 /\                ",
    "                         ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _            ",
    "          __..._____--==/___]_|__|_____________________________[___\==--____,------' .7          ",
    "         |                                                                     BB-61/            ",
    "          \_________________________________________________________________________|            ",
    "  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww   ",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW ",
    "  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww   ",
]

start_string = [
    "┏━╸┏┓╻╺┳╸┏━╸┏━┓   ╺━┓╻ ╻┏┳┓   ┏━┓╺┳╸┏━┓┏━┓╺┳╸┏━╸┏┓╻",
    "┣╸ ┃┗┫ ┃ ┣╸ ┣┳┛   ┏━┛┃ ┃┃┃┃   ┗━┓ ┃ ┣━┫┣┳┛ ┃ ┣╸ ┃┗┫",
    "┗━╸╹ ╹ ╹ ┗━╸╹┗╸   ┗━╸┗━┛╹ ╹   ┗━┛ ╹ ╹ ╹╹┗╸ ╹ ┗━╸╹ ╹",
]

name_prompt_string = [
    "┏┓╻┏━┓┏┳┓┏━╸   ┏━╸╻┏┓╻┏━╸┏━╸┏┓ ┏━╸┏┓╻   ╻ ╻┏┓╻╺┳┓   ┏━╸┏┓╻╺┳╸┏━╸┏━┓   ╺━┓╻ ╻┏┳┓   ┏━┓╺┳╸┏━┓┏━┓╺┳╸",
    "┃┗┫┣━┫┃┃┃┣╸    ┣╸ ┃┃┗┫┃╺┓┣╸ ┣┻┓┣╸ ┃┗┫   ┃ ┃┃┗┫ ┃┃   ┣╸ ┃┗┫ ┃ ┣╸ ┣┳┛   ┏━┛┃ ┃┃┃┃   ┗━┓ ┃ ┣━┫┣┳┛ ┃ ",
    "╹ ╹╹ ╹╹ ╹┗━╸   ┗━╸╹╹ ╹┗━┛┗━╸┗━┛┗━╸╹ ╹   ┗━┛╹ ╹╺┻┛   ┗━╸╹ ╹ ╹ ┗━╸╹┗╸   ┗━╸┗━┛╹ ╹   ┗━┛ ╹ ╹ ╹╹┗╸ ╹ ",
]

symbols = {
    "sea": 8779,
    "sea2": 8777,
    "ship": 9972,
    "anchor": 9875,
    "target": 9711,
    "circled_dot": 8857,
    "explosion": 10041,
    "cross_mark": 10006,
    "skull": 9760,
    "circle_miss": 9675,
    "forbidden": 9940,
    "red_x": 10060,
    "green_x": 10062,
}


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


sounds = {
    "cannon": resource_path("assets/cannon.wav"),
    "explosion": resource_path("assets/explosion3.wav"),
    "watersplash": resource_path("assets/watersplash2.wav"),
    "click": resource_path("assets/click2.wav"),
    "applause": resource_path("assets/applause3.wav"),
    "boo": resource_path("assets/boo.wav"),
}

for symbol in symbols:
    symbols[symbol] = chr(symbols[symbol])


pieces = {
    "carrier": {
        "name": "carrier",
        "size": 5,
    },
    "battleship": {
        "name": "battleship",
        "size": 4,
    },
    "cruiser": {
        "name": "cruiser",
        "size": 3,
    },
    "submarine": {
        "name": "submarine",
        "size": 3,
    },
    "destroyer": {
        "name": "destroyer",
        "size": 2,
    },
}


piece_colors = {
    "red": (255, 0, 0),
    "yellow": (255, 255, 0),
    "limegreen": (50, 205, 50),
    "magenta": (255, 0, 255),
    "darkorange": (255, 140, 0),
}

letter_keys = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def color_sea(string):
    return colored(string, (65, 105, 225), attrs=["bold"])


def color_reverse(string, colour):
    return colored(string, colour, attrs=["reverse"])


def select_symbol_to_print(cell, index, index2, player, match):
    sea_block = f" {chr(127754)} "
    sea_block2 = colored(
        f"{chr(8779) + chr(8779):^4}",
        (65, 105, 225),
        attrs=["bold"],
    )
    hit_water_block = f" {chr(128166)} "
    explosion = f" {chr(128165)} "
    sunk_ship = f" {chr(128128)} "
    ship = f' {colored(symbols["ship"], cell["symbol_color"])}  '

    if player.status == "player1":
        if cell["shot"]:
            if cell["occupied"]:
                if cell["destroyed"]:
                    return sunk_ship
                else:
                    return explosion
            else:
                return hit_water_block
        else:
            if cell["occupied"]:
                return f' {colored(symbols["ship"], cell["symbol_color"])}  '
            else:
                return sea_block2
    else:
        cursor_position = match.player1.cursor
        if cursor_position == (index, index2):
            cursor = 10060 if cell["shot"] else 10062
            return f" {chr(cursor)} "
        else:
            if cell["shot"]:
                if cell["occupied"]:
                    if cell["destroyed"]:
                        return sunk_ship
                    else:
                        return explosion
                else:
                    return hit_water_block
            else:
                return sea_block2


# Shot on water 128167 or 128166
# Fazer piças 128405
# forbidden 128683
# ship 128674  9973 9972
# Bóia 128735
# devil 128121
# coco 128169
# crown 128081
# trevo 127808
# star 11088 127775
# wave 127754


# This function generates a list of Strings that represents the current state of the board of one/each player;
def draw_board(player, match):
    board_width = 65
    player_board = []

    def color_main(string):
        return colored(string, player.color, attrs=["reverse"])

    def color_sec(string):
        return colored(string, player.sec_color)

    def color_outer_frame(string):
        return colored(string, player.sec_color, attrs=["reverse", "bold"])

    # This block is used to create the outside frame of the board
    outer_block = color_outer_frame(f'{"":^3}')
    ###############################################################################################
    color_now_playing = "black" if match.now_playing.name == player.name else "white"
    color_now_playing_block = colored(
        f'{" " * 3}',
        color_now_playing,
        attrs=["reverse", "bold"],
    )
    string_now_playing_frame = colored(
        f'{" " * (board_width + 6)}',
        color_now_playing,
        attrs=["reverse", "bold"],
    )
    # This is the string that represents the top and bottom parts of the outside frame. It shows the name of the player and is shown on the top and bottom of the board;
    string_name_row = (
        color_now_playing_block
        + color_outer_frame(f"{player.name:^{board_width}}")
        + color_now_playing_block
    )
    ###############################################################################################
    string_no_name_row = (
        color_now_playing_block
        + color_outer_frame(" " * board_width)
        + color_now_playing_block
    )
    # This is the string that represents the top and bottom parts of the inner outside frame. It shows the letters from A to J,
    string_first_row = color_now_playing_block + outer_block + color_main(f'{" ":<6}')
    # using unicode characters to show the letters from A to J (special unicode characters);
    for x in range(127312, 127322):
        string_first_row += color_main(f"{chr(x):<{5 if x < (127322 - 1) else 8}}")
    string_first_row += outer_block
    string_first_row += color_now_playing_block
    ###############################################################################################
    no_values_row = (
        color_now_playing_block
        + outer_block
        + color_main(" ") * 3
        + color_sec(" +")
        + color_sec("-") * 49
        + color_sec("+ ")
        + color_main(" ") * 3
        + outer_block
        + color_now_playing_block
    )
    ###############################################################################################

    player_board.append(string_now_playing_frame)

    player_board.append(string_name_row)
    player_board.append(string_first_row)

    for index, row in enumerate(player.board):
        real_index = index + 120813
        # Starting the row with its correspondent number
        values_row = color_now_playing_block + outer_block
        values_row += (
            f'{color_main(f"{chr(real_index):>2} ")} '
            if index != 9
            else f'{color_main(f"{chr(120813)}{chr(120812)} ")} '
        )

        for index2, cell in enumerate(row):
            row_length = len(row) - 1

            to_print = select_symbol_to_print(cell, index, index2, player, match)

            values_row += (
                (color_sec("|") + to_print)
                if index2 != row_length
                else (color_sec("|") + to_print) + color_sec("| ")
            )

        values_row += (
            color_main(f" {chr(real_index)} ")
            if index != 9
            else color_main(f"{chr(120813)}{chr(120812)} ")  # End of row
        )
        values_row += outer_block + color_now_playing_block
        player_board.append(no_values_row)
        player_board.append(values_row)

    player_board.append(no_values_row)
    player_board.append(string_first_row)
    player_board.append(string_no_name_row)

    # This could be a new function
    strings_ships_names = player.pieces.keys()
    word_width = int(board_width / 5)
    new_string = color_now_playing_block
    for ship in strings_ships_names:
        ship_is_destroyed = not player.pieces[
            ship
        ]  # Checking if list is empty with marvelous Python syntax
        ship_color = "red" if ship_is_destroyed else "green"
        new_string += colored(
            f"{ship:^{word_width}}", ship_color, attrs=["reverse", "bold"]
        )
        f"{ship:^{word_width}}"
    new_string += color_now_playing_block
    player_board.append(new_string)
    player_board.append(string_now_playing_frame)

    return player_board


player_playing_message = [
    " ┏┓┏━╸╺┳╸╺━┓╺┳╸   ╻┏━┓╺┳╸   ╺┳┓┏━╸┏━┓   ┏━┓┏━┓╻┏━╸╻  ┏━╸┏━┓   ╺┳┓┏━┓┏━┓┏┓╻ ",
    "  ┃┣╸  ┃ ┏━┛ ┃    ┃┗━┓ ┃     ┃┃┣╸ ┣┳┛   ┗━┓┣━┛┃┣╸ ┃  ┣╸ ┣┳┛    ┃┃┣┳┛┣━┫┃┗┫ ",
    "┗━┛┗━╸ ╹ ┗━╸ ╹    ╹┗━┛ ╹    ╺┻┛┗━╸╹┗╸   ┗━┛╹  ╹┗━╸┗━╸┗━╸╹┗╸   ╺┻┛╹┗╸╹ ╹╹ ╹╹",
]

cpu_playing_message = [
    " ┏┓┏━╸╺┳╸╺━┓╺┳╸   ╻┏━┓╺┳╸   ╺┳┓╻┏━╸   ┏━╸┏━┓╻ ╻   ╺┳┓┏━┓┏━┓┏┓╻",
    "  ┃┣╸  ┃ ┏━┛ ┃    ┃┗━┓ ┃     ┃┃┃┣╸    ┃  ┣━┛┃ ┃    ┃┃┣┳┛┣━┫┃┗┫",
    "┗━┛┗━╸ ╹ ┗━╸ ╹    ╹┗━┛ ╹    ╺┻┛╹┗━╸   ┗━╸╹  ┗━┛   ╺┻┛╹┗╸╹ ╹╹ ╹",
]

player_won_message = [
    "╺┳┓┏━┓┏━┓   ┏━┓┏━┓╻┏━╸╻     ╻┏━┓╺┳╸   ╻ ╻┏━┓┏━┓┏┓ ┏━╸╻    ╺┳┓╻ ╻   ╻ ╻┏━┓┏━┓╺┳╸   ┏━╸┏━╸╻ ╻┏━┓┏┓╻┏┓╻┏━╸┏┓╻╻",
    " ┃┃┣━┫┗━┓   ┗━┓┣━┛┃┣╸ ┃     ┃┗━┓ ┃    ┃┏┛┃ ┃┣┳┛┣┻┓┣╸ ┃     ┃┃┃ ┃   ┣━┫┣━┫┗━┓ ┃    ┃╺┓┣╸ ┃╻┃┃ ┃┃┗┫┃┗┫┣╸ ┃┗┫╹",
    "╺┻┛╹ ╹┗━┛   ┗━┛╹  ╹┗━╸┗━╸   ╹┗━┛ ╹    ┗┛ ┗━┛╹┗╸┗━┛┗━╸╹╹   ╺┻┛┗━┛   ╹ ╹╹ ╹┗━┛ ╹    ┗━┛┗━╸┗┻┛┗━┛╹ ╹╹ ╹┗━╸╹ ╹╹",
]

cpu_won_message = [
    "┏━┓┏━┓╻┏━╸╻     ╻ ╻┏━┓┏━┓┏┓ ┏━╸╻    ╺┳┓╻ ╻   ╻ ╻┏━┓┏━┓╺┳╸   ╻ ╻┏━╸┏━┓╻  ┏━┓┏━┓┏━╸┏┓╻╻   ╻  ┏━┓┏━┓┏━╸┏━┓╻╻╻",
    "┗━┓┣━┛┃┣╸ ┃     ┃┏┛┃ ┃┣┳┛┣┻┓┣╸ ┃     ┃┃┃ ┃   ┣━┫┣━┫┗━┓ ┃    ┃┏┛┣╸ ┣┳┛┃  ┃ ┃┣┳┛┣╸ ┃┗┫╹   ┃  ┃ ┃┗━┓┣╸ ┣┳┛╹╹╹",
    "┗━┛╹  ╹┗━╸┗━╸   ┗┛ ┗━┛╹┗╸┗━┛┗━╸╹╹   ╺┻┛┗━┛   ╹ ╹╹ ╹┗━┛ ╹    ┗┛ ┗━╸╹┗╸┗━╸┗━┛╹┗╸┗━╸╹ ╹╹   ┗━╸┗━┛┗━┛┗━╸╹┗╸╹╹╹",
]


# This is a simple helper function. It just renders an array of strings stretched to a specific width
def render_array_strings(array_strings, length, color):
    for string in array_strings:
        print(colored(f"{string:^{length}}", color, attrs=["bold"]))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    # print("\033[H\033[J", end="")


def enoughScreen(columns, rows):
    return columns >= 160 and rows >= 40


def find_middle_of_screen(start, end, length):
    space_available = end - start
    return start + (round(space_available / 2) - round(length / 2))


def default_screen(elements, rows):
    game_screen = []
    for index in range(rows):
        if 0 <= index < 2:
            game_screen.append(elements["top_bottom_row"])
        elif 3 <= index < 3 + len(game_title):
            game_screen.append(
                f'{elements["outer_block"]}{colored(game_title[index - 3], (0, 191, 255)):^{elements["middle_space"] + 21}}{elements["outer_block"]}'
            )
        elif 10 <= index < 12:
            game_screen.append(elements["top_bottom_row"])
        elif rows - 2 <= index < rows:
            game_screen.append(elements["top_bottom_row"])
        else:
            game_screen.append(elements["middle_row"])
    return game_screen


def start_screen(game_screen, elements, columns, rows):
    start_string_position = find_middle_of_screen(
        18 + len(battleship), rows - 3, len(start_string)
    )
    for index in range(rows):
        if start_string_position <= index < start_string_position + len(start_string):
            game_screen[index] = (
                f'{elements["outer_block"]}{(f"{colored(start_string[index - start_string_position], (0, 191, 255))}").center(elements["middle_space"] + 21)}{elements["outer_block"]}'
            )
        elif 18 <= index < 18 + len(battleship):
            game_screen[index] = (
                f'{elements["outer_block"]}{colored(battleship[index - 18], (0, 191, 255)):^{elements["middle_space"] + 21}}{elements["outer_block"]}'
            )

    return game_screen


def enter_name_screen(match, game_screen, elements, columns, rows):
    for index in range(rows):
        if 38 <= index < 38 + len(name_prompt_string):
            game_screen[index] = (
                f'{elements["outer_block"]}{(f"{colored(name_prompt_string[index - 38], (0, 191, 255))}").center(elements["middle_space"] + 21)}{elements["outer_block"]}'
            )
        elif index == 42:
            game_screen[index] = (
                f'{elements["outer_block"]}{(match.player_name + colored("|", "white")).center(elements["middle_space"] + 13)}{elements["outer_block"]}'
            )
    return game_screen


def game_board_screen(match, game_screen, elements, columns, rows):

    message_to_display = None
    if match.over:
        message_to_display = (
            cpu_won_message
            if match.winner.type_of_player == "cpu"
            else player_won_message
        )
    else:
        message_to_display = (
            cpu_playing_message
            if match.now_playing.type_of_player == "cpu"
            else player_playing_message
        )
    ###############################################################################################
    current_player = match.player1
    current_player_board = draw_board(current_player, match)
    ###############################################################################################
    opponent = match.player2
    oponnent_board = draw_board(opponent, match)
    ###############################################################################################
    space_to_center = int((columns / 2 - (elements["frame_width"] * 1.5) - 71) / 2)
    string_space_to_center = " " * space_to_center
    start_point_boards = find_middle_of_screen(19, rows - 2, len(current_player_board))

    for index in range(13, 13 + len(message_to_display)):
        game_screen[index] = (
            f'{elements["outer_block"]}{message_to_display[index - 13]:^{elements["middle_space"]}}{elements["outer_block"]}'
        )
    game_screen[17] = elements["top_bottom_row"]
    game_screen[18] = elements["top_bottom_row"]
    for index in range(19, rows - 2):
        if start_point_boards <= index < start_point_boards + len(current_player_board):
            game_screen[index] = (
                f'{elements["outer_block"]}{string_space_to_center}{current_player_board[index - start_point_boards]}{string_space_to_center}{elements["outer_block"]}{string_space_to_center}{oponnent_board[index - start_point_boards]}{string_space_to_center}{elements["outer_block"]}'
            )
        else:
            game_screen[index] = elements["divided_middle_row"]

    return game_screen


def draw_game_screen(match, columns, rows):

    frame_width = 4
    middle_space = columns - 2 * frame_width
    divided_middle_row_space = (columns - 3 * frame_width) / 2
    outer_block = colored(" ", (0, 0, 128), attrs=["reverse"]) * frame_width

    screen_elements = {
        "frame_width": frame_width,
        "outer_block": colored(" ", (0, 0, 128), attrs=["reverse"]) * frame_width,
        "middle_space": columns - 2 * frame_width,
        "divided_middle_row_space": (columns - 3 * frame_width) / 2,
        "top_bottom_row": colored(" ", (0, 0, 128), attrs=["reverse"]) * columns,
        "middle_row": f'{outer_block}{" ":^{middle_space}}{outer_block}',
        "divided_middle_row": f'{outer_block}{" ":^{divided_middle_row_space}}{outer_block}{" ":^{divided_middle_row_space}}{outer_block}',
    }

    game_screen = default_screen(screen_elements, rows)

    match match.current_screen:
        case "start_screen":
            return start_screen(game_screen, screen_elements, columns, rows)
        case "enter_name_screen":
            return enter_name_screen(match, game_screen, screen_elements, columns, rows)
        case "game_screen":
            return game_board_screen(match, game_screen, screen_elements, columns, rows)


def print_game_screen(match, columns, rows):
    game_screen_list = draw_game_screen(match, columns, rows)
    game_screen_string = "\n".join("".join(row) for row in game_screen_list)
    clear_screen()

    print(game_screen_string)
    if match.current_sound != None:
        play(match.current_sound)
        match.current_sound = None


def render_game_screen(match):
    columns, rows = shutil.get_terminal_size()
    if columns % 2 != 0:
        columns -= 1
    rows -= 1

    if enoughScreen(columns, rows):
        print_game_screen(match, columns, rows)
    else:
        clear_screen()
        print(
            "Fenster nicht groß genug. Bitte drücken Sie F11, um den Vollbildmodus zu aktivieren."
        )
        while True:
            sleep(1)
            new_columns, new_rows = shutil.get_terminal_size()
            if enoughScreen(new_columns, new_rows):
                return render_game_screen(match)


# Helper function to generate a set of random coordinates to help populate the board
def generate_random_coords():
    return (random.randint(0, 9), random.randint(0, 9))


def populate_board():
    board = []
    for x in range(10):
        board.append([])
        for _ in range(10):
            board[x].append(
                {
                    "occupied": False,
                    "occupied_by": None,
                    "shot": False,
                    "destroyed": False,
                    "symbol": color_sea(symbols["sea"]),
                    "symbol_color": None,
                }
            )
    return board


def generate_piece_coords(piece_size):
    piece_coords = [generate_random_coords()]
    operand = (
        -1
        if (random.random() < 0.5)
        else 1
        # Operand tells if piece generation goes forwards or backwards according to direction (horizontal or vertical);
    )
    direction = "vertical" if (random.random() < 0.5) else "horizontal"
    piece_coords.extend(
        (
            (piece_coords[0][0], piece_coords[0][1] + (x + 1) * operand)
            if direction == "horizontal"
            else (piece_coords[0][0] + (x + 1) * operand, piece_coords[0][1])
        )
        for x in range(piece_size - 1)
    )
    return piece_coords


def is_off_limit(coordinate):
    return not (0 <= coordinate[0] < 10) or not (0 <= coordinate[1] < 10)


# This function checks if all the coordinates of the randomly generated piece fit in the board. It checks if they're off limit and if the cell in the board is already occupied;
def all_coords_valid(piece_coords, board):
    list_of_already_occupied_cells = []
    for coord in piece_coords:
        if is_off_limit(coord):
            return False
        list_of_already_occupied_cells.append(board[coord[0]][coord[1]]["occupied"])
    return not (any(list_of_already_occupied_cells))


# This function places each individual piece on the board. It must receive an array of coords in tuple form: (coordy, coordx)
def place_pieces(player, piece_coords, piece_color, piece_name):
    player.pieces[piece_name] = piece_coords
    for coord in piece_coords:
        player.board[coord[0]][coord[1]]["symbol"] = colored(
            symbols["ship"], piece_color
        )
        player.board[coord[0]][coord[1]]["occupied"] = True
        player.board[coord[0]][coord[1]]["occupied_by"] = piece_name
        player.board[coord[0]][coord[1]]["symbol_color"] = piece_color


def randomly_place_pieces_on_board(player):
    # deciding order of pieces; The function random.sample is very handy for this
    list_of_pieces = random.sample(list(pieces.keys()), k=5)
    list_of_colors = random.sample(list(piece_colors.keys()), k=5)
    for index, piece in enumerate(list_of_pieces):
        piece_size = pieces[piece]["size"]
        piece_name = pieces[piece]["name"]
        piece_color = piece_colors[list_of_colors[index]]
        while True:
            piece_coords = generate_piece_coords(piece_size)
            if all_coords_valid(piece_coords, player.board):
                place_pieces(player, piece_coords, piece_color, piece_name)
                break
            else:
                continue


up = {"ref": key.UP, "type of": "movement", "operation": (-1, 0)}
right = {"ref": key.RIGHT, "type of": "movement", "operation": (0, 1)}
down = {"ref": key.DOWN, "type of": "movement", "operation": (1, 0)}
left = {"ref": key.LEFT, "type of": "movement", "operation": (0, -1)}
enter = {"ref": key.ENTER, "type of": "confirm"}
space = {"ref": key.SPACE, "type of": "confirm"}

allowed_keys_in_game = [up, right, left, down, enter, space]


# This function checks if the given input is valid (it must be included in the list of allowed_keys_in_game);
def is_input_valid(input):
    return any(input == key["ref"] for key in allowed_keys_in_game)


# This function returns a dictionary that represents a key pressed;
def process_input(input):
    for key in allowed_keys_in_game:
        if input == key["ref"]:
            return key


# Using module readkey() to get player input and running indefinitely until player gives acceptable input
def get_player_input():
    while True:
        key_pressed = readkey()
        if is_input_valid(key_pressed):
            return process_input(key_pressed)
        else:
            continue


# Checking if the cell (determined by the coords cursor position) in the provided player board was already shot, returning true if yes or false if no;
def already_shot(player, coords):
    cell_pointed_by_cursor = player.board[coords[0]][coords[1]]
    return cell_pointed_by_cursor["shot"]


def mark_ship_as_destroyed(player_that_got_hit, ship_that_got_hit_name):
    hit_player_board = player_that_got_hit.board
    for row in player_that_got_hit.board:
        for cell in row:
            if cell["occupied_by"] == ship_that_got_hit_name:
                cell["destroyed"] = True


# This function manages a successful shot.
def process_successful_shot(player_that_got_hit, coords, cell_that_got_hit):
    ship_that_got_hit_name = cell_that_got_hit["occupied_by"]
    ship_that_got_hit = player_that_got_hit.pieces[ship_that_got_hit_name]
    player_that_got_hit.pieces[ship_that_got_hit_name] = list(
        filter(lambda x: x != coords, ship_that_got_hit)
    )
    if not player_that_got_hit.pieces[ship_that_got_hit_name]:
        mark_ship_as_destroyed(player_that_got_hit, ship_that_got_hit_name)


def shoot(match, player_that_got_hit, coords):
    match.current_sound = sounds["cannon"]
    render_game_screen(match)
    cell_that_got_hit = player_that_got_hit.board[coords[0]][coords[1]]
    cell_that_got_hit["shot"] = True  # Changing the status of the cell
    successfully_hit_a_target = cell_that_got_hit["occupied"]  # Boolean value
    if successfully_hit_a_target:
        process_successful_shot(player_that_got_hit, coords, cell_that_got_hit)
        match.current_sound = sounds["explosion"]
    else:
        match.current_sound = sounds["watersplash"]


def human_turn(match):
    now_playing = match.now_playing
    opponent = match.player_order[1]

    while True:
        render_game_screen(match)

        player_input = get_player_input()
        # Logic for movement of the cursor across opponent's board;
        if player_input["type of"] == "movement":
            # The movement operation to execute is calculated adding the respective tuple from the key pressed to the current coordinates (This comment is confusing!! I must change it)
            operation_to_execute = player_input["operation"]
            new_y_coord = now_playing.cursor[0] + operation_to_execute[0]
            new_x_coord = now_playing.cursor[1] + operation_to_execute[1]
            if not (is_off_limit((new_y_coord, new_x_coord))):
                now_playing.cursor = (new_y_coord, new_x_coord)
                match.current_sound = sounds["click"]
        # Logic for when player presses enter or space to make a valid shot
        elif player_input["type of"] == "confirm":
            y_cursor_coord, x_cursor_coord = now_playing.cursor
            cursor_coords = (y_cursor_coord, x_cursor_coord)

            if not (already_shot(opponent, cursor_coords)):
                shoot(match, opponent, cursor_coords)
                break  # The turn only ends when player makes a shoot move;
    render_game_screen(match)


def coord_valid(coords, board):
    cell_already_hit = False
    coords_off_limit = is_off_limit((coords[0], coords[1]))
    if not coords_off_limit:
        cell_already_hit = board[coords[0]][coords[1]]["shot"]
    return not cell_already_hit and not coords_off_limit


def process_next_coords(found_ship_coords, opponent):
    new_coords_vertical_up = []
    new_coords_vertical_down = []
    new_coords_horizontal_right = []
    new_coords_horizontal_left = []
    # vertical
    for x in range(5):
        real_index = x + 1
        # Going down
        new_coord_down = (found_ship_coords[0] + real_index, found_ship_coords[1])
        if coord_valid(new_coord_down, opponent.board):
            new_coords_vertical_up.append(new_coord_down)
        # Going up
        new_coord_up = (found_ship_coords[0] - real_index, found_ship_coords[1])
        if coord_valid(new_coord_up, opponent.board):
            new_coords_vertical_down.append(new_coord_up)
        # Going right
        new_coord_right = (found_ship_coords[0], found_ship_coords[1] + real_index)
        if coord_valid(new_coord_right, opponent.board):
            new_coords_horizontal_right.append(new_coord_right)
        # going left
        new_coord_left = (found_ship_coords[0], found_ship_coords[1] - real_index)
        if coord_valid(new_coord_left, opponent.board):
            new_coords_horizontal_left.append(new_coord_left)
    return {
        "new_coords_vertical_down": new_coords_vertical_down,
        "new_coords_vertical_up": new_coords_vertical_up,
        "new_coords_horizontal_right": new_coords_horizontal_right,
        "new_coords_horizontal_left": new_coords_horizontal_left,
    }


def start_chase(player):
    do_something = 2


def reset_chase(player):
    do_something = 1


def shoot_random_cell(match, now_playing, opponent):
    not_hit_cells_coordinates = []
    for index, row in enumerate(opponent.board):
        for index2, cell in enumerate(row):
            if not cell["shot"]:
                not_hit_cells_coordinates.append((index, index2))
    chosen_cell_coords = random.choice(not_hit_cells_coordinates)
    selected_cell = opponent.board[chosen_cell_coords[0]][chosen_cell_coords[1]]
    successfully_hit_a_target = selected_cell["occupied"]
    shoot(match, opponent, chosen_cell_coords)


def shoot_specific_cell(match, now_playing, opponent):
    chosen_direction = None
    list_chosen_direction = []
    for key, value in now_playing.possible_next_coords.items():
        if len(value) != 0:
            list_chosen_direction = value
            chosen_direction = key
            break
    chosen_cell_coords = list_chosen_direction[0]
    selected_cell = opponent.board[chosen_cell_coords[0]][chosen_cell_coords[1]]
    shoot(match, opponent, chosen_cell_coords)
    successfully_hit_a_target = selected_cell["occupied"]
    successfully_destroyed_a_target = selected_cell["destroyed"]
    now_playing.possible_next_coords[chosen_direction] = list(
        filter(
            lambda x: x != chosen_cell_coords,
            now_playing.possible_next_coords[chosen_direction],
        )
    )
    if successfully_hit_a_target:
        if successfully_destroyed_a_target:
            now_playing.chasing_a_ship = False
            now_playing.ship_being_chased_coords = None
            now_playing.possible_next_coords = None
    else:
        now_playing.possible_next_coords[chosen_direction] = []


# Checking if there are already hit ships that weren't destroyed. Return value is a tuple with a boolean indicating if there are ships and a list of the ships, that might be empty
def check_if_ship_found(opponent):
    ships_found = []
    for index, row in enumerate(opponent.board):
        for index2, cell in enumerate(row):
            if cell["shot"] and cell["occupied"] and not cell["destroyed"]:
                ships_found.append((index, index2))
    return (len(ships_found) != 0, ships_found)


def cpu_turn(match):
    now_playing = match.now_playing
    opponent = match.player_order[1]
    if not now_playing.chasing_a_ship:
        ship_found = check_if_ship_found(opponent)
        if ship_found[0]:
            now_playing.chasing_a_ship = True
            now_playing.ship_being_chased_coords = ship_found[1][0]
            now_playing.possible_next_coords = process_next_coords(
                now_playing.ship_being_chased_coords, opponent
            )
            shoot_specific_cell(match, now_playing, opponent)
        else:
            shoot_random_cell(match, now_playing, opponent)
    else:
        shoot_specific_cell(match, now_playing, opponent)
    # sleep(0.3)
    render_game_screen(match)


def check_if_match_end(match):
    opponent = match.player_order[1]
    opponent_destroyed_ships = list(
        map(lambda x: len(x) == 0, opponent.pieces.values())
    )
    match_is_over = all(opponent_destroyed_ships)
    if match_is_over:
        match.over = True
        match.winner = match.player_order[0]
        if match.winner.type_of_player == "human":
            match.current_sound = sounds["applause"]
        else:
            match.current_sound = sounds["boo"]


def game_turn(match):
    match.now_playing = match.player_order[0]
    (
        human_turn(match)
        if match.now_playing.type_of_player == "human"
        else cpu_turn(match)
    )
    check_if_match_end(match)
    if (
        match.rule == "regular"
    ):  # For now, this will be the rule. Others might be added in future updates;
        match.player_order.reverse()


def game_match(match):
    while not match.over:
        game_turn(match)
    render_game_screen(match)


def insert_name(match):
    match.current_screen = "enter_name_screen"
    render_game_screen(match)
    while True:
        key_pressed = readkey().upper()
        if key_pressed == key.BACKSPACE:
            match.player_name = match.player_name[:-1]
        if len(match.player_name) < 25:
            if any(key_pressed == char for char in letter_keys):
                match.player_name += key_pressed
            elif key_pressed == key.SPACE:
                match.player_name += " "
        render_game_screen(match)
        if key_pressed == key.ENTER:
            break


def initialize_match(match):
    match.player1 = HumanPlayer(match.player_name, "green", "player1")
    match.both_players = (match.player2, match.player1)
    match.player_order = [match.player1, match.player2]
    match.now_playing = match.player_order[0]
    match.current_screen = "game_screen"


def start_game(match):
    match.current_screen = "start_screen"
    render_game_screen(match)
    # You really have to press enter to start
    while True:
        if readkey() == key.ENTER:
            break
    insert_name(match)
    initialize_match(match)
    game_match(match)


class Player:
    def __init__(self, name, color, sec_color, status, type_of_player):
        self.name = name
        self.color = color
        self.sec_color = sec_color
        self.status = status
        self.type_of_player = type_of_player
        # This will be a dictionary with a list of tuples (very weird combination, but possible in python);
        self.pieces = {
            "carrier": [],
            "battleship": [],
            "cruiser": [],
            "submarine": [],
            "destroyer": [],
        }
        self.sound = None
        self.board = populate_board()
        randomly_place_pieces_on_board(self)


class HumanPlayer(Player):
    def __init__(self, name, color, status):
        super().__init__(name, color, "blue", status, "human")
        self.cursor = (0, 0)


class CpuPlayer(Player):
    def __init__(self, name, status):
        super().__init__(name, "red", "yellow", status, "cpu")
        self.chasing_a_ship = False
        self.ship_being_chased_coords = None
        self.possible_next_coords = None


class Match:
    def __init__(self, rule):
        self.current_screen = None
        self.player_name = "Menschlicher Spieler"
        self.player1 = None
        self.player2 = CpuPlayer("KI-Spieler", "player2")
        self.rule = rule
        self.current_screen = None
        self.current_sound = None
        self.current_display_message = ""
        self.both_players = None
        self.player_order = None
        self.now_playing = None
        self.winner = None
        self.over = False

        start_game(self)


class Game:
    def __init__(self):
        self.current_screen = None
        self.player_name = "PLAYER1"
        start_game(self)


new_match = Match("regular")

# Types of rules:
# Salvo: atiras um número de quadrados por turno igual ao número de navios que te restam.
# House rule “acertaste, jogas outra vez”: regra caseira comum — se acertas, jogas novamente até falhar. É só uma variação, não a regra oficial

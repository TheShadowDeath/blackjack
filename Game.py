from Player import Bot
from consts import MESSEGES

class Game:

    def __init__(self):
        self.players = []
        self.player = None
        self.dealler = None
        self.all_players_count = 1

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def start_game(self):
        message = MESSEGES.get('ask_start')
        if not self._ask_starting(message=message):
            exit(1)

        bots_count = int(input('Hello, write bots count\n'))
        self.all_players_count = bots_count + 1
        for _ in range(bots_count):
            b = Bot()
            self.players.append(b)
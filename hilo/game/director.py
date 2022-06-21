from game.card import Card


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 300
        self.guess = 0
        self.message = ""

        for _ in range(2):
            card = Card()
            self.cards.append(card)

        # for system that doesn't supprt ANSI
        import subprocess
        import sys
        while True:
            try:
                import ansicon
                ansicon.load()
                # print(u'\x1b[32mIf you see this color GREEN means ansicom is working.\x1b[m')
                break
            except ModuleNotFoundError:
                subprocess.check_call(
                    [sys.executable, '-m', 'pip', 'install', 'ansicon'])

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to deal.

        Args:
            self (Director): An instance of Director.
        """
        self.message = f"~Deal or No Deal~Deal cards? [y/n]   "
        self.dialog()
        deal_cards = input('\x1b[2F\x1b[20C')
        self.is_playing = (deal_cards == "y")
        print()

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            self.game_over()
            return

        for i in range(len(self.cards)):
            card = self.cards[i]
            card.deal()
            # print(f"this is value: {card.value}")

        # print(f"The current card is {self.cards[0].value}")
        # print(f"The next card is {self.cards[1].value}")

        self.message = f"~High or Low~Your current score is: {self.score}~~The current card is: {self.cards[0].value}~Is the next card higher or lower? [h/l]   "
        self.dialog()
        self.guess = input('\x1b[2F\x1b[42C').lower()
        print()

#         self.guess = input(f"The current card is: {self.cards[0].value}\n\
# Is the next card higher or lower? [h/l]").lower()

        if ((self.cards[0].value > self.cards[1].value) and self.guess == "l"
                or (self.cards[0].value < self.cards[1].value and self.guess == "h")):
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to deal again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        self.message = f"~Result~The next card is: {self.cards[1].value}~Your score is: {self.score} "
        self.dialog()
        print()

        # print(f"The next card is: {self.cards[0].value}")
        # print(f"Your score is: {self.score}\n")
        self.is_playing == (self.score > 0)

    def game_over(self):
        self.message = f"~Game Over!~Your final score is: {self.score}~~Exiting Cards..."
        self.dialog()

    def dialog(self):
        t = self.message

        def boxer(*t):
            if t[0].isnumeric():
                limit = int(t[0])  # override width
            else:
                line_width = max(len(x) for x in t)
                limit = line_width + 2
            # show box title
            print(
                f'┌\x1b[7;34;47m{t[1]}\x1b[0m{"─" * (limit - len(t[1]))}╖')
            # empty box
            for five in t[2:]:  # start from [n:] index
                print(f'│ {" " * (limit - 2)} ║')
            print('╘═'+'═' * (limit - 3)+'══╝', end='')
            # box content
            print(f'\x1b[{len(t[1:])}F')
            for five in t[2:]:  # start from [n:] index
                print(f'\x1b[2C{five}')
            print()
            # exit()
        # t = '40~Welcome~~~' #first index is box width
        tt = t.split('~')
        # print(f'tt: {tt}')
        boxer(*tt)

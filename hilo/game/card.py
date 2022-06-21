"""Game Module"""
import random


class Card:
    """A pice of cardboard with a different number on one side.

    The responsibility of Card is to keep track of the side facing up and calculate the points for
    it.

    Attributes:
        value (int): The number on the card facing up.
    """

    def __init__(self):
        """Constructs  a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def deal(self):
        self.value = random.randint(1, 13)

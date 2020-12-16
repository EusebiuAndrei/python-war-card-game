from random import shuffle


class Card:
    nr_of_cards = 52
    names = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    origins = ['C', 'S', 'H', 'D']  # Clubs, Spades, Hearts, Diamonds
    paths = [f"sprites/{name}{origin}.png" for name in names for origin in ['C', 'S', 'H', 'D']]
    powers_and_origins = [str(power) + origin for power in range(13) for origin in ['C', 'S', 'H', 'D']]

    def __init__(self, name, origin, power, image):
        self.name = name
        self.origin = origin
        self.power = power
        self.image = image

    def __str__(self):
        return f"{self.name}{self.origin}: {self.power} | {self.image}"

    def get_fullname(self):
        return f"{self.name}{self.origin}"

    @classmethod
    def get_shuffled_cards(cls, images):
        powers_and_origins = cls.powers_and_origins.copy()
        shuffle(powers_and_origins)
        cards = []

        for power_and_origin in powers_and_origins:
            power = int(power_and_origin[0:-1])
            name = cls.names[power]
            origin = power_and_origin[-1]

            cards.append(Card(name, origin, power, images[f"{name}{origin}"]))

        return cards

    @classmethod
    def print_cards(cls, cards):
        for card in cards:
            print(card)
        print()


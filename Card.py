from random import shuffle


class Card:
    nr_of_cards = 52
    names = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    origins = ['C', 'S', 'H', 'D']  # Clubs, Spades, Hearts, Diamonds
    full_names = [str(power) + origin for power in range(13) for origin in ['C', 'S', 'H', 'D']]

    def __init__(self, name, origin, power):
        self.name = name
        self.origin = origin
        self.power = power
        self.img_path = f"sprites/{name}{origin}.png"

    def __str__(self):
        return f"{self.name}{self.origin}: {self.power} | {self.img_path}"

    @classmethod
    def get_shuffled_cards(cls):
        full_names = cls.full_names.copy()
        shuffle(full_names)
        cards = []

        for full_name in full_names:
            power = int(full_name[0:-1])
            name = cls.names[power]
            origin = full_name[-1]

            cards.append(Card(name, origin, power))

        return cards

    @classmethod
    def print_cards(cls, cards):
        for card in cards:
            print(card)
        print()


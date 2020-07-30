class Roll:
    def __init__(self, name, defeated_by, defeat):
        self.name = name
        self.defeated_by = defeated_by
        self.defeat = defeat


class Player:
    def __init__(self, name):
        self.name = name
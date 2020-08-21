#!/usr/bin/env python3

class Ships:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def set_pos(self, row_start, row_end, column_start, column_end, orientation='h'):
        self.row_start = row_start
        self.row_end = row_end
        self.column_start = column_start
        self.column_end = column_end
        self.orient = 'h' if orientation == 'h' else 'v'

    def get_pos(self):
        return (self.name, self.row_start, self.row_end,
                self.column_start, self.column_end, self.orient)

    def __repr__(self):
        return f"{self.name} has size {self.size}"

class Player:
    def __init__(self, player_name="Player1"):
        self.player_name = player_name
        self.ship_coordinates = list()
        self.dict_ships = dict()

    def __repr__(self):
        return f"Player name: {self.player_name}"

#!/usr/bin/env python3

class Ships:
    def __init__(self, name, size, orientation='h'):
        self.name = name
        self.size = size
        self.orient = 'h'

    def set_pos(self, row, column, orientation='h'):
        self.row = row
        self.column = column
        if orientation == 'h':
            self.orient = 'h'
        else:
            self.orient = 'v'

    def get_pos(self):
        return (self.name, self.row, self.column, self.orient)

    def __repr__(self):
        return f"{self.name} has size {self.size}"

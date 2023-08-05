from .base import BaseMap
import random

class Map(BaseMap):

    def __init__(self, rows=10, cols=10):
        super().__init__(rows, cols)
        self._obstruct_idx = []
    
    def obstruct(self, X, Y=None, index=False):
        if index:
            self._obstruct_idx.append(X)
            X, Y = self.to_coordinate(X)
            self._grid[X][Y] = '[]'
        else:
            self._grid[X][Y] = '[]'
            self._obstruct_idx.append(self.to_index((X, Y)))
    
    def save(self):
        return self._grid

class Environment(Map):

    def __init__(self, grid):
        super().__init__()

        if hasattr(grid, '_grid'):
            self.__dict__.update(grid.__dict__)
        else:
            self._grid = grid
            self._rows = len(grid)
            self._cols = len(grid[0])
            self._start = 0
            self._end = self._rows * self._cols - 1
    
    def _valid_state(self, X, Y, action=None):
        if self._grid[X][Y] != 'o':
            if action is not None:
                raise ValueError(f'Action: {action}, State: ({X}, {Y}) is invalid!')
            else:
                raise ValueError(f'Current State: ({X}, {Y}) is invalid!')
    
    @property
    def valid_states(self, index=True):
        coordinate = []
        for row in range(self._rows):
            for col in range(self._cols):
                if self._grid[row][col] == 'o':
                    coordinate.append((row, col))
        
        if index:
            return [self.to_index(c) for c in coordinate]
        else:
            return coordinate
    
    def valid_actions(self, X, Y=None, index=False):
        if index:
            X, Y = self.to_coordinate(X)
        self._valid_state(X, Y)
        
        actions = {self._up: 'up', self._down: 'down', self._left: 'left', self._right: 'right'}
        coordinates = [action(X, Y) for action in actions.keys()]
        states = [self._grid[X][Y] for X, Y in coordinates]
        valid = [['up', 'down', 'left', 'right'][i] for i, s in enumerate(states) if s in ['o', 'x']]
        return valid

    def _up(self, X, Y=None, index=False):
        if index:
            X, Y = self.to_coordinate(X)
        self._valid_state(X, Y)
        if X == 0: X = self._rows - 1
        else: X -= 1
        return (X, Y)

    def _down(self, X, Y=None, index=False):
        if index:
            X, Y = self.to_coordinate(X)
        self._valid_state(X, Y)
        if X == self._rows - 1: X = 0
        else: X += 1
        return (X, Y)
    
    def _left(self, X, Y=None, index=False):
        if index:
            X, Y = self.to_coordinate(X)
        self._valid_state(X, Y)
        if Y == 0: Y = self._cols - 1
        else: Y -= 1
        return (X, Y)

    def _right(self, X, Y=None, index=False):
        if index:
            X, Y = self.to_coordinate(X)
        self._valid_state(X, Y)
        if Y == self._cols - 1: Y = 0
        else: Y += 1
        return (X, Y)

    def up(self, X, Y=None, index=False):
        X, Y = self._up(X, Y, index)
        self._valid_state(X, Y, 'up')

        if index:
            return self.to_index((X, Y))
        else:
            return (X, Y)

    def down(self, X, Y=None, index=False):
        X, Y = self._down(X, Y, index)
        self._valid_state(X, Y, 'down')

        if index:
            return self.to_index((X, Y))
        else:
            return (X, Y)
    
    def left(self, X, Y=None, index=False):
        X, Y = self._left(X, Y, index)
        self._valid_state(X, Y, 'left')

        if index:
            return self.to_index((X, Y))
        else:
            return (X, Y)

    def right(self, X, Y=None, index=False):
        X, Y = self._right(X, Y, index)
        self._valid_state(X, Y, 'right')

        if index:
            return self.to_index((X, Y))
        else:
            return (X, Y)

    def next(self, action, X, Y=None, index=False):
        if action == 'up':
            return self.up(X, Y, index)
        if action == 'down':
            return self.down(X, Y, index)
        if action == 'left':
            return self.left(X, Y, index)
        if action == 'right':
            return self.right(X, Y, index)
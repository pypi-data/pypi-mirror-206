# -*- coding: utf-8 -*-

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum

from .constant import FieldConstants as Consts

class Mino(IntEnum):
    _ = 0
    EMPTY = 0
    I = 1
    L = 2
    O = 3
    Z = 4
    T = 5
    J = 6
    S = 7
    X = 8
    G = 8
    GRAY = 8

    @staticmethod
    def parse_name(name):
    # parse_name() is added to support parsing of ' ' and lowercase names.
        if name == ' ':
            return Mino._
        try:
            return Mino[name.upper()]
        except:
            raise ValueError(f'Unknown mino name: {name}') from None

    def is_colored(self):
        return self is not Mino._ and self is not Mino.X

    def shifted(self, amount, strict=False):
        if strict:
            return Mino(self+amount)
        else:
            return Mino((self+amount) % len(Mino))

    def mirrored(self):
        return {
            Mino._: Mino._,
            Mino.I: Mino.I,
            Mino.L: Mino.J,
            Mino.O: Mino.O,
            Mino.Z: Mino.S,
            Mino.T: Mino.T,
            Mino.J: Mino.L,
            Mino.S: Mino.Z,
            Mino.X: Mino.X,
        }.get(self)

class Rotation(IntEnum):
    REVERSE = 0
    RIGHT = 1
    R = 1
    CW = 1
    SPAWN = 2
    LEFT = 3
    L = 3
    CCW = 3

    @staticmethod
    def parse_name(name):
    # parse_name() is added to support parsing of numeric and lowercase names.
        rotation = {
            '0': Rotation.SPAWN,
            '2': Rotation.REVERSE,
            '180': Rotation.REVERSE,
        }.get(name, None)
        if rotation is not None:
            return rotation
        try:
            return Rotation[name.upper()]
        except:
            raise KeyError(f'Unknown rotation: {rotation}')

    def short_name(self):
        return ['2', 'L', '0', 'R'][self]

    def shifted(self, amount, strict=False):
        if strict:
            return Rotation(self+amount)
        else:
            return Rotation((self+amount) % len(Rotation))

    def mirrored(self):
        return {
            Rotation.SPAWN: Rotation.SPAWN,
            Rotation.RIGHT: Rotation.LEFT,
            Rotation.REVERSE: Rotation.REVERSE,
            Rotation.LEFT: Rotation.RIGHT,
        }.get(self)

@dataclass
class Operation():
    SHAPES = {
        Mino._: {},
        Mino.I: {Rotation.REVERSE: [[0, 0], [1, 0], [-1, 0], [-2, 0]],
                 Rotation.RIGHT: [[0, 0], [0, 1], [0, -1], [0, -2]],
                 Rotation.SPAWN: [[0, 0], [-1, 0], [1, 0], [2, 0]],
                 Rotation.LEFT: [[0, 0], [0, -1], [0, 1], [0, 2]]},
        Mino.L: {Rotation.REVERSE: [[0, 0], [1, 0], [-1, 0], [-1, -1]],
                 Rotation.RIGHT: [[0, 0], [0, 1], [0, -1], [1, -1]],
                 Rotation.SPAWN: [[0, 0], [-1, 0], [1, 0], [1, 1]],
                 Rotation.LEFT: [[0, 0], [0, -1], [0, 1], [-1, 1]]},
        Mino.O: {Rotation.REVERSE: [[0, 0], [-1, 0], [0, -1], [-1, -1]],
                 Rotation.RIGHT: [[0, 0], [0, -1], [1, 0], [1, -1]],
                 Rotation.SPAWN: [[0, 0], [1, 0], [0, 1], [1, 1]],
                 Rotation.LEFT: [[0, 0], [0, 1], [-1, 0], [-1, 1]]},
        Mino.Z: {Rotation.REVERSE: [[0, 0], [-1, 0], [0, -1], [1, -1]],
                 Rotation.RIGHT: [[0, 0], [0, -1], [1, 0], [1, 1]],
                 Rotation.SPAWN: [[0, 0], [1, 0], [0, 1], [-1, 1]],
                 Rotation.LEFT: [[0, 0], [0, 1], [-1, 0], [-1, -1]]},
        Mino.T: {Rotation.REVERSE: [[0, 0], [1, 0], [-1, 0], [0, -1]],
                 Rotation.RIGHT: [[0, 0], [0, 1], [0, -1], [1, 0]],
                 Rotation.SPAWN: [[0, 0], [-1, 0], [1, 0], [0, 1]],
                 Rotation.LEFT: [[0, 0], [0, -1], [0, 1], [-1, 0]]},
        Mino.J: {Rotation.REVERSE: [[0, 0], [1, 0], [-1, 0], [1, -1]],
                 Rotation.RIGHT: [[0, 0], [0, 1], [0, -1], [1, 1]],
                 Rotation.SPAWN: [[0, 0], [-1, 0], [1, 0], [-1, 1]],
                 Rotation.LEFT: [[0, 0], [0, -1], [0, 1], [-1, -1]]},
        Mino.S: {Rotation.REVERSE: [[0, 0], [1, 0], [0, -1], [-1, -1]],
                 Rotation.RIGHT: [[0, 0], [0, 1], [1, 0], [1, -1]],
                 Rotation.SPAWN: [[0, 0], [-1, 0], [0, 1], [1, 1]],
                 Rotation.LEFT: [[0, 0], [0, -1], [-1, 0], [-1, 1]]},
        Mino.X: {},
    }

    mino: Mino
    rotation: Rotation
    x: int
    y: int

    @classmethod
    def shape_at(cls, mino, rotation, x=0, y=0):
        return [[x+dx, y+dy] for dx, dy
                in cls.SHAPES.get(mino, {}).get(rotation, (0, 0))]

    @classmethod
    def is_inside_at(cls, mino, rotation, x, y):
        return all(0 <= x < Consts.WIDTH
                   and 0 <= y < Consts.HEIGHT
                   for x, y in cls.shape_at(mino, rotation, x, y))

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

    def shifted(self, dx, dy):
        return Operation(self.mino, self.rotation, self.x+dx, self.y+dy)

    def mirror(self):
        mirrored = self.mirrored()
        self.mino = mirrored.mino
        self.rotation = mirrored.rotation
        self.x = mirrored.x
        self.y = mirrored.y

    def mirrored(self):
        mino = self.mino.mirrored()
        if mino is Mino.I or self.Mino is Mino.O:
            rotation = self.rotation
            if (rotation is Rotation.REVERSE
                    or (rotation is Rotation.LEFT and mino is Mino.O)):
                x = Consts.WIDTH - self.x
            elif rotation is Rotation.SPAWN or mino is Mino.O:
                x = Consts.WIDTH - self.x - 2
            else:
                x = Consts.WIDTH - self.x - 1
        else:
            rotation = self.rotation.mirrored()
            x = Consts.WIDTH - self.x -1
        return Operation(mino, rotation, x, self.y)

    def shape(self):
        return self.shape_at(self.mino, self.rotation, self.x, self.y)

    def is_inside(self):
        return self.is_inside_at(self.mino, self.rotation, self.x, self.y)


# Copyright (c) 2015 Gamda Software, LLC
#
# See the file LICENSE.txt for copying permission.

from abc import ABCMeta, abstractmethod
from enum import Enum
from chess.chess import Color
from gameboard.gameboard import Gameboard, Coordinate

class Type(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

class Abstract_Piece(metaclass = ABCMeta):
    """Chess Piece

    Abstract class for chess pieces. Defines two properties: color and
    type and two methods: valid_moves() and squares_attacked().

    """

    def __init__(self, color, type):
        """Return a new piece of the specified color and type.

        Args:
            color (chess.Color): piece's color
            type (Type): piece's type

        """
        if not isinstance(color, Color):
            raise ValueError("Use chess.Color values")
        super().__init__()
        self._color = color
        self._type = Type.PAWN

    @property
    def color(self):
        """chess.Color: Color of the piece."""
        return self._color

    @property
    def type(self):
        """Type: Type of the piece."""
        return self._type

    @abstractmethod
    def valid_moves(self, board, position):
        """Return a list of coordinates where Piece can move.

        Args:
            board (gameboard.gameboard.Gameboard): board representing gamestate
            position (gameboard.gameboard.Coordinate): piece's current position

        Returns:
            List of gameboard.gameboard.Coordinate elements. The piece can
            move to any of these coordinates in the current gamestate.

        """
        raise NotImplementedError

    @abstractmethod
    def squares_attacked(self, board, position):
        """Return a list of coordinates that Piece is currently attacking.

        Args:
            board (gameboard.gameboard.Gameboard): board representing gamestate
            position (gameboard.gameboard.Coordinate): piece's current position

        Returns:
            List of gameboard.gameboard.Coordinate elements. The piece is 
            attacking all of these coordinates in the current gamestate.

        """
        raise NotImplementedError


class Pawn(Abstract_Piece):

    def __init__(self, color):
        super().__init__(color, Type.PAWN)

    def valid_moves(self, board, position):
        raise NotImplementedError

    def squares_attacked(self, board, position):
        raise NotImplementedError
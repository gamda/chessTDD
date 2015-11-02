# Copyright (c) 2015 Gamda Software, LLC
#
# See the file LICENSE.txt for copying permission.

from abc import ABCMeta, abstractmethod
from enum import Enum
from gameboard.gameboard import Gameboard, Coordinate, Direction

class Type(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

class Color(Enum):
        WHITE = True
        BLACK = False

class Abstract_Piece(metaclass = ABCMeta):
    """Chess Piece

    Abstract class for chess pieces. Defines two properties: color and
    type and two methods: valid_moves() and squares_attacked().

    """

    @property
    def color(self):
        """Color: Color of the piece."""
        return self._color

    @property
    def type(self):
        """Type: Type of the piece."""
        return self._type

    def __init__(self, color, piece_type):
        """Return a new piece of the specified color and type.

        Args:
            color (chess.Color): piece's color
            type (Type): piece's type

        """
        if not isinstance(color, Color):
            raise ValueError("Use piece.Color values")
        super().__init__()
        self._color = color
        self._type = piece_type

    @abstractmethod
    def valid_moves(self, board, position):
        """Return a list of coordinates where Piece can move.

        Args:
            board (gameboard.gameboard.Gameboard): board representing gamestate
            position (gameboard.gameboard.Coordinate): piece's current position

        Returns:
            Set of gameboard.gameboard.Coordinate elements. The piece can
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
            Set of gameboard.gameboard.Coordinate elements. The piece is 
            attacking all of these coordinates in the current gamestate.

        """
        raise NotImplementedError

    def __str__(self):
        t = _type_to_string(self._type)
        t = t.upper() if self._color == Color.WHITE else t
        return t


class Pawn(Abstract_Piece):

    def __init__(self, color):
        super().__init__(color, Type.PAWN)
        self.has_moved = False

    def valid_moves(self, board, position):
        moves = set()
        # straight ahead
        forward_direction = Direction.top \
                            if self.color == Color.WHITE \
                            else Direction.btm
        first = board.neighbor_in_direction(position, forward_direction)
        if board.is_empty(first):
            moves.add(first)
            second = board.neighbor_in_direction(first, forward_direction)
            if board.is_empty(second) and not self.has_moved:
                moves.add(second)
        # captures
        diagonal_directions = [Direction.top_right, Direction.top_left] \
                              if self.color == Color.WHITE else \
                              [Direction.btm_right, Direction.btm_left]
        for direction in diagonal_directions:
            neighbor = board.neighbor_in_direction(position, direction)
            if neighbor is not None and not board.is_empty(neighbor):
                moves.add(neighbor)
        return moves

    def squares_attacked(self, board, position):
        raise NotImplementedError


class Knight(Abstract_Piece):

    def __init__(self, color):
        super().__init__(color, Type.KNIGHT)

    def valid_moves(self, board, position):
        raise NotImplementedError

    def squares_attacked(self, board, position):
        raise NotImplementedError


class Bishop(Abstract_Piece):

    def __init__(self, color):
        super().__init__(color, Type.BISHOP)

    def valid_moves(self, board, position):
        raise NotImplementedError

    def squares_attacked(self, board, position):
        raise NotImplementedError


class Rook(Abstract_Piece):

    def __init__(self, color):
        super().__init__(color, Type.ROOK)

    def valid_moves(self, board, position):
        raise NotImplementedError

    def squares_attacked(self, board, position):
        raise NotImplementedError


class Queen(Abstract_Piece):

    def __init__(self, color):
        super().__init__(color, Type.QUEEN)

    def valid_moves(self, board, position):
        raise NotImplementedError

    def squares_attacked(self, board, position):
        raise NotImplementedError


class King(Abstract_Piece):

    def __init__(self, color):
        super().__init__(color, Type.KING)
        self.has_moved = False

    def valid_moves(self, board, position):
        raise NotImplementedError

    def squares_attacked(self, board, position):
        raise NotImplementedError

def _type_to_string(t):
    if t == Type.PAWN:
        return 'p'
    elif t == Type.KNIGHT:
        return 'n'
    elif t == Type.BISHOP:
        return 'b'
    elif t == Type.ROOK:
        return 'r'
    elif t == Type.QUEEN:
        return 'q'
    elif t == Type.KING:
        return 'k'
    return ""

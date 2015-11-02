# Copyright (c) 2015 Gamda Software, LLC
#
# See the file LICENSE.txt for copying permission.

from enum import Enum
from gameboard.gameboard import Gameboard, Coordinate
from chess.piece import Color, Type, Pawn, Knight, Bishop, Rook, Queen, King

class Chess:
    """Chess game logic"""

    @property
    def board(self):
        return self._board

    @property
    def pieces(self):
        return self._pieces

    @property
    def moves(self):
        """List of tuples of the form (origin, destination), both Coordinate"""
        return self._board.moves

    @property
    def last_move(self):
        return self._board.moves[-1]

    def __init__(self):
        self.reset()

    def valid_moves_for_piece_at_coordinate(self, coordinate):
        """Return a set of coordinates where Piece can move.

        Args:
            coordinate (gameboard.Coordinate): position to check for moves
        Returns:
            Set of gameboard.gameboard.Coordinate elements. The piece can
            move to any of these coordinates in the current gamestate.
        Raises:
            TypeError: if coordinate is not Coordinate
            
        """
        if not isinstance(coordinate, Coordinate):
            raise TypeError("coordinate variable must be from Coordinate enum")
        piece = self._pieces.get(coordinate)
        return piece.valid_moves(self.board, coordinate) \
               if piece is not None else \
               set()

    def move(self, origin, destination):
        """Perform the requested move and returns a Move_Type

        Args:
            origin (Coordinate): the square where the piece is currently
            destination (Coordinate): the square where the piece will end
        Returns:
            Move_Type: Normal, Castle, or En_passant
        Raises:
            TypeError: if origin or destination is not Coordinate
            
        """
        piece = self._pieces[origin]
        self._board.move(origin, destination)
        self._pieces[destination] = self._pieces[origin]
        del self._pieces[origin]
        if piece.type is Type.PAWN or piece.type is Type.KING:
            piece.has_moved = True

    def reset(self):
        """Restore pieces for a new game."""

        self._board = Gameboard()
        self._pieces = {}
        # Pawns
        for i in range(1, 63, 8):
            wp = Pawn(Color.WHITE)
            self._pieces[Coordinate(i)] = wp
            bp = Pawn(Color.BLACK)
            self._pieces[Coordinate(i+5)] = bp
        # Other pieces
        self._pieces[Coordinate.a1] = Rook(Color.WHITE)
        self._pieces[Coordinate.h1] = Rook(Color.WHITE)
        self._pieces[Coordinate.a8] = Rook(Color.BLACK)
        self._pieces[Coordinate.h8] = Rook(Color.BLACK)
        self._pieces[Coordinate.b1] = Knight(Color.WHITE)
        self._pieces[Coordinate.g1] = Knight(Color.WHITE)
        self._pieces[Coordinate.b8] = Knight(Color.BLACK)
        self._pieces[Coordinate.g8] = Knight(Color.BLACK)
        self._pieces[Coordinate.c1] = Bishop(Color.WHITE)
        self._pieces[Coordinate.f1] = Bishop(Color.WHITE)
        self._pieces[Coordinate.c8] = Bishop(Color.BLACK)
        self._pieces[Coordinate.f8] = Bishop(Color.BLACK)
        self._pieces[Coordinate.d1] = Queen(Color.WHITE)
        self._pieces[Coordinate.d8] = Queen(Color.BLACK)
        self._pieces[Coordinate.e1] = King(Color.WHITE)
        self._pieces[Coordinate.e8] = King(Color.BLACK)

        for c, p in self._pieces.items():
            self._board.set_content(c,p)

    def __str__(self):
        string = ""
        for r in self._board.rows:
            for s in r:
                piece = self._pieces[s] if not self._board.is_empty(s) else "."
                string = string + str(piece) + '\t'
            string = string + '\n'
        return string
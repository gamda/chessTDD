# Copyright (c) 2015 Gamda Software, LLC
#
# See the file LICENSE.txt for copying permission.

import unittest
from gameboard.gameboard import Coordinate
from chess.piece import Type as Piece_Type, Color
from chess.piece import Pawn, Knight, Bishop, Rook, Queen, King
from chess.chess import Chess


class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def _print(self):
        print(self.chess)

    def test_piece_color_and_type(self):
        self.assertRaises(ValueError, Pawn, "string")
        p = Pawn(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.PAWN)
        self.assertEqual(p.color, Color.WHITE)
        self.assertEqual(p.has_moved, False)
        self.assertEqual(str(p), "P")
        p = Pawn(Color.BLACK)
        self.assertEqual(p.color, Color.BLACK)
        self.assertEqual(str(p), "p")
        self.assertEqual(p.has_moved, False)
        p = Knight(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.KNIGHT)
        self.assertEqual(str(p), "N")
        p = Bishop(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.BISHOP)
        self.assertEqual(str(p), "B")
        p = Rook(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.ROOK)
        self.assertEqual(str(p), "R")
        p = Queen(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.QUEEN)
        self.assertEqual(str(p), "Q")
        p = King(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.KING)
        self.assertEqual(str(p), "K")
        self.assertEqual(p.has_moved, False)

    def test_pawn_valid_moves_no_capture(self):
        # white move - two squares
        pos = Coordinate.e2
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        answer = set([Coordinate.e3, Coordinate.e4])
        self.assertEqual(moves, answer)
        # black move - two squares
        self.chess.move(Coordinate.e2, Coordinate.e4)
        self.assertEqual(self.chess.pieces[Coordinate.e4].has_moved, True)
        pos = Coordinate.e7
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        answer = set([Coordinate.e6, Coordinate.e5])
        self.assertEqual(moves, answer)
        # blocked white pawn
        self.chess.move(Coordinate.e7, Coordinate.e5)
        self.assertEqual(self.chess.pieces[Coordinate.e5].has_moved, True)
        pos = Coordinate.e4
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        answer = set()
        self.assertEqual(moves, answer)
        # blocked black pawn
        pos = Coordinate.e5
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        self.assertEqual(moves, answer)
        # white move - pawn that moved previously
        self.chess.move(Coordinate.a2, Coordinate.a3)
        pos = Coordinate.a3
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        answer = set([Coordinate.a4])
        self.assertEqual(moves, answer)
        # black move - pawn that moved previously
        self.chess.move(Coordinate.b7, Coordinate.b5)
        pos = Coordinate.b5
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        answer = set([Coordinate.b4])
        self.assertEqual(moves, answer)
        # white move - second square not empty
        self.chess.move(Coordinate.a3, Coordinate.a4)
        self.chess.move(Coordinate.b5, Coordinate.b4)
        pos = Coordinate.b2
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        answer = set([Coordinate.b3])
        self.assertEqual(moves, answer)
        # black move - second square not empty
        self.chess.move(Coordinate.a4, Coordinate.a5)
        pos = Coordinate.a7
        moves = self.chess.pieces[pos].valid_moves(self.chess.board, pos)
        answer = set([Coordinate.a6])
        self.assertEqual(moves, answer)

        self._print()


























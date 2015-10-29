# Copyright (c) 2015 Gamda Software, LLC
#
# See the file LICENSE.txt for copying permission.

import unittest
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
        self.assertEqual(str(p), "P")
        p = Pawn(Color.BLACK)
        self.assertEqual(p.color, Color.BLACK)
        self.assertEqual(str(p), "p")
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
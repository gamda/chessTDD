# Copyright (c) 2015 Gamda Software, LLC
#
# See the file LICENSE.txt for copying permission.

import unittest
from chess.piece import Type as Piece_Type
from chess.piece import Pawn, Knight, Bishop, Rook, Queen, King
from chess.chess import Chess, Color

class TestPieces(unittest.TestCase):

    def test_piece_raises_type_error_wrong_color(self):
        self.assertRaises(ValueError, Pawn, "string")

    def test_piece_color_and_type(self):
        p = Pawn(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.PAWN)
        self.assertEqual(p.color, Color.WHITE)
        p = Pawn(Color.BLACK)
        self.assertEqual(p.color, Color.BLACK)
        p = Knight(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.KNIGHT)
        p = Bishop(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.BISHOP)
        p = Rook(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.ROOK)
        p = Queen(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.QUEEN)
        p = King(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.KING)


class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()
# Copyright (c) 2015 Gamda Software, LLC
#
# See the file LICENSE.txt for copying permission.

import unittest
from chess.piece import Type as Piece_Type
from chess.piece import Pawn
from chess.chess import Chess, Color

class TestPieces(unittest.TestCase):

    def test_piece_raises_type_error_wrong_color(self):
        self.assertRaises(ValueError, Pawn, "string")

    def test_pawn(self):
        p = Pawn(Color.WHITE)
        self.assertEqual(p.type, Piece_Type.PAWN)
        self.assertEqual(p.color, Color.WHITE)
        p = Pawn(Color.BLACK)
        self.assertEqual(p.color, Color.BLACK)

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()
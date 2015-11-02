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
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.e3, Coordinate.e4])
        self.assertEqual(moves, answer)
        # black move - two squares
        self.chess.move(Coordinate.e2, Coordinate.e4)
        self.assertEqual(self.chess.pieces[Coordinate.e4].has_moved, True)
        pos = Coordinate.e7
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.e6, Coordinate.e5])
        self.assertEqual(moves, answer)
        # blocked white pawn
        self.chess.move(Coordinate.e7, Coordinate.e5)
        self.assertEqual(self.chess.pieces[Coordinate.e5].has_moved, True)
        pos = Coordinate.e4
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set()
        self.assertEqual(moves, answer)
        # blocked black pawn
        pos = Coordinate.e5
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        self.assertEqual(moves, answer)
        # white move - pawn that moved previously
        self.chess.move(Coordinate.a2, Coordinate.a3)
        pos = Coordinate.a3
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.a4])
        self.assertEqual(moves, answer)
        # black move - pawn that moved previously
        self.chess.move(Coordinate.b7, Coordinate.b5)
        pos = Coordinate.b5
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.b4])
        self.assertEqual(moves, answer)
        # white move - second square not empty
        self.chess.move(Coordinate.a3, Coordinate.a4)
        self.chess.move(Coordinate.b5, Coordinate.b4)
        pos = Coordinate.b2
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.b3])
        self.assertEqual(moves, answer)
        # black move - second square not empty
        self.chess.move(Coordinate.a4, Coordinate.a5)
        pos = Coordinate.a7
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.a6])
        self.assertEqual(moves, answer)

    def test_pawn_valid_moves_capture(self):
        # white one capture available
        self.chess.move(Coordinate.e2, Coordinate.e4)
        self.chess.move(Coordinate.f7, Coordinate.f5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.e5, Coordinate.f5])
        self.assertEqual(moves, answer)
        # black one capture available
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.f5)
        answer = set([Coordinate.e4, Coordinate.f4])
        self.assertEqual(moves, answer)
        # black two captures available
        self.chess.move(Coordinate.g2, Coordinate.g4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.f5)
        answer = set([Coordinate.e4, Coordinate.f4, Coordinate.g4])
        self.assertEqual(moves, answer)
        # white two captures available
        self.chess.move(Coordinate.d7, Coordinate.d5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.d5, Coordinate.e5, Coordinate.f5])
        self.assertEqual(moves, answer)

    def test_en_passant_white(self):
        # white right
        self.chess.move(Coordinate.e2, Coordinate.e4)
        self.chess.move(Coordinate.a7, Coordinate.a6)
        self.chess.move(Coordinate.e4, Coordinate.e5)
        self.chess.move(Coordinate.f7, Coordinate.f5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e5)
        answer = set([Coordinate.e6, Coordinate.f6])
        self.assertEqual(moves, answer)
        # white left
        self.chess.move(Coordinate.a2, Coordinate.a3)
        self.chess.move(Coordinate.d7, Coordinate.d5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e5)
        answer = set([Coordinate.d6, Coordinate.e6])

    def test_en_passant_black(self):
        # black right
        self.chess.move(Coordinate.a2, Coordinate.a3)
        self.chess.move(Coordinate.e7, Coordinate.e5)
        self.chess.move(Coordinate.a3, Coordinate.a4)
        self.chess.move(Coordinate.e5, Coordinate.e4)
        self.chess.move(Coordinate.f2, Coordinate.f4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.e3, Coordinate.f3])
        self.assertEqual(moves, answer)
        # black left
        self.chess.move(Coordinate.a7, Coordinate.a6)
        self.chess.move(Coordinate.d2, Coordinate.d4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.d3, Coordinate.e3])

        self._print()























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

    def _move(self, origin, destination):
        self.chess.move(origin, destination)

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
        self._move(Coordinate.e2, Coordinate.e4)
        self.assertEqual(self.chess.pieces[Coordinate.e4].has_moved, True)
        pos = Coordinate.e7
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.e6, Coordinate.e5])
        self.assertEqual(moves, answer)
        # blocked white pawn
        self._move(Coordinate.e7, Coordinate.e5)
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
        self._move(Coordinate.a2, Coordinate.a3)
        pos = Coordinate.a3
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.a4])
        self.assertEqual(moves, answer)
        # black move - pawn that moved previously
        self._move(Coordinate.b7, Coordinate.b5)
        pos = Coordinate.b5
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.b4])
        self.assertEqual(moves, answer)
        # white move - second square not empty
        self._move(Coordinate.a3, Coordinate.a4)
        self._move(Coordinate.b5, Coordinate.b4)
        pos = Coordinate.b2
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.b3])
        self.assertEqual(moves, answer)
        # black move - second square not empty
        self._move(Coordinate.a4, Coordinate.a5)
        pos = Coordinate.a7
        moves = self.chess.valid_moves_for_piece_at_coordinate(pos)
        answer = set([Coordinate.a6])
        self.assertEqual(moves, answer)

    def test_pawn_valid_moves_capture(self):
        # white one capture available
        self._move(Coordinate.e2, Coordinate.e4)
        self._move(Coordinate.f7, Coordinate.f5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.e5, Coordinate.f5])
        self.assertEqual(moves, answer)
        # black one capture available
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.f5)
        answer = set([Coordinate.e4, Coordinate.f4])
        self.assertEqual(moves, answer)
        # black two captures available
        self._move(Coordinate.g2, Coordinate.g4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.f5)
        answer = set([Coordinate.e4, Coordinate.f4, Coordinate.g4])
        self.assertEqual(moves, answer)
        # white two captures available
        self._move(Coordinate.d7, Coordinate.d5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.d5, Coordinate.e5, Coordinate.f5])
        self.assertEqual(moves, answer)

    def test_en_passant_white(self):
        # white right
        self._move(Coordinate.e2, Coordinate.e4)
        self._move(Coordinate.a7, Coordinate.a6)
        self._move(Coordinate.e4, Coordinate.e5)
        self._move(Coordinate.f7, Coordinate.f5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e5)
        answer = set([Coordinate.e6, Coordinate.f6])
        self.assertEqual(moves, answer)
        # en passant gone after move is made
        self._move(Coordinate.a2, Coordinate.a3)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e5)
        answer = set([Coordinate.e6])
        self.assertEqual(moves, answer)
        # white left
        self._move(Coordinate.a3, Coordinate.a4)
        self._move(Coordinate.d7, Coordinate.d5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e5)
        answer = set([Coordinate.d6, Coordinate.e6])
        self.assertEqual(moves, answer)
        # en passant gone after move is made
        self._move(Coordinate.a4, Coordinate.a5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e5)
        answer = set([Coordinate.e6])
        self.assertEqual(moves, answer)

    def test_en_passant_black(self):
        # black right
        self._move(Coordinate.a2, Coordinate.a3)
        self._move(Coordinate.e7, Coordinate.e5)
        self._move(Coordinate.a3, Coordinate.a4)
        self._move(Coordinate.e5, Coordinate.e4)
        self._move(Coordinate.f2, Coordinate.f4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.e3, Coordinate.f3])
        self.assertEqual(moves, answer)
        # en passant gone after move is made
        self._move(Coordinate.a4, Coordinate.a5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.e3])
        self.assertEqual(moves, answer)
        # black left
        self._move(Coordinate.a7, Coordinate.a6)
        self._move(Coordinate.d2, Coordinate.d4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.d3, Coordinate.e3])
        self.assertEqual(moves, answer)
        # en passant gone after move is made
        self._move(Coordinate.b2, Coordinate.b3)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.e4)
        answer = set([Coordinate.e3])
        self.assertEqual(moves, answer)

    def test_pawn_squares_attacked(self):
        # center
        pos = Coordinate.e2
        attacked = self.chess.squares_attacked_by_piece_at_coordinate(pos)
        answer = set([Coordinate.d3, Coordinate.f3])
        self.assertEqual(attacked, answer)
        # edge
        pos = Coordinate.a2
        attacked = self.chess.squares_attacked_by_piece_at_coordinate(pos)
        answer = set([Coordinate.b3])
        self.assertEqual(attacked, answer)

    def test_knight_valid_moves(self):
        # white edge
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.b1)
        answer = set([Coordinate.a3, Coordinate.c3])
        self.assertEqual(moves, answer)
        # black edge
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.b8)
        answer = set([Coordinate.a6, Coordinate.c6])
        self.assertEqual(moves, answer)
        # white center
        self._move(Coordinate.b1, Coordinate.c3)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.c3)
        answer = set([Coordinate.b5, Coordinate.d5, # top
                      Coordinate.b1, # btm
                      Coordinate.a4, # left
                      Coordinate.e4]) # right
        self.assertEqual(moves, answer)
        # black center
        self._move(Coordinate.b8, Coordinate.c6)   
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.c6)
        answer = set([Coordinate.b8, # top
                      Coordinate.b4, Coordinate.d4, # btm
                      Coordinate.a5, # left
                      Coordinate.e5]) # right
        self.assertEqual(moves, answer)
        # white attacking pieces
        self._move(Coordinate.c3, Coordinate.d5)
        attacked = self.chess.squares_attacked_by_piece_at_coordinate(Coordinate.d5)
        answer = set([Coordinate.c7, Coordinate.e7, # top
                      Coordinate.f4, Coordinate.f6, # right
                      Coordinate.c3, Coordinate.e3, # btm
                      Coordinate.b4, Coordinate.b6]) # left
        self.assertEqual(attacked, answer)

    def test_knight_squares_attacked(self):
        # white edge
        pos = Coordinate.b1
        attacked = self.chess.squares_attacked_by_piece_at_coordinate(pos)
        answer = set([Coordinate.a3, Coordinate.c3, Coordinate.d2])
        self.assertEqual(attacked, answer)
        # white center
        self._move(Coordinate.b1, Coordinate.c3)
        pos = Coordinate.c3
        attacked = self.chess.squares_attacked_by_piece_at_coordinate(pos)
        answer = set([Coordinate.b5, Coordinate.d5, # top
                      Coordinate.e2, Coordinate.e4, # right
                      Coordinate.b1, Coordinate.d1, # btm
                      Coordinate.a2, Coordinate.a4]) # left
        self.assertEqual(attacked, answer)

    def test_bishop_valid_moves_white(self):
        # no moves
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.c1)
        answer = set()
        self.assertEqual(moves, answer)
        # one lane
        self._move(Coordinate.e2, Coordinate.e4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.f1)
        answer = set([Coordinate.e2, 
                      Coordinate.d3, 
                      Coordinate.c4, 
                      Coordinate.b5, 
                      Coordinate.a6])
        self.assertEqual(moves, answer)
        # one lane with capture
        self._move(Coordinate.a7, Coordinate.a6)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.f1)
        self.assertEqual(moves, answer)
        # four lanes with capture
        self._move(Coordinate.f1, Coordinate.b5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.b5)
        answer = set([Coordinate.c6, 
                      Coordinate.d7,
                      Coordinate.c4,
                      Coordinate.d3,
                      Coordinate.e2,
                      Coordinate.f1,
                      Coordinate.a4,
                      Coordinate.a6])
        self.assertEqual(moves, answer)

    def test_bishop_valid_moves_black(self):
        # no moves
        self._move(Coordinate.e2, Coordinate.e4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.c8)
        answer = set()
        self.assertEqual(moves, answer)
        # one lane
        self._move(Coordinate.e7, Coordinate.e5)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.f8)
        answer = set([Coordinate.e7, 
                      Coordinate.d6, 
                      Coordinate.c5, 
                      Coordinate.b4, 
                      Coordinate.a3])
        self.assertEqual(moves, answer)
        # four lanes
        self._move(Coordinate.f8, Coordinate.b4)
        moves = self.chess.valid_moves_for_piece_at_coordinate(Coordinate.b4)
        answer = set([Coordinate.c5,
                      Coordinate.d6,
                      Coordinate.e7,
                      Coordinate.f8,
                      Coordinate.c3,
                      Coordinate.d2,
                      Coordinate.a3,
                      Coordinate.a5])
        self.assertEqual(moves, answer)

        self._print()























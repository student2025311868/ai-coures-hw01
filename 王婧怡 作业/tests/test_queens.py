# tests/test_queens.py
import unittest
from src.eight_queens import solve_n_queens

class TestEightQueens(unittest.TestCase):
    """八皇后问题单元测试"""

    def test_n4_queens(self):
        """测试N=4，正确解数=2"""
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2)

    def test_n8_queens(self):
        """测试N=8，正确解数=92"""
        solutions = solve_n_queens(8)
        self.assertEqual(len(solutions), 92)

if __name__ == "__main__":
    unittest.main()
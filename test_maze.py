import unittest
from maze import Maze

class Test_maze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells_one(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0,0,num_rows,num_cols,0,0)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_break_entrance_and_exit_created(self):
        m1 = Maze(0,0,12,10,10,10)
        m1._break_entrance_and_exit()
        top_left_cell = m1._cells[0][0]
        bottom_right_cell = m1._cells[-1][-1]
        self.assertTrue(top_left_cell.walls.left_wall ^ top_left_cell.walls.top_wall)
        self.assertTrue(bottom_right_cell.walls.right_wall ^ bottom_right_cell.walls.bottom_wall)

if __name__ == "__main__":
    unittest.main()
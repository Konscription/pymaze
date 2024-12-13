import random
import time
from cell import Cell, Walls
from graphics import Point


class Maze:
    def __init__(
        self,
        x1, y1,
        num_rows, num_cols,
        cell_size_x,
        cell_size_y,
        win = None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = self._create_cells()
    
    def check_sizes(self) -> bool:
        window_height = self._win._height
        window_width = self._win._width
        width_pad_total = self._x1 * 2
        height_pad_total = self._y1 * 2
        usable_width = window_width - width_pad_total
        usable_height = window_height - height_pad_total
        valid_width = False
        valid_height = False
        #print(f"usable width: {usable_width}")
        #max_width_size = usable_width / self.num_cols
        #print(f"max size: {max_width_size}")
        if usable_width / self.num_cols >= self.cell_size_x:
            valid_width = True
        if usable_height / self.num_rows >= self.cell_size_y:
            valid_height = True
        return (valid_width and valid_height)
        
    def _create_cells(self):
        if self._win is not None:
            if not self.check_sizes():
                print("problem with size of grid.")
        cells = []
        top_left_x = self._x1
        top_left_y = self._y1
        for x in range(self.num_cols):
            columns = []
            for y in range(self.num_rows):
                sqp1 = Point(top_left_x, top_left_y)
                bottom_right_x = top_left_x + self.cell_size_x
                bottom_right_y = top_left_y + self.cell_size_y
                sqp2 = Point(bottom_right_x, bottom_right_y)
                columns.append(Cell(sqp1,sqp2,Walls(),win=self._win))
                top_left_y += self.cell_size_y
            top_left_x += self.cell_size_x
            top_left_y = self._y1
            cells.append(columns)
        #print("starting draw")
        if self._win is not None:
            for columns in cells:
                for cell in columns:
                    self._draw_cell(cell)
        return cells
        
    def _draw_cell(self, cell:Cell):
        if self._win is None:
            return
        cell.draw()
        #print(f"X: {cell._sqp1.x} Y: {cell._sqp1.y}")
        self._animate()
        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self, seed=None):
        """
        The entrance to the maze will always be at the top of the top-left cell, 
        the exit always at the bottom of the bottom-right cell.
        """
        top_left_cell = self._cells[0][0]

        bottom_right_cell = self._cells[-1][-1]

        rng1 = random.randint(1,100)
        rng2 = random.randint(1,100)
        
        if rng1 % 2 == 0:
            top_left_cell.walls.left_wall = False
        else:
            top_left_cell.walls.top_wall = False
        
        if rng2 % 2 == 0:
            bottom_right_cell.walls.right_wall = False
        else:
            bottom_right_cell.walls.bottom_wall = False

        #print(f"TL cell: {top_left_cell}")
        #print(f"BR cell: {bottom_right_cell}")
        self._draw_cell(top_left_cell)
        self._draw_cell(bottom_right_cell)
        
        
        
        
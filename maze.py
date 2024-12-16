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
        win = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = self._create_cells()
        self.seed = seed
    
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
                columns.append(Cell(sqp1, sqp2, Walls(), win=self._win, grid_loc=Point(x,y)))
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
        
    def _draw_cell(self, cell:Cell) -> None:
        if self._win is None:
            return
        cell.draw()
        #print(f"X: {cell._sqp1.x} Y: {cell._sqp1.y}")
        self._animate()
        
    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self, seed=None) -> None:
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
        
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        while True:
            cells_to_visit = []
            
            if i - 1 >= 0 and i - 1 < self.num_cols:
                left_adjacent_cell = self._cells[i-1][j]
                if not left_adjacent_cell.visited:
                    cells_to_visit.append(left_adjacent_cell)
            
            if i + 1 < self.num_cols:
                right_adjacent_cell = self._cells[i+1][j]
                if not right_adjacent_cell.visited:
                    cells_to_visit.append(right_adjacent_cell)
            
            if j - 1 >= 0 and j - 1 < self.num_rows:
                top_adjacent_cell = self._cells[i][j-1]
                if not top_adjacent_cell.visited:
                    cells_to_visit.append(top_adjacent_cell)
                    
            if j + 1 < self.num_rows:
                bottom_adjacent_cell = self._cells[i][j+1]
                if not bottom_adjacent_cell.visited:
                    cells_to_visit.append(bottom_adjacent_cell)

            if cells_to_visit == []:
                current_cell.draw()
                return
                
            next_cell = random.choice(cells_to_visit)
            
            i_diff = next_cell.grid_loc.x - current_cell.grid_loc.x
            j_diff = next_cell.grid_loc.y - current_cell.grid_loc.y
            
            if i_diff > 0: #right
                current_cell.walls.right_wall = False
                next_cell.walls.left_wall = False
            if i_diff < 0: #left
                current_cell.walls.left_wall = False
                next_cell.walls.right_wall = False
            if j_diff > 0: #bottom
                current_cell.walls.bottom_wall = False
                next_cell.walls.top_wall = False
            if j_diff < 0: #top
                current_cell.walls.top_wall = False
                next_cell.walls.bottom_wall = False
            
            current_cell.draw()
            next_cell.draw()
            
            self._break_walls_r(next_cell.grid_loc.x, next_cell.grid_loc.y)
            
    def _reset_cells_visited(self):
        for columns in self._cells:
            for cell in columns:
                cell.visited = False
    
    def _solve_r(self, i:int, j:int) -> bool:
        self._animate()
        
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        if current_cell.grid_loc == Point(self.num_cols - 1, self.num_rows -1 ):
            return True
        
        directions = [
            (-1, 0, 'left_wall'),
            (1, 0, 'right_wall'),
            (0, -1, 'top_wall'),
            (0, 1, 'bottom_wall')]
        
        for dir_i, dir_j, wall in directions:
            ni, nj = i + dir_i, j + dir_j
            
            if 0 <=ni < self.num_cols and 0 <= nj < self.num_rows:
                adjacent_cell = self._cells[ni][nj]
                if not getattr(current_cell.walls, wall) and not adjacent_cell.visited:
                    current_cell.draw_move(adjacent_cell)
                    
                    if self._solve_r(ni, nj):
                        return True
                    
                    current_cell.draw_move(adjacent_cell, True)
        return False

    def solve(self) -> bool:
        return self._solve_r(0, 0)
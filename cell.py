from graphics import Line, Point

class Walls:
    def __init__(self, has_left_wall:bool=True, has_right_wall:bool=True,
                 has_top_wall:bool=True, has_bottom_wall:bool=True):
        self.left_wall = has_left_wall
        self.right_wall = has_right_wall
        self.top_wall = has_top_wall
        self.bottom_wall = has_bottom_wall
    
class Cell:
    def __init__(self, sqp1:Point, sqp2:Point, walls:Walls=Walls(), win=None, grid_loc:Point=None):
        self.walls = walls
        self._sqp1 = sqp1
        self._sqp2 = sqp2
        self._win = win
        self.visited = False
        self.grid_loc = grid_loc
        
    def __repr__(self):
        return f"({self._sqp1.x},{self._sqp1.y})({self._sqp2.x},{self._sqp2.y}) walls: {self.walls.left_wall}, {self.walls.right_wall}, {self.walls.top_wall}, {self.walls.bottom_wall}"
    
    def draw(self):
        if self._win is None:
            return
        left_line = Line(self._sqp1,Point(self._sqp1.x,self._sqp2.y))
        right_line = Line(Point(self._sqp2.x,self._sqp1.y),self._sqp2)
        top_line = Line(self._sqp1,Point(self._sqp2.x,self._sqp1.y))
        bottom_line = Line(Point(self._sqp1.x,self._sqp2.y),self._sqp2)
        
        if self.walls.left_wall:
            self._win.draw_line(left_line)
        else:
            self._win.draw_line(left_line, "white")
        if self.walls.right_wall:
            self._win.draw_line(right_line)
        else:
            self._win.draw_line(right_line, "white")
        if self.walls.top_wall:
            self._win.draw_line(top_line)
        else:
            self._win.draw_line(top_line, "white")
        if self.walls.bottom_wall: 
            self._win.draw_line(bottom_line)
        else:
            self._win.draw_line(bottom_line,"white")

    def draw_move(self,to_cell, undo=False):
        if self._win is None:
            return  
        half_length = abs(self._sqp2.x - self._sqp1.x) // 2
        midpoint = Point(
            self._sqp1.x + half_length, 
            self._sqp1.y + half_length
        )
        to_half_length = abs(to_cell._sqp2.x - to_cell._sqp1.x) // 2
        to_midpoint = Point(
            to_cell._sqp1.x + to_half_length, 
            to_cell._sqp1.y + to_half_length
        )
        fill_color = "red"
        if undo:
            fill_color = "grey"
        line = Line(midpoint,to_midpoint)
        self._win.draw_line(line, fill_color)
        

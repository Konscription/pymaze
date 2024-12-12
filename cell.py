from graphics import Line, Point

class Walls:
    def __init__(self, has_left_wall:bool=True, has_right_wall:bool=True,
                 has_top_wall:bool=True, has_bottom_wall:bool=True):
        self.left_wall = has_left_wall
        self.right_wall = has_right_wall
        self.top_wall = has_top_wall
        self.bottom_wall = has_bottom_wall
    
class Cell:
    def __init__(self, win, sqp1:Point, sqp2:Point, walls:Walls=Walls()):
        self.walls = walls
        self._sqp1 = sqp1
        self._sqp2 = sqp2
        self._win = win
        
    def draw(self):
        if self._win is None:
            return     
        if self.walls.left_wall:
            line = Line(self._sqp1,Point(self._sqp1.x,self._sqp2.y))
            self._win.draw_line(line)
        if self.walls.right_wall:
            line = Line(Point(self._sqp2.x,self._sqp1.y),self._sqp2)
            self._win.draw_line(line)
        if self.walls.top_wall:
            line = Line(self._sqp1,Point(self._sqp2.x,self._sqp1.y))
            self._win.draw_line(line)
        if self.walls.bottom_wall:
            line = Line(Point(self._sqp1.x,self._sqp2.y),self._sqp2)
            self._win.draw_line(line)

    def draw_move(self,to_cell, undo=False):
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
        

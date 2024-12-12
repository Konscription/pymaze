from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, point_1:Point, point_2:Point):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas:Canvas, fill_color:str) -> None:
        """ function to draw a line to a given canvas with a specified color
        
        Args:
            canvas (Canvas): canvas to draw a line onto.
            fill_color (str): string like "black" or "red".
        """        
        canvas.create_line(
            self.point_1.x, self.point_1.y, 
            self.point_2.x, self.point_2.y, 
            fill=fill_color, 
            width=2
            )
        
class Walls:
    def __init__(self, has_left_wall:bool=True, has_right_wall:bool=True,
                 has_top_wall:bool=True, has_bottom_wall:bool=True):
        self.left_wall = has_left_wall
        self.right_wall = has_right_wall
        self.top_wall = has_top_wall
        self.bottom_wall = has_bottom_wall
    
class Cell:
    def __init__(
        self, walls:Walls,
        _x1:int,_y1:int,
        _x2:int,_y2:int,
    ):
        self.walls = walls
        self.x1 = _x1
        self.x2 = _x2
        self.y1 = _y1
        self.y2 = _y2
        
    def draw(self, canvas:Canvas, line_color:str):
        line_width = 2
        if self.walls.left_wall:
            canvas.create_line(
                self.x1,self.y1,
                self.x1,self.y2, 
                fill=line_color,
                width=line_width
                )
        if self.walls.right_wall:
            canvas.create_line(
                self.x2, self.y1,
                self.x2, self.y2,
                fill=line_color,
                width=line_width
            )
        if self.walls.top_wall:
            canvas.create_line(
                self.x1, self.y1,
                self.x2, self.y1,
                fill=line_color,
                width=line_width
            )
        if self.walls.bottom_wall:
            canvas.create_line(
                self.x1, self.y2,
                self.x2, self.y2,
                fill=line_color,
                width=line_width
            )

class Window:
    def __init__(self, width:int, height:int):
        """initalize a window for the maze solver application with a given
        width and height

        Args:
            width (int): width of window in pixels
            height (int): height of window in pixels
        """
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
        
    def close(self) -> None:
        self.__running = False
    
    def draw_line(self, line:Line, fill_color:str) -> None:
        line.draw(self.__canvas, fill_color)
        
    def draw_cell(self, cell:Cell):
        cell.draw(self.__canvas, "black")




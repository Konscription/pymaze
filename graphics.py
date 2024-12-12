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




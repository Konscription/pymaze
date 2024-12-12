from graphics import Window , Point, Line
from cell import Cell, Walls
def main():
    win = Window(800,800)
    cells = [
        Cell(
            win,
            Point(1,1),
            Point(50,50),
            walls=Walls(False,False,False,False)
        ),
        Cell(
            win,
            Point(50,1),
            Point(100,50),
            walls=Walls(False,False,False,True)
        ),
        Cell(
            win,         
            Point(100,1),
            Point(150,50),
            walls=Walls(False,False,True,False)
        ),
        Cell(
            win,
            Point(150,1),
            Point(200,50),
            walls=Walls(False,False,True,True)
        ),
        Cell(
            win,
            Point(200,1),
            Point(250,50),
            walls=Walls(False,True,False,False)
        )
    ]
    for cell in cells:
        cell.draw()
    cells[0].draw_move(cells[1])
    cells[3].draw_move(cells[4],True)
    win.wait_for_close()
    
main()


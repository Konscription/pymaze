from graphics import Window , Point, Line, Cell, Walls

def main():
    win = Window(800,800)
    cells = [
        Cell(
            Walls(False,False,False,False),
            1,1,
            50,50
        ),
        Cell(
            Walls(False,False,False,True),
            50,1,
            100,50
        ),
        Cell(
            Walls(False,False,True,False),
            100,1,
            150,50
        ),
        Cell(
            Walls(False,False,True,True),
            150,1,
            200,50
        ),
        Cell(
            Walls(False,True,False,False),
            200,1,
            250,50
        )
    ]
    for cell in cells:
        win.draw_cell(cell)
    win.wait_for_close()
    
main()


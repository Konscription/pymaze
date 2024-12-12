from graphics import Window , Point, Line

def main():
    win = Window(800,800)
    line1 = Line(Point(0,0), Point(50,50))
    line2 = Line(Point(50,50), Point(50,100))
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()
    
main()


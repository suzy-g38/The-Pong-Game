from turtle import Turtle
ALIGNMENT = "center"
FONT = ("FFF Forward", 50, "normal")
POSITIONS = [(0, 310), (0, 280), (0, 250), (0, 220), (0, 190), (0, 160), (0, 130), (0, 100), (0, 70), (0, 40),
                     (0, 10), (0, -20), (0, -50), (0, -80), (0, -110), (0, -140), (0, -170), (0, -200), (0, -230),
                     (0, -260)]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(self.right_score, font=FONT, align=ALIGNMENT)

    def update_left_scoreboard(self):
        self.left_score += 1
        self.update_scoreboard()

    def update_right_scoreboard(self):
        self.right_score += 1
        self.update_scoreboard()



    def middle_line(self):
        for position in POSITIONS:
            dot = Turtle("square")
            dot.color("white")
            dot.turtlesize(stretch_len=0.20, stretch_wid=0.60)
            dot.penup()
            dot.goto(position)




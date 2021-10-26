import turtle as t

class Score(t.Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color(227/255, 226/255, 225/255)
        self.goto(0,270)
        self.increase_score()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='Center', font = ("Arial", 15, "normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='Center', font = ("Arial", 30, "normal"))
        
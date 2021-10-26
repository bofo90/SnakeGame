import turtle as t
import random

class Food(t.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color(230/255, 73/255, 46/255)
        self.relocate()
        
    def relocate(self):   
        self.goto(random.randint(-40, 40)*10,random.randint(-40, 40)*10)
        
    def face_snake(self,snake):
        self.setheading(snake)
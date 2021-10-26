import turtle as t
MOVE_DIS = 10

class Snake():
    
    def __init__(self):
        
        self.segments = []
        for i in range(3):
            self.add_segment((i*-10,0))
            # seg = t.Turtle('square')
            # seg.color(227/255, 226/255, 225/255)
            # seg.penup()
            # seg.goto(i*-20,0)
            # self.segments.append(seg)
            
        self.head = self.segments[0]
        
    def add_segment(self, position):
        seg = t.Turtle('square')
        seg.color(227/255, 226/255, 225/255)
        seg.penup()
        seg.shapesize(0.5,0.5)
        seg.goto(position)
        self.segments.append(seg)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
        self.head.forward(MOVE_DIS)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


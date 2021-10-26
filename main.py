import turtle as t
import food
import score
import snake
import time

# def close_window():
#     try:
#         t.bye()
#     except t.Terminator:
#         pass
    
# close_window()

screen = t.Screen()
screen.setup(800, 800)
screen.bgcolor((33/255, 32/255, 31/255))
screen.tracer(0)
screen.title('Snake Game')

my_snake = snake.Snake()
my_food = food.Food()
my_score = score.Score()

screen.listen()
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
screen.onkey(my_snake.right, 'Right')
screen.onkey(my_snake.left, 'Left')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    my_food.face_snake(my_food.towards(my_snake.head.position()))
    
    if my_snake.head.distance(my_food) < 5:
        my_food.relocate()
        my_score.increase_score()
        my_snake.extend()

    if my_snake.head.xcor() > 390 or my_snake.head.xcor() < -390 or my_snake.head.ycor() > 390 or my_snake.head.ycor() < -390:
        game_on = False
        my_score.game_over()
        
    for seg in my_snake.segments[1:]:
        if my_snake.head.distance(seg) < 10:
            game_on = False
            my_score.game_over()
            

screen.exitonclick()
# close_window()

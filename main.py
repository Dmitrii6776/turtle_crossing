import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
scoreboard = Scoreboard()
player.starting_position()
screen.setup(width=600, height=600)
screen.tracer(0)


game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(player.move, 'w')
    time.sleep(0.01)
    screen.update()
    car.generate_car()
    car.car_move()
    for cars in car.car_list:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            if screen.textinput(title='Restart', prompt='Restart the game? Type "y" or "n"') == 'y':
                game_is_on = True
                player.starting_position()
                scoreboard.new_game()

    if player.ycor() > FINISH_LINE_Y:
        player.starting_position()
        scoreboard.update_score()
        car.increase_speed()


screen.exitonclick()
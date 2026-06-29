## URL - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

## SOLUTION ##

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
    if wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
    else:
        move()
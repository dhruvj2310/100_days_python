## URL = https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

## SOLUTION ##
## turn_left(), move(), at_goal(), front_is_clear() and wall_in_front() are already defined

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cross_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        cross_hurdle()
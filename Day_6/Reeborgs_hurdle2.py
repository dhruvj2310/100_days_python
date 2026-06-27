#URL = https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

## SOLUTION ##
## move(), turn_left() and at_goal() already defined inbiult


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cross_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    cross_hurdle()
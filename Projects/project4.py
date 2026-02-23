# goal is to click on space for cookies untill 2000 cookies
import turtle, time, random, math
from utils import *
# Section 1 - setup
# TODO - set a background using set_background()
set_background("castle")
 
# TODO - create at least two variables and set their starting value. ex: cookies = 0
cookies = 0
ovens = 0
cost = 10
message_sprite = create_sprite("alien",-300,150)
message_sprite.color("white")
 
# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_cookie(): 
    global cookies
    cookies += 1
    x = random.randint(-300,300)
    y = random.randint(-200,200)
    create_sprite("cookie",x,y)
 
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
 
window.onkeypress(make_cookie,"space")
# Press Space to make a cookie
 
# TODO - make a second control
def buy_oven():
    global ovens, cookies, cost
    if cookies >= cost:
        cookies = cookies - cost
        cost  = cost * 2
        ovens += 1
        x = random.randint(-300,300)
        y = random.randint(-200,200)
        create_sprite("oven",x,y)
 
 
window.onkeypress(buy_oven,"o")
# Buy a oven with O
 
 
# Section 3 - game loop
window.listen()
for i in range(100000):
    message_sprite.clear()
    cookies += ovens / 20
    message_sprite.write(f"Cookies: {round(cookies)}\nOven Price: {cost}\nOvens: {ovens}",font=("Arial",30,"normal"))
    message_sprite.hideturtle()
    # TODO - put any repeating actions here
 
    time.sleep(0.1)
    window.update()


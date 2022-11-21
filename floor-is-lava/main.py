game_over = False
stage.set_background("brickwall")
stage.disable_floor()
platforms = []

game_over = False
stage.set_background("brickwall")
stage.disable_ceiling()
platforms = []
chick = codesters.Sprite("chick2")
chick.set_size(.6)
score = 0
landed = False
OG_platform = codesters.Rectangle(0, -190, 100, 20, "blue")
platforms.append(OG_platform)
left_pressed = False
right_pressed = False


lives_number = 3
lives_text = codesters.Text("Lives:"+str(lives_number),-200,200,"yellow")

def lives_code(sprite,hit_sprite):
    global lives_number,lives_text
    if hit_sprite.get_image_name() == "chick2":
        hit_sprite.set_y(0)
        lives_number -= 1
        lives_text.hide()
        lives_text = codesters.Text("Lives:"+str(lives_number),-200,200,"yellow")
    if lives_number < 1:
        lives_text.hide()
        lives_text = codesters.Text("Died",-200,200,"yellow")
        gg = codesters.Text("Game Over",0,0,"yellow")
        gg.set_size(3)
        
        

# sprite = codesters.Rectangle(x, y, width, height, "color")
lava = codesters.Rectangle(0, -225, 500, 50, "red")

lava.event_collision(lives_code)

falling_speed_x = -4
falling_speed_y = -1

plat_y = 225

def follow(sprite,hit_sprite):
    if hit_sprite.get_image_name() == "chick2" and hit_sprite.get_y() > sprite.get_y() + 10:
        chick.set_x_speed(sprite.get_x_speed())
        chick.set_y_speed(sprite.get_y_speed())
        
        
def restart(sprite):
    if sprite.get_y() < -200:
        sprite.set_y(615)

for i in range(4):
    platform = codesters.Rectangle(0, plat_y, 100, 20, "blue")
    platform.set_gravity_off()
    platform.set_x_speed(falling_speed_x)
    platform.set_y_speed(falling_speed_y)
    platform.event_collision(follow)
    platforms.append(platform)
    plat_y += 200
    falling_speed_x = falling_speed_x *-1
    # stage.wait(4.5)



def left_key(sprite):
    global left_pressed, OG_platform, chick, landed
    left_pressed = True
    
    if chick.get_x() < -50:
        chick.set_y_speed(-4)
        landed = False
        
    if chick.get_x() < -200:
        chick.set_x(-200)

    if right_pressed == False:
        sprite.move_left(20)
        
    left_pressed = False
chick.event_key("left", left_key)



def right_key(sprite):
    global right_pressed,chick, OG_platform, landed
    
    right_pressed = True
    
    if left_pressed == False:
        sprite.move_right(20)
        
    if chick.get_x() > 50:
        chick.set_y_speed(-4)
        landed = False
        
    right_pressed = False
chick.event_key("right", right_key)


def jump():
    global landed
    if landed:
        for i in range(4):
            chick.move_up(30)
            chick.set_x_speed(0)
            landed = False
        landed = False
        print(landed)
        
chick.event_key("up", jump)

def collision(sprite, hit_sprite):
    global landed, falling_speed_x,falling_speed_y
    my_var = hit_sprite.get_color() 
    # checking if my chick hits platform
    if my_var == "blue":
        # this checks if chick y pos isnt higher than the platform it hits then fall
        if hit_sprite.get_y() > sprite.get_y():
            sprite.set_y_speed(-4)
            sprite.set_x_speed(0)
        else:
            sprite.set_y_speed(0)        
            landed = True
        
    if my_var == "red":
        sprite.say("Ouch")
    
chick.event_collision(collision)

while True:
    stage.wait(.2)
    if not landed:
        chick.set_y_speed(-3)
    for i in platforms:
        restart(i)

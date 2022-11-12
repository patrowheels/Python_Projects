import random


# this deck is going to have all my image names inside of it (string data types)
deck = []
# this list is going to have the physical red square objects in it (object data types)
card_list = []
card_locations = []
x = -160
y = 180

turns = 0




def card_animation(sprite,color):
    sprite.set_width(10)
    stage.wait(.1)
    sprite.set_color(color)
    sprite.set_width(100)

def flip_up(sprite):
        # sprite.say(sprite.id)
        global turns
        turns += 1
        # set up turn one 
        if turns == 1:
            global image1
            global sprite1
            sprite1 = sprite
            # these two lines below remeber the x and y location of the card we click on 
            x = sprite.get_x()
            y = sprite.get_y()

            image1 = codesters.Sprite(deck[sprite.id],x,y)
            image1.set_size(.5)
            card_animation(sprite,"black")
        if turns == 2:
                sprite2 = sprite
                x = sprite.get_x()
                y = sprite.get_y()
                image2 = codesters.Sprite(deck[sprite.id],x,y)
                image2.set_size(.5)
                card_animation(sprite,"black")
                stage.wait(1)
                if image1.get_image_name() != image2.get_image_name():
                    image1.hide()
                    image2.hide()
                    card_animation(sprite1,"red")
                    card_animation(sprite2,"red")
                turns = 0



for p in range(4):
    for i in range(4):

        card = codesters.Rectangle(x,y,100,110,"red")
        card.event_click(flip_up)
        card.id = i+(p*4)
        card_y = card.get_y()
        card_x = card.get_x()
        card_list.append(card_x)
        card_list.append(card_y)
        card_list.append(card)

        x += 110
    x = -160
    y -= 120

def create_deck():
    for i in range(2):
        deck.append("skeleton")
        deck.append("jackolantern")
        deck.append("pumpkin")
        deck.append("candycorn")
        deck.append("broom")
        deck.append("zombie1")
        deck.append("zombie2")
        deck.append("alien1")
create_deck() 

random.shuffle(deck)

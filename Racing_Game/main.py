import pygame
import random
from car import Car
pygame.init()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (211, 211, 211)
PURPLE = (48, 25, 52)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

speed = 1

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Racing Car")
#
all_sprites_list = pygame.sprite.Group()

all_coming_cars = pygame.sprite.Group()

playerCar = Car(RED, 20, 30, 70)
playerCar.rect.x = 200
playerCar.rect.y = 300

car1 = Car(BLACK, 20, 30, random.randint(50, 100))
car1.rect.x = 280
car1.rect.y = 400

car2 = Car(PURPLE, 20, 30, random.randint(50, 100))
car2.rect.x = 370
car2.rect.y = 0

car3 = Car(PURPLE, 20, 30, random.randint(50, 100))
car3.rect.x = 200
car3.rect.y = 500

car4 = Car(PURPLE, 20, 30, random.randint(50, 100))
car4.rect.x = 450
car4.rect.y = 00

# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

# rect(surface, color, rect) -> Rect
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


def create_road(screen, color, dict, border_width):
    # The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, color, dict, border_width)

    # -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we can exit the while loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False
        # --- Game logic should go here

        # Game Logic
    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > 500:
            car.changeSpeed(random.randint(50, 100))
            car.repaint(random.choice(colorList))
            car.rect.y = 00

    # Check if there is a car collision
    car_collision_list = pygame.sprite.spritecollide(
        playerCar, all_coming_cars, False)
    for car in car_collision_list:
        print("Car crash!")
        # End Of Game
        carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    if keys[pygame.K_UP]:
        playerCar.moveBackward(1)
    if keys[pygame.K_DOWN]:
        playerCar.moveForward(1)

    all_sprites_list.update()

    # --- Drawing code should go here
    # First, clear the screen to white.
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, [115, 0, 460, 500], 0)

    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    create_road(screen, GREY, [180, 0, 75, 500], 0)
    create_road(screen, GREY, [260, 0, 75, 500], 0)
    create_road(screen, GREY, [340, 0, 75, 500], 0)
    create_road(screen, GREY, [420, 0, 75, 500], 0)

    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

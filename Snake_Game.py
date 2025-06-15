import turtle #Draws shapes and patterns using turtle graphics module.
import time   #Returns current time or measures time intervals.
import random #Generates random numbers or selections.
import pygame #Creates games and multimedia applications in Python.
import sys
# Initialize pygame mixer for sound
pygame.mixer.init()
try:
    kaboom_sound = pygame.mixer.Sound("kaboom.wav")
except pygame.error:
    kaboom_sound = None

try:
    chomp_sound = pygame.mixer.Sound("CHOMP.wav")
except pygame.error:
    chomp_sound = None
    
try:
    SPARKLE_sound = pygame.mixer.Sound("SPARKLE.wav")
except pygame.error:
    SPARKLE_sound = None

try:
    BOING_sound = pygame.mixer.Sound("BOING.wav")
except pygame.error:
    BOING_sound = None
    
# Game state
score = 0
high_score = 0
delay = 0.1
special_timer = 0
special_duration = 0
special_food_active = False
bomb_timer = 0
bomb_duration = 0
bomb_active = False
speed_threshold = 2  # Speed up every 2 segments

# Screen setup
wn = turtle.Screen()
wn.title("Snake Chaos")
wn.bgcolor("#99d9ea")
wn.setup(width=600, height=600)
wn.tracer(0)

# Register shapes
wn.register_shape("FRUIT.gif")
wn.register_shape("STAR.gif")
wn.register_shape("LA_BOMBA.gif")
wn.register_shape("KABOOM.gif")

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("#C04000")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("FRUIT.gif")
food.penup()
food.goto(0, 100)

# Special food
special_food = turtle.Turtle()
special_food.shape("STAR.gif")
special_food.penup()
special_food.goto(2000, 2000)
special_food.hideturtle()

# Bomb
bomb = turtle.Turtle()
bomb.shape("LA_BOMBA.gif")
bomb.penup()
bomb.goto(2000, 2000)
bomb.hideturtle()

# Kaboom
kaboom = turtle.Turtle()
kaboom.shape("KABOOM.gif")
kaboom.penup()
kaboom.hideturtle()

# Score display
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("red")
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Snake body
segments = []

# Controls
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)# 20 pixels up
    elif head.direction == "down":
        head.sety(head.ycor() - 20)# 20 pixels down
    elif head.direction == "left":
        head.setx(head.xcor() - 20)# 20 pixels to the left
    elif head.direction == "right":
        head.setx(head.xcor() + 20) # 20 pixels to the right

def update_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

def reset_game(message="GAME OVER!"):
    global score, delay, special_food_active, bomb_active, speed_threshold
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(2000, 2000)
    segments.clear()

    pen.clear()
    pen.goto(0, 0)
    pen.write(message, align="center", font=("Courier", 30, "bold"))
    wn.update()
    time.sleep(2)
    pen.clear()
    pen.goto(0, 260)

    score = 0
    delay = 0.1
    speed_threshold = 2

    special_food.hideturtle()
    special_food_active = False
    bomb.hideturtle()
    bomb_active = False
    update_score()

def spawn_special_food():
    global special_timer, special_duration, special_food_active
    if special_timer == 0 and not special_food_active:
        x, y = random.randint(-14, 14)*20, random.randint(-14, 14)*20
        special_food.goto(x, y)
        special_food.showturtle()
        special_food_active = True
        special_timer = random.randint(100, 200)  # Faster spawn!
        special_duration = 70
    else:
        special_timer = max(0, special_timer - 1)

    if special_duration > 0 and special_food_active:
        special_duration -= 1
        if special_duration == 0:
            special_food.hideturtle()
            special_food_active = False

def spawn_bomb():
    global bomb_timer, bomb_duration, bomb_active
    if bomb_timer == 0 and not bomb_active:
        x, y = random.randint(-14, 14)*20, random.randint(-14, 14)*20
        bomb.goto(x, y)
        bomb.showturtle()
        bomb_active = True
        bomb_timer = random.randint(150, 300)  # Faster spawn!
        bomb_duration = 150
    else:
        bomb_timer = max(0, bomb_timer - 1)

    if bomb_duration > 0 and bomb_active:
        bomb_duration -= 1
        if bomb_duration == 0:
            bomb.hideturtle()
            bomb_active = False

            
# Add this global flag near the top of your code, with other global variables:
running = True

# Quit function to stop the loop and close window
def quit_game():
    global running
    running = False  # Stop the main game loop
    wn.bye()         # Close the turtle window

# Bind the 'q' key to quit
wn.onkey(quit_game, "q")


# Keyboard
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")






# Main Game loop
while running:
    wn.update()

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290: #To determine whether the snake hits the wall
        if BOING_sound:
            BOING_sound.play()
        reset_game("GAME OVER!")

    # Food
    if head.distance(food) < 20:  #To determine whether the snake head is "eats" the fruit
        if chomp_sound:
            chomp_sound.play()

        food.goto(random.randint(-13, 13)*20, random.randint(-13, 13)*20) # *20 is for making the grid. Easier to get the fruits
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("#FF7F50" if len(segments) % 2 == 0 else "#FAD5A5")
        new_segment.penup()
        segments.append(new_segment)
        score += 1
        if score > high_score:
            high_score = score
        update_score()

        if len(segments) >= speed_threshold: #Increasing the speed of the Snake Head (This is for the "Fruit")
            delay = max(0.03, delay - 0.005)
            speed_threshold += 6

    # Special food
    if special_food_active and head.distance(special_food) < 20: #To determine whether the snake head is "eating" the special fruit
        if SPARKLE_sound:
            SPARKLE_sound.play()
        special_food.hideturtle()
        special_food_active = False
        for _ in range(2):
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color("#FF7F50" if len(segments) % 2 == 0 else "#FAD5A5")
            new_segment.penup()
            segments.append(new_segment)
        score += 2
        if score > high_score:
            high_score = score
        update_score()

        if len(segments) >= speed_threshold: #Increasing the speed of the Snake Head (This is for the "Special_Fruit")
            delay = max(0.03, delay - 0.01)
            speed_threshold += 6

    # Bomb collision
    if bomb_active and head.distance(bomb) < 20: #To determine whether the snake head is "eating" with the Bomb...KABOOM!
        if kaboom_sound:
            kaboom_sound.play()
        bomb.hideturtle()
        head.hideturtle()
        for segment in segments:
            segment.hideturtle()
        kaboom.goto(head.xcor(), head.ycor())
        kaboom.showturtle()
        wn.update()
        time.sleep(1.5)
        kaboom.hideturtle()
        reset_game("💥 KA-BOOM! GAME OVER 💥")
        head.showturtle()

    # Move segments
    for i in range(len(segments) - 1, 0, -1): #Logic for the end segment followiung the snake head.
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()  #Using the move function

    # Self collision
    for segment in segments:
        if segment.distance(head) < 20: #Checking if the Snake head is eating its own segment 
            if BOING_sound:
                BOING_sound.play()
            reset_game("GAME OVER!")
            break

    # Spawns
    spawn_special_food() #Spawning the star at a random time
    spawn_bomb() #Spawning the bomb at a random time

    time.sleep(delay)  #delaying the end of game to add sound and effects

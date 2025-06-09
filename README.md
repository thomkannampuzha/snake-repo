

Goal of the project
Create a fun version of the classic "Snake" game with a unique "Thom twist." The game will keep the core features like the snake growing when it eats food, ending the game if it runs into itself or a hazard, and using sound effects to make it more engaging. As the snake grows, the speed will increase to make the game more exciting and challenging.

About the “Snake Chaos” game
In Snake Chaos, your aim is to help the snake eat as much food as possible to grow longer and earn points, all while avoiding crashes into walls, itself, or surprise bombs. The game ends if the snake hits any of these obstacles. Special food (like stars) gives extra points and bonus growth, but bombs are dangerous traps that can end the game with a cool explosion animation.
You control the snake with the keyboard as it moves nonstop, and the more it grows, the faster it gets—making it harder to stay in control. Sound effects bring the game to life, and the score system keeps track of both your current score and your highest score. The challenge is simple: stay alive and get the highest score.

Steps followed to build the game:
1. Initial setup 
* Import the required python modules
    * turtle - draws shapes and graphics using turtle graphics module; I am using turtle function for graphics of the characters (snake, strawberry, star and bomb) 
    * time - return current time or measures time intervals; I am using the time function for adding delays for sound effects and ending the game
    * random - generates random numbers or selections; I am using random function for placement of the characters and for deciding the time it appears in the game 
    * pygame - creates games and multimedia function in Python and it is a cross platform (MacBook, Windows, Linux); I am using the pygame function to add sound effects to eating the fruit and star, hitting the bomb, hitting the wall and snake hitting itself
* Set up the background
    * Title is “Snake chaos”
    * Size is 600x600
    * Background colour is #99d9ea
    * wn as variable for the turtle screen
* Register the custom shapes/writing/variable using turtle function
    * Snake head for the head of the snake
    * Food for strawberry
    * Special food for star
    * bomb for bomb
    * Kaboom as graphic effect upon hitting the bomb
    * Score display
    * New segment as custom variable to add segments to the snake on eating fruit or star
* Hide the turtle cursor with a square

1. Creation of game objects
* Snakehead - a list of turtle segments (initially one segment with a square as snake head)
* Food - a turtle object (initially a red circle, replaced by a “strawberry” GIF)
* Special Food - a turtle object (triangle initially, replaced by a “star” GIF)
* Bomb - a turtle object (initially a black circle, replace by “la bomba” GIF)
* Kaboom - a turtle object added for graphic effect on snake hitting the bomb

3. Movements and Control
* Defined movement functions as move() to update the snake’s position and segment following logic. 
    * Added head.xcor() function to move the snake head horizontally and head.ycor() to move vertically
* Defined control functions as go_up(), go_down(), go_left(), go_right()
* Used wn.onkey() or wn.listen() to link keys to movement

4. Main Game loop
* Created a while True loop.
    * used time.sleep(delay) for controlling the game timing
    * Collision with fruit and star: Play sound, increase score, relocate fruit, grow snake segment, increase speed.
    * Collision with bomb: Play sound, trigger game over.
    * Collision with walls: Play sound, Trigger game over.
    * Collision with self: Play sound, Trigger game over.
    * Defined the variable speed_threshold  to increase speed with addition of two snake segments
    * Added len() function to increase the snake segment on eating fruit or star

5. Scores and “Game over” message
* Created a score display using turtle pen variable.
* Updated the score when fruit is eaten using update_score(), pen.clear() and pen.write() functions
* Added “game over” message when hitting the bomb, hitting walls and self-collision

6. Sound effects
* Imported sound effects  from YouTube
* Used pygame.mixer.init() function for sound effects
* Played sound effect for the following events:
    * Boing sound for the snake head hits the wall and self-collision 
    * Chomp sound on eating the fruit
    * Sparkle sound for eating the star
    * Kaboom for hitting the bomb

What I learned
* How to use Python modules together
* Game logic and loops
* Adding sound and graphics
* Debugging and testing
* Deploying my code in GitHub
* Creativity in coding!


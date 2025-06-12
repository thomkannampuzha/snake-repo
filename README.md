# About the “Snake Chaos” game
In Snake Chaos, your aim is to help the snake eat as much food as possible to grow longer and earn points, all while avoiding crashes into walls, itself, or surprise bombs. The game ends if the snake hits any of these obstacles. Special food (like stars) gives extra points and bonus growth, but bombs are dangerous traps that can end the game with a cool explosion animation.
You control the snake with the keyboard as it moves nonstop, and the more it grows, the faster it gets—making it harder to stay in control. Sound effects bring the game to life, and the score system keeps track of both your current score and your highest score. The challenge is simple: stay alive and get the highest score.




# Flow Chart for the “Snake Chaos” game
   
   <img width="785" alt="image" src="https://github.com/user-attachments/assets/fa5ffba7-7c1f-4b9a-a718-a8234ea88680" />




# Pseudo Code for the “Snake Chaos” game



Start game and load sounds
Initialize score, speed, and game state variables
Create window and draw snake, food, special food, bomb, and score display

      While game is running:
         Update screen
    
          If snake hits wall or itself:
            Play crash sound
           Reset game (score, snake, items)

          If snake eats food:
           Play chomp sound
           Move food to random location
           Add segment, increase score
           Speed up snake if needed

         If snake eats special food:
           Play sparkle sound
           Hide special food
           Add 2 segments, increase score
           Speed up snake more

         If snake hits bomb:
           Play explosion sound
           Show kaboom effect
           Reset game

     Move snake and all body segments
     Spawn special food and bombs at intervals
     Wait based on speed (delay) before next frame
    End game when player quits


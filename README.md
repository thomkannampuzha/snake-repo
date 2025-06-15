# About the “Snake Chaos” game
Get ready for Snake Chaos — a wild twist on the classic Snake game where things get faster, crazier, and more explosive the longer you survive! Guide your snake through a colourful arena, gobbling up juicy fruit and glowing stars to rack up points and grow longer. But beware: hidden bombs, sharp turns, and your own tail are out to end your run in a flash of chaos and sound. With every bite, the speed ramps up, your reflexes are tested, and the challenge gets real. Can you stay in control long enough to claim the high score — or will chaos swallow you whole?


# How to launch the game in your computer:
1. Download the repository as a .zip file:
   * Find the green "Code" button on the repository's main page. 
   * Click on the "Code" button and then select "Download ZIP" from the dropdown menu.  

2. Extract the .zip file:
   * Locate the downloaded .zip file on your computer. 
   8 Right-click on the .zip file and choose an option like "Extract All..." or "Extract Here" (the exact wording may vary depending on your operating system). 
* Choose a location to extract the files, such as your Desktop or a dedicated folder for games.  

3. Run the .exe file:
   * Once the .zip file is extracted, navigate to the extracted folder. 
   * Look for a file with the .exe extension, which is usually the game's executable file. 
   * Double-click the .exe file to launch the game.  


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


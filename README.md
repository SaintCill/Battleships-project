# Battleship Game

A simple battleship game built in python.


## Foreword about the project
This was created as a means to use what i have learned over the last month. The project was restarted a total of three times, as i was never quite happy with
the readability of the code. It initially used OOP, but i realized that the project was simple enough that using OOP actually made the readability worse. I also
understood that i knew way less about OOP and how to efficiently use it than i had thought, something that i am rectifying as you are reading this.

The project itself posed a fun challange, escpecially when i had to scrap old versions and start again, as it made me take what i had learned from previous attempts
and make the new ones better. It was, at times, an exercise in patience, even more so when i first realized that i should restart from scratch. As i was creating the
final version of this project, more and more ideas starting popping up, new features, new libraries to use, new headaches to solve. I came to a point where i had to
decide whether to finish the project as i had intended, or restart once more and create something half done. I decided to finish the current project and then shift
focus to truly understanding how to efficiently use OOP. I intend to remake this once i have archived an understanding, so that i may compare the two.

## About this project
This is, as i mentioned earlier, a simple battleship game made with python. It allows the player to chose the size of the board, and pits them against a computer, the
goal being to sink the computers battleships before they do the same to you. The code itself is basically made up of different functions that act together to create
the game envoirement. You might ask why i elected to not use classes and instead stick to functions, and that is a question i asked myself half way through this
itiration of the project. The simple answer is that i didn't really find any use for creating objects, as the ships don't really do anything other then get hit.


### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Replit version](https://www.example.com)
- [Python](https://www.example.com)


## Features

### Existing features

- Randomly created board
  - Ships are given a random position and orientation
- Play against the computer
- Accepts user input
- Maintain scores
- Input validation and error checking
  - You cannot enter coordinates outside of the chosen board size
  - Board size does not go above 10x10, and will tell the player this
  - Board does not accept strings and will print error message if string is input
  - Cannot enter the same guess twice

### Future features

- Additional game mode: 3 round system where you have to get more points than computer over the 3 rounds.
- More ship types utilizing classes.
- High scores
- Difficulty levels

## Data model

The board is being represented as a two dimensional list. Each cell on the board contains one of the following
values:
- "0": Empty cell
- "S": Ship cell (gets drawn over with a "0" for player.)
- "X": Hit ship cell

Ships themselves are represented as coordinates on the board, and stored inside the "Ship_locations" list. Things
such as game state are maintained and updated inside of the "update_board" function, where the specifics for both
"player_board" and "computer_board" is also being handled. "player_guess" stores the input from the user, which is
compared to the list of previous guesses inside of the "guesses" list. The main game loop is handled inside of the
"main()" function, where the game itself is set up. This includes taking turns, updating the board after each turn
and determining the winning side.

### Testing
The project has been manually tested by doing the following:
- Passed code through PEPB linter, without any problems outside of the odd spacing
- Given invalid inputs: strings where numbers are expected, out of bounds input, same input twice.
- Tested in VS code terminal, replit output and Atom terminal.


## Bugs

  - Ran into an issue while testing where ship locations weren't being marked on the board despite getting hit, solved
    this by creating a copy of all ship locations on a seperate list, and removed them from it instead.
  - Bug where it was impossible to win if multiple ships spawned on the same location, since the hit only removed one
    instance of a ship part on that coordinate. Utilized above fix to solve the issue.
  - Found a bug where the computer would win the game regardless of who sunk the ships first. This was caused by the
    code not differentiating between player and computer. Solved this by adding an additional parameter that checked
    if it was the players turn or not when the final ship was sunk.

## Remaining bugs
  - No bugs remain currently from my testing

## Validator testing
  - PEPB
    - No errors concerning functionality nor the code itself were returned from PEPBonline.com
      - There were some spacing issues from PEPB, where it wanted me to have a certain amount of spacing
        between lines, or where it was complaining about line lengths above 79 characters.

### Deployment

- Fork or copy this repository
- Run app through [heroku](https://www.heroku.com)
- Create new web service on [render](https://render.com) (heroku alternative)
- Fork [my repl](https://replit.com/@mguinart/Battleship)

### Credits

Code
  - bigmonty12 on github for the two dimensional list
  - bigmonty12 for the base of the "ships()" function, aswell as the suggestion of subtracting 1 to account for pythons 0-based indexing
  - ChatGPT for turning my gibberish into questions i could actually ask/search for in forums

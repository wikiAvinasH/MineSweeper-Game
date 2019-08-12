## Let’s play MineSweeper

The goal is that, a user needs to find the location of the secret mine that has been placed in any cell of a grid. If user is able to identify all the safe spots and the location of the mine is un-flagged, then the user win’s the game.

This is based on 3*3 DataFrame matrix and here is the visual representation of the minefield matrix.

![alt test](https://github.com/wikiAvinasH/GitHub-Repo-Folder/blob/master/MineSweeper.JPG)

## Requirement and Rules of the Game

* [Valid inputs are 1 to 9] [Opened cells will be marked as 'O'] [Mine cell as 'X']
* Create a 3*3 DataFrame matrix filled with 1-9 (Please refer the visual representation minefield matrix, highlighted in Red color)
* Hide the location of the mine in "one" specific cell using random funtion
* The goal of the game is to open all the “safe cells”
* If user opened cell has the mine then the user loses the Game
* If user opened a “safe” mine then the user is safe and the adjacent “safe cells” will also be “opened” and their values will be changed to 0 (Adjacent means that the cells share the common edge)
* Flagged mines to be denoted by X

### Prerequisites

Please find all the dependency python libraries that needs to be installed using pip utility
* pandas - pip install pandas
* sys
* tkinter

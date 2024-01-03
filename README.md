# ChessFENAgain

## DISCLAIMER
Please don't cheat in any online game. This project was just for my own interest. I would never use this against an online opponent, even if my rating is in the gutter (it is right now). YOU WILL GET BANNED IF YOU USE THIS ONLINE. You are a terrible human being if you use this against your friends. Only use against bots.

## Showcase
Improvements to ChessFEN. Speed optimizations incoming and less breakable code.
<br>
Undetectable for sure. Offline compatible as well (stronger if using stockfish GET api)
<br>
Still very unusable for anyone who isn't Me. Documentation coming soon.

![image](https://github.com/davidzhengyes/ChessFENAgain/assets/81645746/81604eda-1e1a-4fac-ba5a-0b27a9338791)
![image](https://github.com/davidzhengyes/ChessFENAgain/assets/81645746/1e3c0add-446d-4953-a4bf-fd8834c4cae0)


## Instructions
Highlight move MUST be unchecked!
<br>
For now, only works on boards with consistent dark and light squares, each dark/light square must be identical. Support for others may come in the future.
<br>
Need to have python PyPi packages installed: pyqt6, pyautogui, pillow, pynput pyside6?

<br> Should set up your own piece images before using.
<br> First, go to chess.com's analysis board. Next, in the "Initialize Pieces" Subwindow, click "Set Default Pieces" ONCE, then click the top-left and bottom-right corners of the board, making sure not to click on the white rook. Next, set up the board, and paste in the FEN "8/pqkp4/8/8/8/8/PQKP4/8 b - - 0 1". Click "Scan Extras". Next, go to any play against computer game, click "Game Board Loc" and then click the top-left and bottom-right corners. You are now ready to evaluate. Click either "White to move" or "Black to move", then "GetFEN".










## Possible Improvements (no particular order)
Automove (No click needed!)
<br> Lesser eval (Doesn't show the very best move)
<br> Better looking GUI, and more intuitive, so doesn't crash on a misinput
<br> Efficiency (Searching within the board and not the whole screen)
<br> Testing algorithm edge cases (User inaccuracy) and also can write a testing algorithm against games already played
<br> Modify algorithm so it can be used on chessboards with the rank and file indicator on the other side (capture smaller part of each piece)
<br> Wrap all into .exe, easier to run by everyone.
<br> Make options to specify castling availability, en passant, half-move clock and fullmove number (not necessary)



<br> stockfish version 16, taken from stockfish github june 30, 2023 release.



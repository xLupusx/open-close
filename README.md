# Open-Close Game

Open-Close is a simple game consisting of 2 players where one of them is the predictor. Each player has 2 hands that can be shown either face-up (Open) or face-down (Close). The predictor must predict how many of the hands will be open in the next round, if the predictor is correct, they win, if not, the next player become the predictor and the game continues on until there is a winner.

## About this project

This is a coding challenge that I did to apply for a company in January 2021, using Test Driven Development.

In this project, you'll be playing with an AI who makes moves randomly. Your input needs to be in the form of OC1 if you're the predictor, or OC if you're not. The first two characters must either be O or C, indicating the state of the hands that you yourself play, [O]pen or [C]lose, while the number act as your prediction, ranging from 0-4 as the maximum number of hands is 4.

Due to the game being developed using TDD, it was designed to catch various bad input errors to ensure it can meet requirements under all conditions.

## To run this project

Open your command prompt or terminal and run the command
```
$ cd openclose
$ python openclose.py
```

## To run the unit test

Open your command prompt or terminal and run the command
```
$ python -m unittest -v test_game.py
```

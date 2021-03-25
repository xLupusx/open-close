# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:50:18 2021

@author: Lupus
"""
import sys
from obj import ai
from obj import player
from functions import gameJudge
from functions import validateInput
    
def gameInit():
    pc.moveInput=""
    npc.moveInput=""
    pc.isPredictor, npc.isPredictor = npc.isPredictor, pc.isPredictor #swap predictor everytime a new round is played    
    gameStart()    

def gameStart():
    if pc.isPredictor:
        print("\nYou are now the predictor, what is your input?")
        playerInput = input("You:").upper().strip()
        correct = validateInput(pc.isPredictor, playerInput) #validate input
        if correct:
            pc.moveInput = playerInput
            npc.moveInput = npc.randMove()
            print("AI: "+npc.moveInput)
        else: 
            gameStart()
    else:
        print("\nAI is now the predictor, what is your input?")
        playerInput = input("You:").upper().strip()
        correct = validateInput(pc.isPredictor, playerInput) #validate input
        if correct:                   
            pc.moveInput = playerInput
            npc.moveInput = npc.randMove()+npc.randPrediction()        
            print("AI: "+npc.moveInput)
        else:
            gameStart()
    gameStatus = gameJudge(pc.isPredictor,pc.moveInput,npc.moveInput)
    if gameStatus == 2:  #game ends at 0 (player lost) or 1 (player win) otherwise it continues on
        print("No winner")
        gameInit()
    else:
        if gameStatus == 1:
            print("You WIN!")
            yes = newGame()
        if gameStatus == 0:
            print("You LOST!")
            yes = newGame()
        if yes:
            gameInit()
        else:
            print("Alright, see you later!")
            sys.exit()
            
def newGame():
    answer = input("Would you like to play again? (Y/N) :").lower().strip()
    if answer not in ['y', 'n']:
        print("Invalid input. Please only enter Y for (Y)es or N for (N)o")
        return newGame()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    
# MAIN PORTION
   
print("Welcome to the Open-Close game!")
pc = player()
npc = ai()
pc.isPredictor=False #player start out as predictor first, but this value will be switched later at gameInit
npc.isPredictor=True
gameInit() #First Run
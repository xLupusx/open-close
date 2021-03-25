# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:49:40 2021

@author: Lupus
"""

import unittest
from openclose.functions import gameJudge
from openclose.functions import validateInput

class TestGame(unittest.TestCase):
    def test_predictor_win(self):
        isPredictor = True
        playerInput = "CC1"        
        aiInput = "OC"
        gameStatus = gameJudge(isPredictor,playerInput,aiInput)        
        self.assertTrue(validateInput(isPredictor,playerInput)) #If this function return True, input is valid
        self.assertEqual(gameStatus,1) # 1 means player win
        
    def test_predictor_draw(self):
        isPredictor = True
        playerInput = "OO4"
        aiInput = "CO"
        gameStatus = gameJudge(isPredictor,playerInput,aiInput)
        self.assertTrue(validateInput(isPredictor,playerInput))
        self.assertEqual(gameStatus,2) # 2 means draw
        
    def test_player_draw(self):
        isPredictor = False
        playerInput = "OO"
        aiInput = "CO1"
        gameStatus = gameJudge(isPredictor,playerInput,aiInput)
        self.assertTrue(validateInput(isPredictor,playerInput))
        self.assertEqual(gameStatus,2) # 2 means draw
        
    def test_player_lose(self):
        isPredictor = False
        playerInput = "CO"
        aiInput = "OC2"
        gameStatus = gameJudge(isPredictor,playerInput,aiInput)
        self.assertTrue(validateInput(isPredictor,playerInput))
        self.assertEqual(gameStatus,0) # 0 means ai win
    
    def test_bad_value_predictor_1(self):        
        isPredictor = True
        playerInput = "CC8"
        self.assertFalse(validateInput(isPredictor,playerInput)) #If this function return False, input is invalid
            
    def test_bad_value_predictor_2(self):
        isPredictor = True
        playerInput = "CC"
        self.assertFalse(validateInput(isPredictor,playerInput))   
    
    def test_bad_value_predictor_3(self):
        isPredictor = True
        playerInput = "chicken"
        self.assertFalse(validateInput(isPredictor,playerInput))   

    def test_bad_value_player_1(self):
        isPredictor = False
        playerInput = "CC3"
        self.assertFalse(validateInput(isPredictor,playerInput))   
            
    def test_bad_value_player_2(self):
        isPredictor = False
        playerInput = "chicken"
        self.assertFalse(validateInput(isPredictor,playerInput))   

if __name__ == '__main__':
    unittest.main()
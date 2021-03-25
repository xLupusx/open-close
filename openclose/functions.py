# -*- coding: utf-8 -*-
def gameJudge(isPredictor,playerInput,aiInput):    
    allHands = playerInput+aiInput
    #counting Open hands
    count = 0
    for x in allHands:
        if x == 'O':
            count += 1
    if isPredictor:
         prediction = int(playerInput[2])
         if count == prediction:
             return 1
         else:
             return 2
    else:
        prediction = int(aiInput[2])
        if count == prediction:
            return 0
        else:
            return 2    
#------------------------        
valid_move_list = ["C","O"]
valid_prediction_list = ["0","1","2","3","4"]
        
def validateInput(isPredictor,playerInput):
    if isPredictor:
        try: #Check input validity
            if len(playerInput)==3 and playerInput[0] in valid_move_list and playerInput[1] in valid_move_list and playerInput[2] not in valid_prediction_list:
                print("\nInvalid input. Prediction should only be in the range of 0-4")
                raise ValueError
            if len(playerInput)==2 and playerInput[0] in valid_move_list and playerInput[1] in valid_move_list:
                print("\nInvalid input. You are the predictor, please also enter prediction.")
                raise ValueError                
            if len(playerInput)<3 or playerInput[0] not in valid_move_list or playerInput[1] not in valid_move_list or len(playerInput)>3:                    
                print("\nInvalid input. Correct input should be exactly 3 characters\n"
                      "and in the form of OC1, where the first two letters are O or C, \n"
                      "indicating [O]pen or [C]lose state for each hand, followed by the prediction (0-4)")
                raise ValueError
        except ValueError:
            print("Please enter valid input")
            return False
        return True
    else:
        try:
            if len(playerInput)==3 and playerInput[0] in valid_move_list and playerInput[1] in valid_move_list and playerInput[2] in valid_prediction_list:
                print("\nInvalid input. You are not the predictor, please only enter hands")
                raise ValueError
            if playerInput[0] not in valid_move_list or playerInput[1] not in valid_move_list or len(playerInput)>2:                    
                print("\nInvalid input. Correct input should be exactly 2 characters\n"
                      "and in the form of OC, where O and C indicate [O]pen or [C]lose state for each hand")
                raise ValueError
        except ValueError:
                print("\nPlease enter valid input")
                return False
        return True
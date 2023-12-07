from assets.settings import *

# game's main interfaces.

def title_game():
    print('\n-----------------------------------')

    print('\n      Math Quiz Console Game')

    print('\n-----------------------------------')
    return

def user_input():
    return str(input('Command: '))

def start_menu():
    while True:
        print('\nStart Game (1): ')
        print('Settings (2): ')
        print('Exit (3): \n')
        
        x = user_input()
        
        if (x in ["1","2","3"]):
            return x
        
        print('\nUnknown Input.')
        
def start_game_menu():
    settings = loadJSON()
    score = [0,0] # correct, wrong
    
    for x in range (1,settings['numItems']+1):
        num1, num2 = randomize_quiz(settings['level'],settings['op']) # the question
        true_answer = get_answer(num1, num2, settings['op'])
        
        choices = randomize_options(true_answer, settings['ansVariety'])
        
        print("\n-- Question --\n")
        print(f"{num1} {get_op_str(settings['op'])} {num2} = ?")
        
        answer = user_input()
        
        score = verify_answer(answer, true_answer, score)
        
    print("\nGame End!\n")
    print("Final Score:")
    print(f"Correct: {score[0]}\nWrong: {score[1]}")

def custom_level():
    while True:
        print("\n-- Custom Level Modify --\n")
        
        print("Min (1):")
        min = user_input()
        print("Max (999):")
        max = user_input()
        
        limit = [str(x) for x in range(1,1000)]
        if(min in limit and max in limit):
            return {3:f"{min}-{max}"}
        else:
            print("\nUnknown Input")

def modify_level(): # Level: 1, 2 or custom
    while True:
        print("\n-- Operator Modify --")
        print("Level 1-10 (1): ")
        print("Level 11-100 (2): ")
        print("Custom Level ?-? (3): {} - {}")
        print('-----------------------\n')
        
        x = user_input()
        
        match x:
            case "1": return {1:"1-10"}
            case "2": return {2:"11-100"}
            case "3": return custom_level()
        print("\n Unknown Input.")
    
    
def modify_op(): # Operator: Add, Sub, or Mul
    curOp = ""
    while True:
        print("\n-- Operator Modify --")
        print("Addition (1): ")
        print("Subtraction (2): ")
        print("Multiplication (3): ")
        print("Go Back (4): ")
        print('-----------------------\n')
        
        x = user_input()
        
        match x:
            case "1": return 1
            case "2": return 2
            case "3": return 3
            case "4": return
            
        print("\n Unknown Input.")

def modify_num_items(): # Number of items : <int>
    while True:
        print("\n-- Number of Items Modify --")
        print("\nMin: 1, Max: 100")
        print("Type '0' to exit:\n")
        print('------------------------------\n')
        
        x = user_input()
        
        if(x in [str(x) for x in range(1,101)]):
            return x
        elif(x == "0"):
            return
        print("\n Unknown Input.")
        
def modify_ans_variety(): # distant values between options (there are four options.)
    while True:
        print("\n-- Answer Variety Modify --")
        print("\nMin: 1, Max: 100")
        print("Type '0' to exit:\n")
        print('------------------------------\n')    
        
        x = user_input()
        
        if(x in [str(x) for x in range(1,101)]):
            return x
        elif(x == "0"):
            return
        print("\n Unknown Input.")
        

def settings_menu():
    while True:
        settings = loadJSON()
        print('\n-- Current Settings --')
        print(f"Difficulty Level (1): {settings['level']}")
        print(f"Chosen Operator (2): {settings['op']}")
        print(f"Number of Items (3): {settings['numItems']}")
        print(f"Answer Variety (4): {settings['ansVariety']}")
        print('Exit (5)')
        print('----------------------\n')
        
        x = user_input()
        tgt_setting = ""
        match x:
            case "1": 
                tgt_setting = "level"
                new_value = modify_level()
            case "2": 
                tgt_setting = "op"
                new_value = modify_op()
            case "3": 
                tgt_setting = "numItems"
                new_value = modify_num_items()
            case "4": 
                tgt_setting = "ansVariety"
                new_value = modify_ans_variety()
            case "5": return

        if(x in ["1","2","3","4"] and new_value != None):
            settings_modify(tgt_setting, new_value)
        else:
            print('\nUnknown Input.')
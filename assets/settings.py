import json

def createJSON(): # writes default settings
    default_settings = {
        "level": {1:"1-10"},
        "op": 1, #1 = add, 2 = sub, 3 = mul
        "numItems": 5,
        "ansVariety": 5, # 5 below the correct answer and 5 above the correct answer, for randrange
    }
    
    with open('assets/settings_data.json', 'w') as json_file:
        json.dump(default_settings, json_file)
        return
    
def loadJSON(): # reads json file
    try:
        with open('assets/settings_data.json', 'r') as json_file:
            x = json.load(json_file)
            return x
    except:
        createJSON()
        return loadJSON()

def settings_modify(specified_setting, new_value): # only changes one setting at a time.
        settings_data = loadJSON()
        
        settings_data[specified_setting] = new_value # modifies a specific setting
        
        with open('assets/settings_data.json', 'w') as json_file:
            json.dump(settings_data, json_file) # recreates a new json with modified setting


import random as rnd
def randomize_options(answer, ansVariety): # returns 4 options in a list and in randomized order.
    ans_list = [0,0,0,0]
    ansVariety = int(ansVariety)
    
    for x in range(0,4):
        ans_list[rnd.randrange(0,4)] = rnd.randrange(answer - ansVariety,answer + ansVariety)
    return ans_list

def randomize_quiz(level, op):
    level = level[list(level.keys())[0]]
    
    level_range = (level.split("-"))
    
    level_range[0] = int(level_range[0])
    level_range[1] = int(level_range[1])
    
    while True:
        num1 = rnd.randrange(level_range[0], level_range[1])
        num2 = rnd.randrange(level_range[0], level_range[1])
        
        if(num1 >= num2):
            return num1, num2

def get_answer(num1, num2, op):
    match op:
        case 1: return num1 + num2
        case 2: return num1 - num2
        case 3: return num1 * num2
    return

def verify_answer(answer, true_answer, score):
    if (int (answer) == int(true_answer)):
        print("\nCorrect!")
        score[0] += 1
    else:
        print(f"\nWrong... Answer: {true_answer}")
        score[1] += 1
    return score

def get_op_str(op):
    match op:
        case 1 : return "+"
        case 2 : return "-"
        case 3 : return "x"
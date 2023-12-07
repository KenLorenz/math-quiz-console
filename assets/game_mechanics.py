import random as rnd
def randomize_options(true_answer, ansVariety): # returns 4 options in a list and in randomized order.
    ans_list = [0,0,0,0]
    ansVariety = int(ansVariety)
    
    for x in range(0,4):
        while True:
            rnd_wrong_ans = rnd.randrange(true_answer - ansVariety,true_answer + ansVariety)
            if(rnd_wrong_ans not in ans_list and rnd_wrong_ans != true_answer and (rnd_wrong_ans < 0) == False):
                ans_list[x] = rnd_wrong_ans
                break
            
    ans_list[rnd.randrange(0,4)] = true_answer
    
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
    
def game_end(correct, wrong):
    print("\nGame End!\n")
    print("Final Score:")
    print(f"Correct: {correct}\nWrong: {wrong}\nTotal: {correct + wrong}")
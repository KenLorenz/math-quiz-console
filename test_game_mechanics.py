from assets.game_mechanics import *
from game import *

import unittest

class GameMechanicsTestCase(unittest.TestCase):
    
    def test_randomize_quiz(self):
        
        x, y = randomize_quiz({"1":"1-10"})
        
        limit = [v for v in range(1-11)]
        if(x in limit and y in limit):
            z = True
        else:
            z = False
        
        self.assertTrue(z)
        
    def test_get_answer_sum(self):
        
        x = get_answer(5,5,1)
        
        self.assertEqual(x,10)
        
    def test_get_answer_sub(self):
        
        x = get_answer(10,5,2)
        
        self.assertEqual(x,10)
        
    def test_get_answer_mul(self):
        
        x = get_answer(10,5,3)
        
        self.assertEqual(x,50)
        
    def test_verify_answer_correct(self):
        score = [0,0]
        x = verify_answer(10,10,score)
        
        self.assertEqual(1,score[0])
        
    def test_verify_answer_wrong(self):
        score = [0,0]
        x = verify_answer(10,9,score)
        
        self.assertEqual(1,score[1])
        
    def test_get_op_str(self):
        x = get_op_str(1)
        self.assertEqual("+", x)
from assets.settings import *
from assets.game_mechanics import *

import unittest

class SettingsTestCase(unittest.TestCase):
    
    def test_loadJSON(self):
        
        x = loadJSON()
        
        self.assertEqual(type({1:1}), type(x))
from MonteCarlo import MonteCarloSimulator as MC
import pandas as pd
import unittest

class MonteCarloSimulatorTestSuite(unittest.TestCase):
'''
Simple unit tests for the MonteCarloSimulator package. One unit test per method for all classes.

Tests
-----
    test_change_weight()
        creates a Die objects and changes the weight of the first face value. Checks that the new weight is in the dataframe.

    test_roll()
        creates a Die object and rolls using the default number of rolls (1). Checks that the method returns a dataframe of length 1.

    test_show_die()
        creates a Die object with 3 face values. Checks that the method returns a dataframe of shape 3 rows (face values) x 2 columns (face values and weights).

    test_play()
        creates a Game object with 3 Die objects and plays the Game with 3 rolls. Checks that the method returns a dataframe of shape 3 rows (rolls) x 3 columns (number of dice).

    test_show_game()
        creates a Game object with 3 Die objects and plays the Game with 3 rolls. Checks that the method returns a dataframe of shape 3 rows (rolls) x 3 columns (number of dice) when "wide" parameter is passed 
        and a dataframe of shape 9 rows (rolls of all 3 Die) x 1 column (face value rolled) when the "narrow" parameter is passed.

    test_jackpot()
        creates an Analyzer object with a Game where each roll results in a jackpot. creates an Analyzer object with a Game where no roll results in jackpot. Checks that the first method returns the number of 
        rolls and the second method returns 0.

    test_combo()
        creates an Analyzer object with a Game where each roll results in the same combination of face values. Checks that the data frame returned has 1 row.

    test_face_counts_per_roll()
        creates an Analyzer object with a Game where each roll results in the same combination of face values. Checks that the data frame returned has 1 column.
'''
    
    def test_change_weight(self):
    '''
    Creates a Die objects and changes the weight of the first face value. 
    Returns True if the new weight is in the dataframe at the position of the face value invoked.
    '''
        vals = [1, 2, 3]
        die = MC.Die(vals)
        
        die.change_weight(1, 2)
        msg = "weight was not changed"
        self.assertTrue(die.show_die().iloc[0][1] == 2, msg)
        
    def test_roll(self):
    '''
    Creates a Die object and rolls using the default number of rolls (1). 
    Returns True if the method returns a dataframe of length 1.
    '''
        vals = [1, 2, 3]
        die = MC.Die(vals)
        
        msg = "die was not correctly rolled"
        self.assertTrue(len(die.roll()) == 1, msg)
        
    def test_show_die(self):
    '''
    Creates a Die object with 3 face values. 
    Returns True if the method returns a dataframe of shape 3 rows (face values) x 2 columns (face values and weights).
    '''
        vals = [1, 2, 3]
        die = MC.Die(vals)
        
        msg = "data frame was not correctly generated"
        self.assertTrue(die.show_die().shape == (3,2), msg)
        
    def test_play(self):
    '''
    Creates a Game object with 3 Die objects and plays the Game with 3 rolls. 
    Retruns True if the method returns a dataframe of shape 3 rows (rolls) x 3 columns (number of dice).
    '''
        vals = [1, 2, 3]
        die = MC.Die(vals)
        dice = [die, die, die]
        
        game = MC.Game(dice)
        game.play(3)
        msg = "data frame was not correctly generated"
        self.assertTrue(game.show_game().shape == (3,3), msg)
        
    def test_show_game(self):
    '''
    creates a Game object with 3 Die objects and plays the Game with 3 rolls. 
    Returns True if the method returns a dataframe of shape 3 rows (rolls) x 3 columns (number of dice) when "wide" parameter is passed and a dataframe of shape 9 rows (rolls of all 3 Die) x 1 column (face 
    value rolled) when the "narrow" parameter is passed.
    '''
        vals = [1, 2, 3]
        die = MC.Die(vals)
        dice = [die, die, die]
        
        game = MC.Game(dice)
        game.play(3)
        msg = "data frame was not correctly generated"
        self.assertTrue(game.show_game('wide').shape == (3,3) and game.show_game("narrow").shape == (9,1), msg)
        
    def test_jackpot(self):
    '''
    Creates an Analyzer object with a Game where each roll results in a jackpot. Creates an Analyzer object with a Game where no roll results in jackpot. 
    Returns True if the first method returns the number of rolls and the second method returns 0.
    '''
        vals1 = [1, 1]
        die1 = MC.Die(vals1)
        dice1 = [die1, die1]
        game1 = MC.Game(dice1)
        game1.play(3)
        
        vals2 = [2, 2]
        die2 = MC.Die(vals2)
        dice2 = [die1, die2]
        game2 = MC.Game(dice2)
        game2.play(3)
        
        anz1 = MC.Analyzer(game1)
        anz2 = MC.Analyzer(game2)
        
        jp1 = anz1.jackpot()
        jp2 = anz2.jackpot()
        
        
        msg = "jackpot does not calculate correctly"
        self.assertTrue(jp1 == 3 and jp2 == 0, msg)
    
    def test_combo(self):
    '''
    Creates an Analyzer object with a Game where each roll results in the same combination of face values. 
    Returns True if the data frame returned has a length of 1.
    '''
        vals = [1, 1, 1]
        die = MC.Die(vals)
        dice = [die, die, die]
        
        game = MC.Game(dice)
        game.play(3)
        
        anz = MC.Analyzer(game)
        msg = "combo does not calculate correctly"
        self.assertTrue(len(anz.combo()) == 1, msg)

    def test_face_counts_per_roll(self):
    '''
    Creates an Analyzer object with a Game where each roll results in the same combination of face values. 
    Returns True if the data frame returned has 1 column.
    '''
        vals = [1, 1, 1]
        die = MC.Die(vals)
        dice = [die, die, die]

        game = MC.Game(dice)
        game.play(3)

        anz = MC.Analyzer(game)
        msg = "face_counts_per_roll does not calculate correctly"
        self.assertTrue(len(anz.face_counts_per_roll().columns.values) == 1, msg)
        
if __name__ == '__main__':

    unittest.main(verbosity=3)
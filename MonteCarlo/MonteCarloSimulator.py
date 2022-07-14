import pandas as pd
import numpy as np

class Die():
    '''
    A class to represent a 'die' and pull a random sample from the die. Die defaults to equal weights, or can be weighted to favor some values 
    more than others. 

        Attributes: 
        ----------
        face (np.array) : an array of strings or numbers that represent the faces of die
        weight (np.array(float)) : an array of weights for corresponding faces. Default 1.0, can be change with change_weight()

        Methods:
        --------
        change_weight(face_val, new_weight) 
            changes the weight of the indicated face

        roll(num_rolls = 1)
            returns a weighted random sample of rolls from the faces with replacement 

        show_die()
            returns the dataframe with the current face and weight values
    '''
    def __init__(self, faces):
        '''
        Constructs all the necessary attributes for the die object.

        Parameters
        ----------
            faces : np.array(str or int)
                array of string or integer values of die "faces"/"sides"         
        '''
        self.faces = np.array(faces)
        self._die_df_ = pd.DataFrame()
        self._die_df_["face"] = self.faces
        self._die_df_['weight'] = 1.0
        
    def change_weight(self, face_val, new_weight):
        '''
        Changes the weighting of the indicated face.

        Parameters
        ----------
            face_val : str or int
                face to have weight changed
            new_weight : float
                new weight for face_val
        Returns
        -------
            None
        '''
        ##parameter errors
        if face_val not in self._die_df_.face.values:
            return "Error: value is not on die. Please enter a face value on the die."
        else:
            next
        if type(new_weight) != 'float' and type(new_weight) != 'int':
            float(new_weight)
        
        ##replace entire row with face_val and new weight
        idx = self._die_df_.index[self._die_df_['face'] == face_val]
        self._die_df_.loc[idx, ['face', 'weight']] = [face_val, new_weight]
        
        
    def roll(self, num_rolls = 1):
        '''
        Creates a weighted random sample of size num_rolls from the faces of the die with replacement.

        Parameters
        ----------
            num_rolls : int
                number of times the die is to be rolled. default = 1
        Returns
        -------
            Dataframe containing results of random sample
        '''
        ##random sample
        return pd.DataFrame(self._die_df_.sample(num_rolls, weights = self._die_df_[:]["weight"], replace = True))
    
    def show_die(self):
        '''
        Shows current faces and weights on die.

        Parameters
        ----------
            None

        Returns
        -------
        _die_df_ (pd.DataFrame) : Dataframe containing current face and weight values.
        '''
        return self._die_df_

class Game():
    '''
    A class to represent a game where 1 or more die are rolled. 

        Attributes: 
        ----------
            dice (list(Die objects)) : a list of already initiated Die objects

        Methods:
        --------
            play(rolls) 
                rolls the die in dice rolls number of times

            show_game(show = "wide")
                returns a dataframe of the most recent play in a wide (default) or narrow format
    '''

    def __init__(self, dice):
        '''
        Constructs all the necessary attributes for the Game object. Checks that all die have the same number of faces

        Parameters
        ----------
            dice : list(Die objects)
                a list of already initiated Die objects - all Die must have the same number of faces        
        '''        
        self.dice = dice
        
        #checks to make sure that all die have same number of faces
        faces = len(dice[0].show_die())
        self._play_df_ = pd.DataFrame()
        for d in dice:
            if len(d.show_die()) != faces:
                print("Error: dice must have the same number of faces.")

    def play(self, rolls):
        '''
        Rolls all of the die in the dice list. Saves results in a private dataframe.

        Parameters
        ----------
            rolls : int
                number of times each die is to be rolled

        Returns
        -------
            None
        '''
        self._play_df_ = pd.DataFrame()
        i = 1
        
        ##roll each die and add values to dataframe 
        for die in self.dice:
            temp = pd.DataFrame({"die" + str(i): die.roll(num_rolls = rolls).face})
            temp = temp.reset_index(drop = True)
            self._play_df_ = pd.concat([self._play_df_, temp], axis = 1)
            i+= 1
        
        ##change indexing to start @1 and name roll
        self._play_df_.index = np.arange(1, len(self._play_df_) + 1)
        self._play_df_.index.rename("roll", inplace = True)
    
    def show_game(self, show = "wide"):
        '''
        Shows results of the most recent play in a dataframe. Can be displayed as a wide table (default) or a narrow table.

        Parameters
        ----------
            show : str
                "wide" or "narrow", default = "wide"

        Returns
        -------
            _play_df_ (pd.DataFrame) : Dataframe containing results of most recent play.
        '''
        ##pass dataframe to user in narrow or wide format
        if show == "narrow":
            print_df = self._play_df_.copy()
            print_df = print_df.stack().to_frame("faces")
            return print_df
        elif show == "wide":
            return self._play_df_
        
        ##print error message if invalid parameter is passed
        else:
            return 'Error: enter a valid table type, "narrow" or "wide".'
        
class Analyzer():
        '''
        A class to analyze the a Game object where 1 or more Die objects are rolled to create a random sample.

        Attributes: 
        ----------
            game (Game) : a Game object that has been played

        Methods:
        --------
            jackpot() 
                returns the number of times all die roll the same value

            combo()
                returns a dataframe with all the combinations of face values rolled and the counts for each

            face_counts_per_roll()
                returns a dataframe with a count for each face on each roll
        '''    
    def __init__(self, game):
        '''
        Constructs all the necessary attributes for the Analyzer object.

        Parameters
        ----------
            game : Game object
                a Game object that has been played to be analyzed        
        '''
        self.game = game
        die_type = type(self.game.dice[:])
        self.face_df = pd.DataFrame()
        
    def jackpot(self):
        '''
        Determines the number of "jackpots" in a roll - where all die roll the same face value. Returns the number of jackpots in the game.

        Parameters
        ----------
            None

        Returns
        -------
            int : number of jackpots rolled in game
        '''
        jackpot_df = self.game.show_game()
        jackpot_results = pd.DataFrame()
        
        ##grab each row of dataframe
        for i in jackpot_df.index.values:
            x = jackpot_df.loc[i].to_list()
            val = x[0]
            
            ##check if values in row e the same
            for X in x:
                if val == X:
                    result = True
                else:
                    result = False
                    break
            
            ##add "jackpot" rows with all the same value to new dataframe
            if result == True:
                x_df = pd.DataFrame(x).T
                jackpot_results = pd.concat([jackpot_results, x_df], axis = 0)
        
        ##change indexing to start @1 and name roll
        jackpot_results.index = np.arange(1, len(jackpot_results) + 1)
        jackpot_results.index.rename("roll", inplace = True)
        
        ##return number of jackpots to the user
        return len(jackpot_results) 
        
    def combo(self):
        '''
        Returns a dataframe with all combinations of face values rolled and cooresponding counts for each combination.

        Parameters
        ----------
            None

        Returns
        -------
            face_df (pd.DataFrame) : combinations of face values and counts
        '''
        ##shows count of combinations rolled
        self.face_df = self.game._play_df_.apply(lambda x: pd.Series(sorted(x)), 1)\
         .value_counts()\
         .to_frame('count')
        
        return self.face_df
    def face_counts_per_roll(self):
        '''
        Returns a dataframe with number or times each face value was rolled in each roll.

        Parameters
        ----------
            None

        Returns
        -------
            f_count (pd.DataFrame) : count of each face value for each roll
        '''
        #counts how many times each face was rolled per roll
        self.f_count = self.game.show_game().apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        
        return self.f_count
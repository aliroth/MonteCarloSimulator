# Metadata
--------------------
## Ali Roth
### Monte Carlo Simulator
### DS5100 Final Project
--------------------
# Synopsis

![image](https://user-images.githubusercontent.com/107503014/179130008-6fe870ca-a339-4eae-8174-98b6c701d281.png)
[image source](https://www.quantamagazine.org/how-and-why-computers-roll-loaded-dice-20200708/)

The MonteCarlo package uses a Die() to generate a random sample of variables with replacement. According to  University of Virginia Professor Dr. Rafael Alvarado, 


"Monte Carlo methods are family of techniques first developed by physicists in the 1940s to predict the outcomes of complex stochastic processes, such as nuclear fission and fusion. The behavior of random variables are modeled by chance mechanisms such as dice and computers, using random number generators. The data generated by these mechanisms through sampling are employed to influence the direction of a process."

This package also includes a Game() class to generate samples from multiple Die and an Analyzer() to compile information on the sample results. 

## &ensp;&ensp;&ensp;&ensp; installing
To install the package, clone the git hub repo, navigate into the repo director, and then install the package in a command line. An example for a windows machine is included below.
```python
#clone repo
git clone https://github.com/aliroth/MonteCarloSimulator.git

# navigate into the repo directory
cd MonteCarloSimulator

# install package
pip install MonteCarlo
```
## &ensp;&ensp;&ensp;&ensp; importing
```python
from MonteCarlo import MonteCarlo as MC
```
## &ensp;&ensp;&ensp;&ensp; Creating dice
---
Create a list of face values for your Die object. For this example a Die to represent a coin with H (heads) and T (tails values).

```python
coin_vals = ['H', 'T']

# initialize a Die object, passing the face values in the parameters
coin = MC.Die(coin_vals)
```

Change the weight of any face value on an instantiated die using the change_weight() method. Pass the face value to change and the new weight in the parameters. The example below sets the weight of heads to 5.
```python
coin.change_weight('H', 5)
```

Pull a random sample from your die using the roll() method. Pass the number of times to be rolled in the parameters, or use the default value of 1.
```python
# rolls the coin once 
coin.roll()

# rolls the coin 5 times
coin.roll(5)
```

Display the current face values and weights of the die using the .show_die() method.
```python
coin.show_die()
```

**Example output**

|   | face | weight |
|--:|-----:|:------:|
| 0 |    H |    5.0 |
| 1 |    T |    1.0 |



## &ensp;&ensp;&ensp;&ensp; Playing games
---
To play a game with 1 or more Die objects, create a list of previously created Die objects. Initialize a Game object, passing the list of Die objects in the parameters.

```python
# list of Die objects 
coins = [coin, coin, coin]

# initialize a Game object
game = MC.Game(coins)
```

Call the play() method to pull a random sample of all of your Die in the Game, passing the number of rolls - in this case, 10 rolls - to be played in the Game in the parameter. 
**This MUST be done before an Analyzer object can be used on the game**
```python
game.play(10)
```

To dispay the results of the most recent play(), call the show_game() method on the Game object.
```python
game.show_game()
```

**Example output**

| roll | die1 | die2 | die3 |
|-----:|-----:|-----:|------|
|    1 |    T |    H |    H |
|    2 |    T |    T |    H |
|    3 |    T |    H |    H |
|    4 |    H |    H |    H |
|    5 |    H |    T |    H |
|  ... |  ... |  ... |  ... |


## &ensp;&ensp;&ensp;&ensp; Analyzing games
---
To analyze a played Game, initialize an Analyzer object, passing the Game object in the parameters.

```python
# initialize an Analyzer object
anz = MC.Analyzer(game) 
```

To find the number of "Jackpots" (a roll where every die rolls the same value) in a game, use the .jackpot() method. This retruns the number of jackpots in the game being analyzed.
```python
# run the jackpot method
anz.jackpot()
```

To find all combinations of face values and the counts for each combination, use the combo() method. This displays a dataframe with the combinations and counts sorted by most frequent combination.
```python
# run the jackpot method
anz.combo()
```
**Example output**

|   |   |   | count |
|--:|--:|--:|-------|
| 0 | 1 | 2 |       |
| H | H | T |   462 |
|   |   | H |   363 |
|   | T | T |   165 |
| T | T | T |    10 |
|   |   |   |       |

To find the counts of each face value on each roll, use the face_vaues_per_roll() method. This displays a dataframe with the counts for each face value for each roll.
```python
# run the jackpot method
anz.face_counts_per_roll()
```

**Example output**

| roll |   H |   T |
|-----:|----:|----:|
|    1 |   2 |   1 |
|    2 |   1 |   2 |
|    3 |   2 |   1 |
|    4 |   3 |   0 |
|    5 |   2 |   1 |
|  ... | ... | ... |



# API description

## Die() Class
A class to represent a 'die' and pull a random sample from the die. Die defaults to equal weights, or can be weighted to favor some values more than others. 

        Attributes: 
        ----------
        face (np.array) : an array of strings or numbers that represent the faces of die 
        weight (np.array(float)) : an array of weights for corresponding faces. Default 1.0, can be change with change_weight()

        Methods:
        --------
        change_weight(face_val, new_weight)
            changes the weight of the indicated face
                Parameters
                ----------
                    face_val : str or int
                        face to have weight changed
                    new_weight : float
                        new weight for face_val
                Returns
                -------
                    None  

        roll(num_rolls = 1)
            returns a weighted random sample of rolls from the faces with replacement 
                Parameters
                ----------
                num_rolls : int
                    number of times the die is to be rolled. default = 1
                Returns
                -------
                    Dataframe containing results of random sample

        show_die()
            returns the dataframe with the current face and weight values
                Parameters
                ----------
                    None

                Returns
                -------
                _die_df_ (pd.DataFrame) : Dataframe containing current face and weight values.

## Game() class
A class to represent a game where 1 or more die are rolled. 

        Attributes: 
        ----------
            dice (list(Die objects)) : a list of already initiated Die objects

        Methods:
        --------
            play(rolls) 
                rolls the die in dice rolls number of times
                Parameters
                ----------
                    rolls : int
                        number of times each die is to be rolled

                Returns
                -------
                    None

            show_game(show = "wide")
                returns a dataframe of the most recent play in a wide (default) or narrow format
                Parameters
                ----------
                    show : str
                        "wide" or "narrow", default = "wide"

                Returns
                -------
                    _play_df_ (pd.DataFrame) : Dataframe containing results of most recent play.
                
## Analyzer() Class
A class to analyze the a Game object where 1 or more Die objects are rolled to create a random sample.

    Attributes: 
    ----------
        game (Game) : a Game object that has been played

    Methods:
    --------
        jackpot() 
            returns the number of times all die roll the same value
                Parameters
                ----------
                    None

                Returns
                -------
                    int : number of jackpots rolled in game

        combo()
            returns a dataframe with all the combinations of face values rolled and the counts for each
                Parameters
                ----------
                    None

                Returns
                -------
                face_df (pd.DataFrame) : combinations of face values and counts

        face_counts_per_roll()
            returns a dataframe with a count for each face on each roll
                Parameters
                ----------
                    None

                Returns
                -------
                    f_count (pd.DataFrame) : count of each face value for each roll

# Manifest
Files incuded in this package:

- MonteCarlo.py
- montecarlo_demo.ipynb
- final-project-submission.ipynb
- MonteCarloSimulatorTestSuite.py
- MonteCarloSimulator_testresults.txt
- __init__.py
- setup.py
- director.py


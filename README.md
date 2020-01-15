# PokerMachineTrainigCenter

## external libraries
- https://github.com/ishikota/PyPokerEngine

## Steps to finnish:
- implement player which will decide based on deep neural network
- calculate probability of having best cards at the end of game for every player after every      round (from pypokerengine.engine.hand_evaluator import HandEvaluator)
- NN inputs: (All cach values are downscaled so that biggest stash on table is 1)
  - probability of winning for every player - 10 inputs
  - position at table/no. of players        - 1  input
  - last bet, total bet, total cash for all - 30 inputs
  - minimal bet to continue playing         - 1  input
 - NN outputs:
  - value of bet, if smaller then min       - 1 output
    than min bet is played
  - quit, if > 0,5 than flop                - 1 output
  
 ## learning process:
 - get 1000 random players and select 1 best player
 - create 100 cloned best players with random changes of random number of places
 - repeat
 

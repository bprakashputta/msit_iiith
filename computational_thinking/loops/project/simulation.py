# Project Description
# We use computers to simulate what might happen in the real world so that we can make informed decisions in all kinds of complicated situations. Suppose a gambler makes a series of fair $1 bets, starting with $50, and continues to play until she breaks or has $250. What are the chances of going home with $250, and how many bets might she expect to make before winning or losing?

# Program this simulation that can help answer these questions. It accepts three arguments, the initial stake ($50), the goal amount ($250), and the number of times we want to simulate the game.
# Modify your program to take an extra argument that specifies the number of bets the gambler is willing to make, so that there are three possible ways for the game to end: the gambler wins, loses, or runs out of time. Add the output to give the expected amount of money the gambler will have when the game ends.

import random

def gambling_simulation(initial_stake, goal_amount, trials):
    bets = 0
    wins = 0

    # Perform the simulation trials number of times.
    for i in range(0, trials):
        # start the gambling simulation
        cash = initial_stake
        # random.seed(5)
        while cash > 0 and cash < goal_amount:
            bets = bets + 1
            if random.random() < 0.5:
                cash = cash + 1
            else:
                cash = cash - 1
        
        if cash == goal_amount:
            wins = wins + 1
    
    # Print Results
    print(100*wins/trials,"% wins")
    print("Avg # bets:", bets)



if __name__ == "__main__":
    initial_stake = int(input("Enter initial stake amount : "))
    goal_amount = int(input("Enter goal amount : "))
    trials = int(input("Enter number of trials : "))
    # random.seed(5)
    # for i in range(0, trials):
    #     print(random.random())
    # start simulation
    gambling_simulation(initial_stake, goal_amount, trials)
import random
import time
from tabulate import tabulate

print("\n\n")

# All outcomes counter indexed by tuple
outcomes = { (0,0): 0, (0,1): 0, (1,0): 0, (1,1): 0, (2,0): 0, (2,1): 0, (3,0): 0, (3,1): 0, (4,0): 0, (4,1): 0, (5,0): 0, (5,1): 0 }

n_sim = int(input("Simulation count: "))

tm_start = time.time()

master_pb = (set(random.sample(range(1, 69), 5)), random.randint(1, 26))

for _ in range(n_sim):
    sim_pb = (set(random.sample(range(1, 69), 5)), random.randint(1, 26))
    outcomes[( len(sim_pb[0].intersection(master_pb[0])), (sim_pb[1] == master_pb[1]) )] += 1
tm_stop = time.time()

# Dummy billion
#n_sim = 1000000000
#outcomes = { (0,0): 959700120, (0,1): 25940982, (1,0): 0, (1,1): 10987310, (2,0): 0, (2,1): 1465228, (3,0): 1803919, (3,1): 72201, (4,0): 28943, (4,1): 1203, (5,0): 90, (5,1): 4 }

print("\n")
print("Results for simulation of " + str(n_sim) + " Powerball entries ($" + str(n_sim*2) + " cost)")
print()

# Return formula = (prize-cost)*probability
print(tabulate(
    [
        ['1', '5 white and red', '$203,200,000', outcomes[(5,True)],    outcomes[(5,True)]/n_sim,    '$'+str(round((203200000-2)*(outcomes[(5,True)]/n_sim), 2))],
        ['2', '5 white', '$1,000,000', outcomes[(5,False)],             outcomes[(5,False)]/n_sim,   '$'+str(round((1000000-2)*(outcomes[(5,False)]/n_sim), 2))],
        ['3', '4 white and red', '$50,000', outcomes[(4,True)],         outcomes[(4,True)]/n_sim,    '$'+str(round((50000-2)*(outcomes[(4,True)]/n_sim), 2))],
        ['4', '4 white', '$100', outcomes[(4,False)],                   outcomes[(4,False)]/n_sim,   '$'+str(round((100-2)*(outcomes[(4,False)]/n_sim), 2))],
        ['5', '3 white and red', '$100', outcomes[(3,True)],            outcomes[(3,True)]/n_sim,    '$'+str(round((100-2)*(outcomes[(3,True)]/n_sim), 2))],
        ['6', '3 white', '$7', outcomes[(3,False)],                     outcomes[(3,False)]/n_sim,   '$'+str(round((7-2)*(outcomes[(3,False)]/n_sim), 2))],
        ['7', '2 white and red', '$7', outcomes[(2,True)],              outcomes[(2,True)]/n_sim,    '$'+str(round((7-2)*(outcomes[(2,True)]/n_sim), 2))],
        ['8', '1 white and red', '$4', outcomes[(1,True)],              outcomes[(1,True)]/n_sim,    '$'+str(round((4-2)*(outcomes[(1,True)]/n_sim), 2))],
        ['9', 'Red', '$4', outcomes[(0,True)],                          outcomes[(0,True)]/n_sim,    '$'+str(round((4-2)*(outcomes[(0,True)]/n_sim), 2))],
        ['', 'Nothing', '$0', outcomes[(0,False)]+outcomes[(1,False)]+outcomes[(2,False)], (outcomes[(0,False)]+outcomes[(1,False)]+outcomes[(2,False)])/n_sim, '$'+str(round(-2* ((outcomes[(0,False)]+outcomes[(1,False)]+outcomes[(2,False)])/n_sim) , 2))]
    ],
    headers=['Division', 'Matching', 'Prize', 'No. Winnings', 'Probability', 'Expected Return per Ticket'],
    tablefmt="orgtbl",
    floatfmt=".10f"
))

print()
print(str(round(tm_stop-tm_start, 2)) + " seconds")

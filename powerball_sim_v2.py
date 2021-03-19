import random
import time

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

print("\n")
print("Results for simulation of " + str(n_sim) + " Powerball entries ($" + str(n_sim*2) + " cost)")
print()
print("No Winnings: " + str(outcomes[(0,False)]+outcomes[(1,False)]+outcomes[(2,False)]))
print("Tier 1 [$4]: " + str(outcomes[(0,True)]))
print("Tier 2 [$4]: " + str(outcomes[(1,True)]))
print("Tier 3 [$7]: " + str(outcomes[(2,True)]))
print("Tier 4 [$7]: " + str(outcomes[(3,False)]))
print("Tier 5 [$100]: " + str(outcomes[(3,True)]))
print("Tier 6 [$100]: " + str(outcomes[(4,False)]))
print("Tier 7 [$50,000]: " + str(outcomes[(4,True)]))
print("Tier 8 [$1,000,000]: " + str(outcomes[(5,False)]))
print("Tier 9 [$JACKPOT]: " + str(outcomes[(5,True)]))
print()
jkpt = ""
if outcomes[(5,True)] > 0:
    jkpt = " + " + str(outcomes[(5,True)]) + " JACKPOT "
winnings = outcomes[(0,True)]*4+outcomes[(1,True)]*4+outcomes[(2,True)]*7+outcomes[(3,False)]*7+outcomes[(3,True)]*100+outcomes[(4,False)]*100+outcomes[(4,True)]*50000+outcomes[(5,False)]*1000000
print("Total winnings: $" + str(winnings) + jkpt)
print()
print("Return per ticket: $"+str(winnings/n_sim))
print()
print(str(round(tm_stop-tm_start, 2)) + " seconds")

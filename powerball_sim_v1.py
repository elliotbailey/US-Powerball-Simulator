import random
import os
import time

os.system('cls')

#################################
#
#           POWERBALL (BASE) NOTES
#
#   - picking 5 white balls from a group of 69
#   - picking 1 red ball (powerball) from a group of 26
#   - rewards exist for each tier (white, PB) - [(0,1) [$4], (1,1) [$4], (2,1) [$7], (3,0) [$7], (3,1) [$100], (4,0) [$100],
#                                               (4,1) [$50,000], (5,0) [$1,000,000], (5,1) [$JACKPOT]]
#   - choose random powerball number, simulate n games and determine how many of each prize are won
#
#################################

def gen_powerball():
    # Generate white balls
    white_balls = []
    for i in range(5):
        x = random.randint(1,69)
        while x in white_balls:
            x = random.randint(1,69)
        white_balls.append(x)
    #white_balls = random.sample(range(1, 69), 5)

    # Generate powerball
    red_ball = random.randint(1, 26)

    powerball = [white_balls, red_ball]
    return powerball

def same_object_count(a, b):
    # Determine how many objects of a are also in b
    n_same = 0
    for i in range(len(a)):
        for x in range(len(b)):
            if a[i] == b[x]:
                n_same += 1
    return n_same

n_sim = int(input("Simulation count: "))

# Measure Time
tm_start = time.time()

master_pb = gen_powerball()

tier0 = 0
n_0_1 = 0 # tier 1
n_1_1 = 0 # tier 2
n_2_1 = 0 # tier 3
n_3_0 = 0 # tier 4
n_3_1 = 0 # tier 5
n_4_0 = 0 # tier 6
n_4_1 = 0 # tier 7
n_5_0 = 0 # tier 8
n_5_1 = 0 # tier 9

for i in range(n_sim):
    sim_pb = gen_powerball()

    # higher tiers take priority
    # tier 9
    if same_object_count(sim_pb[0], master_pb[0]) == 5 and sim_pb[1] == master_pb[1]:
        n_5_1 += 1
    # tier 8
    elif same_object_count(sim_pb[0], master_pb[0]) == 5 and sim_pb[1] != master_pb[1]:
        n_5_0 += 1
    # tier 7
    elif same_object_count(sim_pb[0], master_pb[0]) == 4 and sim_pb[1] == master_pb[1]:
        n_4_1 += 1
    # tier 6
    elif same_object_count(sim_pb[0], master_pb[0]) == 4 and sim_pb[1] != master_pb[1]:
        n_4_0 += 1
    # tier 5
    elif same_object_count(sim_pb[0], master_pb[0]) == 3 and sim_pb[1] == master_pb[1]:
        n_3_1 += 1
    # tier 4
    elif same_object_count(sim_pb[0], master_pb[0]) == 3 and sim_pb[1] != master_pb[1]:
        n_3_0 += 1
    # tier 3
    elif same_object_count(sim_pb[0], master_pb[0]) == 2 and sim_pb[1] == master_pb[1]:
        n_2_1 += 1
    # tier 2
    elif same_object_count(sim_pb[0], master_pb[0]) == 1 and sim_pb[1] == master_pb[1]:
        n_1_1 += 1
    # tier 1
    elif same_object_count(sim_pb[0], master_pb[0]) == 0 and sim_pb[1] == master_pb[1]:
        n_0_1 += 1
    else:
        tier0 += 1

print("\n")
print("Results for simulation of " + str(n_sim) + " Powerball entries ($" + str(n_sim*2) + " cost)")
print("")
print("No Winnings: " + str(tier0))
print("Tier 1 [$4]: " + str(n_0_1))
print("Tier 2 [$4]: " + str(n_1_1))
print("Tier 3 [$7]: " + str(n_2_1))
print("Tier 4 [$7]: " + str(n_3_0))
print("Tier 5 [$100]: " + str(n_3_1))
print("Tier 6 [$100]: " + str(n_4_0))
print("Tier 7 [$50,000]: " + str(n_4_1))
print("Tier 8 [$1,000,000]: " + str(n_5_0))
print("Tier 9 [$JACKPOT]: " + str(n_5_1))
print()
jkpt = ""
if n_5_1 > 0:
    jkpt = " + " + str(n_5_1) + " JACKPOT "
print("Total winnings: $" + str(n_0_1*4+n_1_1*4+n_2_1*7+n_3_0*7+n_3_1*100+n_4_0*100+n_4_1*50000+n_5_0*1000000) + jkpt)

tm_stop = time.time()

print(str(round(tm_stop-tm_start, 2)) + " seconds")

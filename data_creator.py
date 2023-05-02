
import random
import numpy as np
import matplotlib.pyplot as plt
import json
from collections import Counter


# a single summon
def summon(ultra, ll):
    #random number between 0 and 10,000
    summoned = random.randint(0, 10000)
    #the value of ultra will depend on what step we're on
    if (summoned <= ultra):
        return(1,0)
    elif (summoned <= ll):
        return (0,1)
    return (0,0)
# do 10 summons
def multi_summon(ultra, ll):
    ultras = 0
    lls = 0
    for i in range(10):
        cur_summ = summon(ultra, ll)
        ultras += cur_summ[0]
        lls += cur_summ[1]
    return (ultras, lls)
# do an entire rotation
def summon_loop():
    ultras = 0
    lls = 0
    cc = 0
    #so for i in range(4) doesn't go 1, 2, 3,4 it goes 0,1,2,3 which is why the 2x rate step is on step ==1
    for i in range(4):
        if i == 4:
            print("Inconcevible!")
        if i != 3:
            #free summon on every step but the last one
            cc += 1000
        if i == 1:
            cur_summ = multi_summon(70, 50)
        else:
            cur_summ = multi_summon(35, 50)
        lls += cur_summ[1]
        if cur_summ[0] >= 1:
            return (1, lls, cc)
    return (ultras, lls, cc)


#main loop, count of total ultras, lls, and cc

ultras = 0
lls = 0
cc = 0
t_cc = 0
t_ultrs = 0

ultra_counts = []
cc_costs = []

iters = int(input("How many iterations?> "))

t_iters = iters
while (iters != 0):
    summ = summon_loop()
    ultras += summ[0]
    lls += summ[1]
    cc += summ[2]
    if (ultras != 0):
        t_cc += cc
        t_ultrs += ultras
        iters-=1
        ultra_counts.append(ultras)
        cc_costs.append(cc)
        ultras = 0 
        cc = 0
cc = t_cc
ultras = t_ultrs

print("Got " + str(ultras) +" Ultras in " + str(cc) + " cc, for an average rate of " +str(cc/ultras))
print("NumPy med " + str(np.median(cc_costs)) + " max " + str(np.max(cc_costs)) + " min " + str(np.min(cc_costs)))




c=Counter(sorted(cc_costs))
with open('dict.json', 'w') as file:
     file.write(json.dumps(c))
print("If you wanted to add new data, go ahead and uncomment the load data in main.py")

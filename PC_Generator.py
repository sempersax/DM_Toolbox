# This is for creating a player character.
# Much of this will be very similar to an NPC, but
# now there is a need for stats.
import numpy as np
import time

def statRoller():
    start = time.time()
   # Create 6 spots for stats
    stats = np.zeros(6)
    # Roll 4d6 six times to get stats
    stats = np.asarray([np.random.randint(0,high=7,size=4) for _ in range(len(stats))])
    # S
    stats = np.sort(stats, axis = 1)
    # Eliminate the lowest value from each roll
    stats = stats[:,1:]
    # Sum the rolls
    stats = np.sum(stats, axis = 1)
    # Sort from low to high
    stats = np.sort(stats, axis = 0)
    print('stat roll time = ',time.time()-start)
    return(stats)

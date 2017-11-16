import matplotlib.pyplot as plt
from random import sample
from time import perf_counter
import Sorts
rnglist = sample(range(20000), k=20000)

def clock(algorithm, rnglistthing):
    start = perf_counter()
    algorithm(rnglistthing)
    end = perf_counter()
    time_elapsed = end - start
    return time_elapsed
y = []
for n in range (1000, 20000, 1000):
    y.append(n)
x =[]
for n in range (1000, 20000, 1000):
    x.append(clock(Sorts.quicksort, rnglist[0:n]))
z =[]
for n in range (1000, 20000, 1000):
    z.append(clock(Sorts.merge_sort, rnglist[0:n])) 
b =[]
for n in range (1000, 20000, 1000):
    b.append(clock(Sorts.bubble_sort, rnglist[0:n])) 
v =[]
for n in range (1000, 20000, 1000):
    v.append(clock(Sorts.insertion_sort, rnglist[0:n]))
k =[]
for n in range (1000, 20000, 1000):
    k.append(clock(Sorts.selection_sort, rnglist[0:n]))
    



plt.plot (x, y, marker="*", color="purple", label="Quicksort")


#Labels axises
plt.xlabel("Time")
plt.ylabel("Items")
plt.title("Sorting Algorithms")
plt.legend()

plt.show()
import matplotlib.pyplot as plt
from random import sample
from time import perf_counter
from Sorts import quicksort, merge_sort, bubble_sort, insertion_sort, selection_sort


def clock(algorithm, rnglistthing):
    start = perf_counter()
    algorithm(rnglistthing)
    end = perf_counter()
    time_elapsed = end - start
    return time_elapsed

y = []
q = []
m = []
b = []
i = []
s = []
for n in range (1000, 20001, 1000):
    y.append(n)
    rnglist = sample(range(n), n)
    
    q.append(clock(quicksort, rnglist.copy()))
    m.append(clock(merge_sort, rnglist.copy())) 
    b.append(clock(bubble_sort, rnglist.copy())) 
    i.append(clock(insertion_sort, rnglist.copy()))
    s.append(clock(selection_sort, rnglist.copy()))


plt.plot (q, y, marker="*", color="purple", label="Quicksort")
plt.plot (m, y, marker="^", color="blue", label="Merge sort")
plt.plot (b, y, marker="s", color="red", label="Bubble sort")
plt.plot (i, y, marker="D", color="yellow", label="Insertion sort")
plt.plot (s, y, marker="|", color="green", label="Selection sort")


#Labels axises
plt.xlabel("Time")
plt.ylabel("Items")
plt.title("Sorting Algorithms")
plt.legend()

plt.show()
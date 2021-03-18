import matplotlib.pyplot as plt
import time


# Your code to test time complexity

def time_complexity_in(e, my_list):
    if x - 1 in my_list:
        a = True


times = []
my_list1 = range(1, 90001, 100)
for x in my_list1:
    my_list = set(range(0, x))
    start_time = time.time()
    time_complexity_in(x - 1, my_list)  # Call to the code for which time complexity is being calculated.
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

plt.xlabel("No. of elements")
plt.ylabel("Time required")
plt.plot(my_list1, times)
plt.show()

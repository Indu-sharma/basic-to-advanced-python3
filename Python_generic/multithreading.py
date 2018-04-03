import threading
import random
import multiprocessing
import subprocess
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print("Taken by function {} is {}".format(func.__name__, t2-t1))
    return wrapper
# Parallelism with Multithreading

@time_it
def executor(count,id):
    out_list = []
    for i in range(1,count):
        out_list.append(random.randint(1,100))
    print len(out_list), id, count


def parallelize(threads):
    size = 1000000 / threads
    myjobs = []
    for id in range(0,threads):
        thread = threading.Thread(target=executor(size,id))
        myjobs.append(thread)

    for job in myjobs:
        job.start()
    for job in myjobs:
        job.join()
    print("List Processing Completed By Threading")


#parallelize(1)

# Parallelism with Multiprocessing

def  parallelize_(threads, func):
    size = 10000000 / threads
    myjobs = []
    for id in range(0,threads):
        thread = multiprocessing.Process(target=eval(func)(size,id))
        myjobs.append(thread)
    for job in myjobs:
        job.start()
    for job in myjobs:
        job.join()
    print("List Processing Completed By MultiProcessing")


parallelize_(2, "executor")

def os_subprocess():
    (output,status) = subprocess.Popen("cat test.txt",shell=True, stdout=subprocess.PIPE).communicate()
    print(output)

#os_subprocess()

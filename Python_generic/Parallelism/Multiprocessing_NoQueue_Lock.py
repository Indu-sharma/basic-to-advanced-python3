import multiprocessing
import time


def increment(final, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        final.value = final.value + 1
        lock.release()

def decrement(final, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        final.value = final.value - 1
        lock.release()

if __name__ == '__main':
    ''' While Working with Shared memory by multiple processes the results could be inconsistent
      .So We use Mutex flavour of Unix Operating system in Python i.e Lock before operating on shared memory and 
      release the lock after working on shared memory variable'''

    final = multiprocessing.Value('i',500)
    lock = multiprocessing.Lock()
    decr = multiprocessing.Process(target=decrement, args=(final,lock,))
    incr = multiprocessing.Process(target=increment, args=(final, lock,))
    decr.start()
    incr.start()
    decr.join()
    incr.join()
    print("Final Value After Increment, Decrement in Shared Variable is:{}", final.value)

import multiprocessing
import time

def usingmap_pool(mylist):
    mysum = 0
    for i in mylist:
        mysum = mysum + reduce(lambda x,y : x+y,range(1000))

    return mysum



if __name__=='__main__':
    p = multiprocessing.Pool(processes = 100)
    result = p.map(usingmap_pool, range(1,100), chunksize=1)
    p.start()
    p.close()
    p.join()

    print(result)

import multiprocessing


def calculate_area(params, pi):

    for index, redius in enumerate(params):
        q.put(pi * redius * redius)


if __name__ == '__main__':
    ''' If we make the result global and create process to invoke method, the result will not avialble to Main program
    as the Child process uses seprate memory. So to resolve it, we use Queue of multiprocessing which is different from python 
    module queue.Queue()(Its used to share the data between threads)'''

    redii = [1, 2, 3, 5]
    q = multiprocessing.Queue()
    pi = 3.14
    p = multiprocessing.Process(target=calculate_area, args=(redii, q, pi))
    p.start()
    p.join()
    result = []
    while q.empty() is False:
        result.append(q.get())

    print("Area of the List {} is {} with pi value {}".format(redii, result, pi))

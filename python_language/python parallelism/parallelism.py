import requests
import threading
import time
import logging

results = []

logging.basicConfig(level='INFO', filename="Threading.log", filemode='w')
logger = logging.getLogger()


def testing_thread_io(urls):
    # print("Currently Running Thread is :{}".format(threading.current_thread().getName()))
    for url in urls:
        try:
            response = requests.get("http://" + url.strip(), timeout=3.01)
        except:
            continue
        redirect = response.url
        try:
            server = response.headers['Server']
        except:
            server = 'NA'
        try:
            status = response.history[-1].status_code
        except:
            status = response.status_code
        # print("Thread:{}, value:{}".format(threading.current_thread().getName(), res))
        results.append('___'.join(map(str, [url, redirect, server, status])))


def testing_thread_non_io(urls):
    for url in urls:
        results.append([[1] * len(url)] * 100000)


def using_threads(fnc, num_threads):
    FL = open("sample_data/infected_sites.txt")
    lines = filter(lambda x: x.strip().strip('\n'), FL.readlines())
    lines = map(lambda x: x.strip('\n'), lines)[0:1000]
    global results
    results = []
    t1 = time.time()
    chunk = len(lines) / num_threads
    threads = [threading.Thread(target=eval(fnc), name="thread-" + str(i), args=(lines[i:i + chunk],)) for i in
               range(0, len(lines), chunk)]
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    t2 = time.time()
    logger.info("Method: {} Took {} with {} threads for Urls={}".format(eval(fnc).__name__, t2 - t1, len(threads),
                                                                        len(results)))


[using_threads('testing_thread_non_io', i) for i in range(1, 26, 5)]
[using_threads('testing_thread_io', i) for i in range(1, 26, 5)]


'''
Threading peroformance comparisons: 

INFO:root:Method: testing_thread_non_io Took 0.0404798984528 with 1 threads for Urls=50
INFO:root:Method: testing_thread_non_io Took 0.0290548801422 with 7 threads for Urls=50
INFO:root:Method: testing_thread_non_io Took 0.0296058654785 with 13 threads for Urls=50
INFO:root:Method: testing_thread_non_io Took 0.0292890071869 with 17 threads for Urls=50
INFO:root:Method: testing_thread_non_io Took 0.0309588909149 with 25 threads for Urls=50
INFO:root:Method: testing_thread_io Took 67.6745920181 with 1 threads for Urls=42
INFO:root:Method: testing_thread_io Took 35.2092139721 with 7 threads for Urls=42
INFO:root:Method: testing_thread_io Took 9.6608710289 with 13 threads for Urls=44
INFO:root:Method: testing_thread_io Took 4.92318415642 with 17 threads for Urls=44
INFO:root:Method: testing_thread_io Took 8.74089694023 with 25 threads for Urls=43
'''


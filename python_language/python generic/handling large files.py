import multiprocessing as mp

""" 
Handling Large Files in Python with Generator & with context. 
"""


def read_file(fp):
    while True:
        _line = fp.readline()
        if not _line:
            break
        yield _line


def process_line(my_line, FO):
    my_array = my_line.strip('\n').split(',')
    if len(my_array) < 4:
        print(f"Invalid Line Detected {my_line}")
        return
    if int(my_array[-1]) < 1987:
        print(my_array)
        my_array[1] = 2 * int(my_array[1])
        my_array = map(lambda x: str(x), my_array)
        out_line = ','.join(my_array)
        FO.write(out_line + '\n')
    return


with open('test') as FH, open('test_out.txt', 'w') as FO:
    lines = read_file(FH)
    for line in lines:
        process_line(line, FO)

""" 
Handling Large Files in Python with Multi Processing & with context. 

"""


def worker_process(fbytes):
    with open('test') as FH, open('test_out.txt', 'a') as FO:
        FH.seek(fbytes)
        line = FH.readline()
        process_line(line, FO)


cores = 4  # You may give process = Number of Cores in your machine.
my_pools = mp.Pool(cores)
jobs = []
with open('test', 'rb') as FH:
    fbytes = FH.tell()
    for line in FH:
        jobs.append(my_pools.apply_async(worker_process, (fbytes,)))
        fbytes = FH.tell()

for job in jobs:
    job.get()
my_pools.close()


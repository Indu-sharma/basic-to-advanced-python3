import time
import logging


def time_it(func):
    """
    Simple Decorator for generic Run Time Logger across all the functions.
    :param func:
    :return:
    """
    logging.info("")
    my_logger = logging.getLogger()
    def timecalculator(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        msg = "Function '{}' took {}".format(func.__name__, t2 - t1)
        my_logger.error(msg)
        return result

    return timecalculator


@time_it
def _cube(nums):
    mylist = [x * x * x for x in nums]
    return mylist


@time_it
def _square(nums):
    mylist = [x * x for x in nums]
    return mylist


nums = xrange(1, 200000)
print(len(_cube(nums)))

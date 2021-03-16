def mycoroutine():
    v_count = 0
    inv_count = 0
    try:
        while True:
            myinput = yield
            if isinstance(myinput, int):
                v_count = v_count + 1
            else:
                inv_count = inv_count + 1
    except GeneratorExit:
        print("You Sent {} valid digits and {} invalid chars:".format(v_count, inv_count))


mygen = mycoroutine()

next(mygen)

for i in range(10):
    mygen.send(i)

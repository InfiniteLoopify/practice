import logging
import threading
import time

var = 0
mylock = threading.Lock()


def thread_function(name):
    logging.info("Thread %s: starting", name)
    global var
    with mylock:
        var = int(str(var)) + 1
    print(var)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        print(var)
        thread.join()
        logging.info("Main    : thread %d done", index)

from time import sleep
import numpy as np


def random_wait():
    wait_time = 4 * np.random.randn() + 20
    if wait_time < 10:
        wait_time += 10
    sleep(wait_time)

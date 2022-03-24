import random
from tabnanny import check
from tokenize import single_quoted

from typing import Tuple


p = 0.1
m = 9

def SingleSim(gachaLen: int, sep: int=10) -> Tuple[int, int, float]:
    checker = 0
    rare_num = 0
    comm_num = 0
    for i in range(gachaLen):
        if i > 0 and i % sep == 0:
            print(
                f"At %.3d times:\t" % i,
                f"Pick rare={rare_num}\tAvgProbability={rare_num/i}"
            )
        if checker == m:
            # hit the `must rare` mechanism
            rare_num += 1
            checker = 0
            continue
        if random.random() <= p:
            # if get rare, reset the checker
            rare_num += 1
            checker = 0
        else:
            comm_num += 1
            checker += 1
    
    return (rare_num, comm_num, rare_num / gachaLen)


if __name__ == "__main__":
    SingleSim(10000, 1000)


    nbar = sum([l * p * (1-p) ** (l-1) for l in range(1, m+1)]) + (m+1) * (1-p) ** m
    print()
    print(
        f"Theoretical pbar={1 / nbar}"
    )

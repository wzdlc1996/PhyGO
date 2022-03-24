from random import random
from typing import Tuple

pab = 0.0
pa = 0.1
pb = 0.5
p0 = 1 - pab - pa - pb


def RaidOutput() -> Tuple[int, int]:
    res = random()
    if res < pab:
        return (1, 1)
    elif res < pab + pa:
        return (1, 0)
    elif res < pab + pa + pb:
        return (0, 1)
    return (0, 0)



def Sim(raidLen: int, sep: int=10):
    reach_goal = 0  # store the number complete
    cumu_a = 0  # cumulate a number
    cumu_b = 0  # cumulate b number
    ia = 0  # identify get a
    ib = 0  # identify get b
    for i in range(raidLen):
        ta, tb = RaidOutput()
        ia += ta
        ib += tb
        cumu_a += ta
        cumu_b += tb
        if ia > 0 and ib > 0:
            reach_goal += 1
            ia = ib = 0
        
        if i > 0 and i % sep == 0:
            print(
                f"At %.3d:\t" % i,
                f"Reached={reach_goal}\tAvgProb={reach_goal / i}"
            )


if __name__ == "__main__":
    Sim(10000, 1000)

    nbar = 1 / (pab + pa) + 1 / (pab + pb) - 1 / (1-p0)
    print()
    print(
        f"Theoretical pbar={1 / nbar}"
    )


import random

N = 10

def sim() -> int:
    found = [0] * N
    t = 0
    while min(found) == 0:
        found[random.randint(0, N-1)] += 1
        t += 1
    return t


def calc_theoretical() -> float:
    t = 0.
    for k in range(N):
        t += N / (N - k)
    return t


if __name__ == "__main__":
    t_ref = calc_theoretical()
    n_samp = 10000
    sum_t = 0
    for _ in range(n_samp):
        sum_t += sim()
    mean_t = sum_t / n_samp
    print(f"Theoretical: {t_ref}\tExperimental: {mean_t}")

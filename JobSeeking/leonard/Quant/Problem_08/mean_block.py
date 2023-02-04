import random

n = 26
m = 10

n_sample = 1000
tot_number = 0

for _ in range(n_sample):
    str_list = random.sample([0]*n + [1]*m, k=m+n)
    n_block = 1
    for k in range(m+n-1):
        if str_list[k+1] != str_list[k]:
            n_block += 1
    tot_number += n_block

print(f"The mean number of block is:\t{tot_number / n_sample}")
print(f"The theoretical value is:\t{1 + 2*m*n/(m+n)}")


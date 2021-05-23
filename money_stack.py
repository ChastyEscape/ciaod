import random
import time


def coins(piles):
    piles.sort()
    sum = 0
    while len(piles) > 0:
        piles = piles[1:len(piles)-1]
        sum += piles[len(piles)-1]
        piles = piles[:len(piles)-1]
    return sum



random_list = []
for i in range(501):
    random_list.append(random.randint(1, 1000))

print (random_list)

start_loop = time.time()
print(coins(random_list))
end_loop = time.time()
print('loop', end_loop-start_loop)
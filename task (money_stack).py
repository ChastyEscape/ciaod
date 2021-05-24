import random
import time


"""
    Тимонин БФИ1901
    «Стопки Монет»:
        На столе стоят 3n стопок монет. Вы и ваши друзья Алиса и Боб забираете стопки монет по
    следующему алгоритму:
        1. Вы выбираете 3 стопки монет из оставшихся на столе.
        2. Алиса забирает себе стопку с максимальным количеством монет.
        3. Вы забираете одну из двух оставшихся стопок.
        4. Боб забирает последнюю стопку.
        5. Если еще остались стопки, то действия повторяются с первого шага.

        Дан массив целых положительных чисел piles. Напишите функцию, 
    возвращающую максимальное число монет, которое вы можете получить.
"""


def coins(piles):
    piles.sort()
    sum = 0
    while len(piles) > 0:
        piles = piles[1:len(piles)-1]
        sum += piles[len(piles)-1]
        piles = piles[:len(piles)-1]
    return sum


if __name__ == "__main__":
    random_list = []
    for i in range(501):
        random_list.append(random.randint(1, 1000))

    print (random_list)

    start_loop = time.time()
    print(coins(random_list))
    end_loop = time.time()
    print('loop', end_loop-start_loop)

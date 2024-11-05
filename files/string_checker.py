from typing import Generator
from collections import defaultdict

def input_gen(number: int) -> Generator:
    yield from [input() for _ in range(number)]

def get_input_from_gen(words_generator: Generator) -> dict:
    container = defaultdict(list)
    index_counter = 1
    while True:
        try:
            container[index_counter] = next(words_generator)
            index_counter += 1
        except StopIteration:
            return container

n, m = map(int, input().split())
A_dict = get_input_from_gen(input_gen(n))
B_dict = get_input_from_gen(input_gen(m))

good_indexes = defaultdict(list)
for k_B in B_dict.keys():
    if B_dict[k_B] not in A_dict.values():
        good_indexes[B_dict[k_B]] += [-1]
    
    for k_A in A_dict.keys():
        if B_dict[k_B] == A_dict[k_A]:
            good_indexes[B_dict[k_B]].append(k_A)

for k, v in good_indexes.items():
    print(*v, sep= ' ', end='\n')
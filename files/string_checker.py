from typing import Generator
from collections import defaultdict

def input_gen(number: int) -> Generator:
     for _ in range(number):
         yield input()

def get_input_from_gen_for(words_generator: Generator) -> dict:
    container = defaultdict(list)
    for index_counter, word in enumerate(words_generator, start=1):
        container[index_counter] = word
    return container

n, m = map(int, input().split())
A_dict = get_input_from_gen_for(input_gen(n))
B_dict = get_input_from_gen_for(input_gen(m))

value_to_indices = defaultdict(list)
for k_A, v_A in A_dict.items():
    value_to_indices[v_A].append(k_A)

good_indexes = defaultdict(list)
for k_B, v_B in B_dict.items():
    if v_B not in value_to_indices:
        good_indexes[v_B].append(-1)
    else:
        good_indexes[v_B].extend(value_to_indices[v_B])

for v in good_indexes.values():
    print(*v, sep= ' ', end='\n')
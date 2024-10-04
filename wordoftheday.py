from itertools import product
from string import ascii_lowercase as letters
from operator import ne, lt

num_letters = int(input("Number of letters: "))

letters_in_place_input = input("Correct letters in correct position. Start counting from one input ecpected like a1 b2: ").split(' ')
letters_out_of_place_input = input("Correct letters that are NOT in correct place Start counting from one input ecpected like a1 b2: ").split()
marked_wrong = input("Letters marked as wrong: ")
required_letters = []
letters_in_place = {}
letters_out_of_place = {}
possible_words = []

for lip in letters_in_place_input:
    if lip !='':
        letter, position = lip[0], lip[1:]
        letters_in_place[int(lip[1:])] = lip[0]
        required_letters.append(letter)

for lop in letters_out_of_place_input:
    if lop !='':
        letter, position = lop[0], int(lop[1:])
        letters_out_of_place[position] = letters_out_of_place.get(position, [lop[0]])
        required_letters.append(letter)

excluded_letters = [l for l in marked_wrong if l not in required_letters]
possible_letters = [l for l in letters if l not in marked_wrong or l in required_letters]

for g in product(*[possible_letters]*num_letters):
    possible = True
    # check letters in place
    for i in range(1, num_letters+1):
        if (i in letters_in_place and letters_in_place[i] != g[i-1]) or (i in letters_out_of_place and g[i-1] in letters_out_of_place[i]):
            possible = False
            break

    if not(possible):
        continue
    # check at least amount of times in correct
    for l in required_letters:
        op = ne if l in marked_wrong else lt
        if op(g.count(l), required_letters.count(l)):
            possible = False
            break
    if possible:
        possible_words.append("".join(g))


print(possible_words)
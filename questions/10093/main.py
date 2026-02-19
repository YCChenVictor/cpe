import sys
import string

lines = sys.stdin.read().splitlines()

base = string.digits + string.ascii_uppercase + string.ascii_lowercase
chars = list(base)

dict = {}
for i in range(0, len(chars)):
    dict[chars[i]] = i

for line in lines:
    elements = list(line)
    largest_number_index = 0
    clean_number = ''
    element_sum = 0
    for element in elements:
        if not dict.get(element):
            continue
        if dict[element] > largest_number_index:
            largest_number_index = dict[element]
        clean_number += element
        element_sum += dict[element]
    first_base_guess = largest_number_index + 1
    
    base_guess = first_base_guess
    while base_guess <= 62:
        if element_sum == 0:
            base_guess = 2
            break
        if element_sum % (base_guess - 1) == 0:
            break
        base_guess += 1
    
    if base_guess > 62:
        print("such number is impossible!")
    else:
        print(base_guess) 

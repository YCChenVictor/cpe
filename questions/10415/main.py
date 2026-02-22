import sys

lines = sys.stdin.read().splitlines()

num_of_melodies = int(lines[0])

finger_presses = [0 for x in range(0, 10)]
c_finger_presses = [1 if 1 <= i <= 3 or 6 <= i <= 9 else 0 for i in range(0, len(finger_presses))]
d_finger_presses = [1 if 1 <= i <= 3 or 6 <= i <= 8 else 0 for i in range(0, len(finger_presses))]
e_finger_presses = [1 if 1 <= i <= 3 or 6 <= i <= 7 else 0 for i in range(0, len(finger_presses))]
f_finger_presses = [1 if 1 <= i <= 3 or 6 <= i <= 6 else 0 for i in range(0, len(finger_presses))]
g_finger_presses = [1 if 1 <= i <= 3 else 0 for i in range(0, len(finger_presses))]
a_finger_presses = [1 if 1 <= i <= 2 else 0 for i in range(0, len(finger_presses))]
b_finger_presses = [1 if 1 <= i <= 1 else 0 for i in range(0, len(finger_presses))]
C_finger_presses = [1 if 2 <= i <= 2 else 0 for i in range(0, len(finger_presses))]
D_finger_presses = [1 if 0 <= i <= 3 or 6 <= i <= 8 else 0 for i in range(0, len(finger_presses))]
E_finger_presses = [1 if 0 <= i <= 3 or 6 <= i <= 7 else 0 for i in range(0, len(finger_presses))]
F_finger_presses = [1 if 0 <= i <= 3 or 6 <= i <= 6 else 0 for i in range(0, len(finger_presses))]
G_finger_presses = [1 if 0 <= i <= 3 else 0 for i in range(0, len(finger_presses))]
A_finger_presses = [1 if 0 <= i <= 2 else 0 for i in range(0, len(finger_presses))]
B_finger_presses = [1 if 0 <= i <= 1 else 0 for i in range(0, len(finger_presses))]

mapping = {
    'c': c_finger_presses,
    'd': d_finger_presses,
    'e': e_finger_presses,
    'f': f_finger_presses,
    'g': g_finger_presses,
    'a': a_finger_presses,
    'b': b_finger_presses,
    'C': C_finger_presses,
    'D': D_finger_presses,
    'E': E_finger_presses,
    'F': F_finger_presses,
    'G': G_finger_presses,
    'A': A_finger_presses,
    'B': B_finger_presses
}

for i in range(1, num_of_melodies + 1):
    presses = [0 for x in range(0, 10)]
    current = [0 for x in range(0, 10)]
    notes = list(lines[i])
    for j in range(0, len(notes)):
        next_move = mapping[notes[j]]
        for k in range(0, len(next_move)):
            if(next_move[k] == 1 and current[k] == 0):
                presses[k] += 1
        current = next_move

    print(" ".join(map(str, presses)))

import pulp
from collections import defaultdict
import numpy as np

# Read answers and valid inputs from their respective files.
with open('answers.txt') as answers_file:
    answers = [line.strip()[:5] for line in answers_file if line.strip()]

with open('inputs.txt') as inputs_file:
    valid_inputs = [line.strip()[:5] for line in inputs_file if line.strip()]

# Extract unique letters for each position from answers.
letters_at_positions = [set() for _ in range(5)]
for answer in answers:
    for pos, letter in enumerate(answer):
        letters_at_positions[pos].add(letter)

# Create a binary decision variable for each valid input.
# x[i] = 1 if the word from valid_inputs i is chosen, else 0
x = pulp.LpVariable.dicts("word", range(len(valid_inputs)), cat="Binary")

# Create an ILP problem
prob = pulp.LpProblem("OptimizedCoverageProblem", pulp.LpMinimize)

# Objective function: Minimize the number of words chosen
prob += pulp.lpSum(x[i] for i in range(len(valid_inputs)))

# Constraints: For each position and each letter from answers, at least one valid input should have that letter in that position
for pos in range(5):
    for letter in letters_at_positions[pos]:
        prob += pulp.lpSum(x[i] for i, word in enumerate(valid_inputs) if word[pos] == letter) >= 1

# Solve the ILP
prob.solve()

# Extract the chosen words
chosen_words = [valid_inputs[i] for i in range(len(valid_inputs)) if x[i].value() == 1.0]

# Create a frequency map for letters at each position across all answers.
frequency_maps = [defaultdict(int) for _ in range(5)]
for answer in answers:
    for pos, letter in enumerate(answer):
        frequency_maps[pos][letter] += 1

# Rank the chosen words based on the sum of their letter frequencies for each position.
def rank_key(word):
    return min(frequency_maps[pos][letter] for pos, letter in enumerate(word))

ranked_chosen_words = sorted(chosen_words, key=rank_key, reverse=True)

print(ranked_chosen_words)
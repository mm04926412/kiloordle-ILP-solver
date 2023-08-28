# kiloordle-ILP-solver

A solver for kilordle that does the following

Find the sets of letters that appear in each column in the valid answers

Uses integer linear programming to find the smallest subset of the valid inputs that covers the set of letters that appear in each column in the valid answers

sort the solution such that the least likely to appear letters in each column are tested last, this lets us win faster if uncommon letter positions are not in the 1000 words today

Note: Code was generated using GPT-4 by guiding it with the steps I wanted to take, mostly to see if I could use GPT-4 to solve a practical problem / interface with a library I hadn't usef b efore, if something in the code seems strange blame GPT-4.

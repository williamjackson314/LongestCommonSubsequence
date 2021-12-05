# Notes
- Written using Python 3.7
- Function descriptions also found in Docstrings in each function

# Requirements
- Libraries: None
- Files: to compare strings from file the file must be a txt file with the two strings as the first two lines of the file. File must be in the same
folder as main.py

# Longest Common Subsequence

**lcs_length**
- This function finds both the longest common subsequence for each section of two strings and the length of the
longest common subsequence of both strings in their entirety.

Longest Common Subsequence Length
- 20

Longest Common Subsequence
- GTCGTCGGAAGCCGGCCGAA

**print_lcs**
- In order for this function to work, the lcs_length (above) must be called first, with the two strings that the lcs is being printed
from as arguments.
- This function prints the longest common subsequence between two strings, ending at character 'i' for the first and character 'j' for the second 
(i and j are function parameters).

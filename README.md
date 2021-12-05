# Notes
- Written using Python 3.7
- Function descriptions also found in the Docstring of each function

# Requirements
- Libraries: None
- Files: to compare strings from file the file must be a .txt file with the two strings as the first two lines of the file. File must be in the same
folder as main.py. This is shown in the "dna.txt" example file provided.

# Longest Common Subsequence

**lcs_length**
- This function finds both the longest common subsequence for every part of two strings and the length of the
longest common subsequence of both strings in their entirety.

**print_lcs**
- In order for this function to work, the lcs_length(above) must be called first, with the two strings that the lcs is being printed
from as arguments.
- This function prints the longest common subsequence between two strings, ending at character 'i' for the first and character 'j' for the second 
(i and j are function parameters).

# Example Output
For the "dna.txt" example file provided, the output is as follows:

LCS Length = 20

LCS = GTCGTCGGAAGCCGGCCGAA

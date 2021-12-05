def read_file(filename):
    """

    Parameters
    ----------
    filename : string
        The name of the file to read from.

    Returns
    -------
    lines : list
        List of lines from the file.

    """

    f = open(filename, "r")
    lines = f.readlines()
    lines = [x.rstrip('\n') for x in lines]

    return lines

def lcs_length(x, y):
    """

    Parameters
    ----------
    x : string
        String to find subsequence relative to.

    y : string
        String to find subsequence relative to.

    Returns
    -------
    c : matrix holding lcs lengths

    b : matrix holding indicator characters to reconstruct the lcs with later

    lcs_len : the length of the longest common subsequence

    """

    # holds the length of lcs
    len_lcs = 0

    # number of rows in matrix c (minus padding) and b
    m = len(x)

    # number of columns in matrix c (minus padding) and b
    n = len(y)

    c = [[0] * (n + 1) for i in range(m + 1)]
    b = [[None] * (n) for i in range(m)]

    for i in range(m):
        for j in range(n):

            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '\\' # '\' ignoring the escape character
                if (c[i][j] > len_lcs):
                    len_lcs = c[i][j]

            # Notice: when a tie occurs, the algorithm chooses the cell above the current one to reference
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '|'

            else: # c[i][j - 1] > c[i - 1][j]
                c[i][j] = c[i][j - 1]
                b[i][j] = '_'

    return c, b, len_lcs

def print_lcs(b, x, i, j):
    """

    Parameters
    ----------
    b : matrix (2-D list)
        Holds indicator characters used to print the lcs.

    x : string
        string to print lcs from.

    i : int
        Starting row in b matrix.

    j : int
        Starting column in b matrix.

    Returns
    -------
    None.

    """
    if (i < 0) or (j < 0):
        return

    if (b[i][j] == '\\'):
        print_lcs(b, x, i - 1, j - 1)
        print(x[i], end='')

    elif (b[i][j] == '|'):
        print_lcs(b, x, i - 1, j)

    elif (b[i][j] == '_'):
        print_lcs(b, x, i, j - 1)

def main():

    # Read in lines from text file
    strings = read_file("dna.txt")

    # store first two lines as strings to find lcs of
    x = strings[0]
    y = strings[1]

    # Find lcs and lcs length
    c, b, length = lcs_length(x, y)

    # print the length of the lcs
    print("LCS Length = " + str(length))

    # print the lcs between two strings from file
    print("LCS = ", end='')
    print_lcs(b, x, len(x) - 1, len(y) - 1)

main()
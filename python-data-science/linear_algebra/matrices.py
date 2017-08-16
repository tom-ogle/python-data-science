

def shape(A):
    """The number of rows and columns, returned as a pair"""
    num_rows = len(A)
    num_columns = len(A[0]) if A else 0
    return num_rows, num_columns


def get_row(A, i):
    """Get the vector representing the ith row"""
    return A[i]


def get_column(A, i):
    """Get the vector representing the ith row"""
    return [r[i] for r in A]


def make_matrix(num_rows, num_cols, entry_func):
    """Create a num_rows x num_cols matrix.
    entry_func(i, j) specifies the entry at (i, j)."""
    matrix = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append(entry_func(i, j))
        matrix.append(row)
    return matrix


def indentity_matrix(num_rows, num_cols):
    def diagonal_is_1(i, j):
        return 1 if i == j else 0

    return make_matrix(num_rows, num_cols, diagonal_is_1)

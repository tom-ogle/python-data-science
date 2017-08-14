

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

def create_augmented_matrix(A, b):
    """
    Create augmented matrix [A|b] from coefficient matrix A and vector b
    Handles any matrix dimensions automatically
    """
    n = len(b)  # Number of equations (rows)
    augmented = []
    for i in range(n):
        row = []
        for j in range(len(A[i])): # Copies all coefficients from matrix A
            row.append(A[i][j]) #Adds it to new row
        row.append(b[i]) # Adds the constant term from vector b
        augmented.append(row)
    return augmented

def swap_rows(matrix, row1, row2):
    """Swaps two rows in a matrix"""
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def partial_pivoting(aug, pivot_col, tol=1e-12):
    # For convenience and numerical stability we will implement partial pivoting.
    # Partial pivoting is to swap first row with the row with the pivot which has maximum absolute value.
    aug_rows = len(aug)
    current_pivot_row = pivot_col
    max_row = current_pivot_row
    for row_below in range(current_pivot_row + 1, aug_rows):
        if abs(aug[row_below][pivot_col]) > abs(aug[max_row][pivot_col]):
            max_row = row_below

    if max_row != current_pivot_row:
        swap_rows(aug, current_pivot_row, max_row)
    return aug

def forward_elimination(aug, tol=1e-12):
    # We need to use forward elimination algorithm to transform augmented matrice to row echelon form(ref)
    aug_rows = len(aug)
    aug_cols = len(aug[0]) - 1
    for pivot_col in range(aug_cols):
        aug = partial_pivoting(aug, pivot_col, tol)
        if abs(aug[pivot_col][pivot_col]) < tol:
            continue

        pivot_val = aug[pivot_col][pivot_col]
        for row_below in range(pivot_col + 1, aug_rows):
            factor = aug[row_below][pivot_col] / pivot_val
            for j in range(pivot_col, aug_cols + 1):
                aug[row_below][j] -= factor * aug[pivot_col][j] # it will make zero every row element below pivot
    return aug


def check_consistency(aug, tol=1e-12):
    """
    Check if system is consistent after forward elimination
    Returns: 'unique', 'no_solution', or 'infinite_solutions'
    """
    total_rows = len(aug)
    total_variables = len(aug[0]) - 1  # Number of variables

    has_infinite = False  # Track if we found any free variable rows

    for current_row in range(total_rows):
        # Check if left side (coefficients) is all zeros
        left_side_all_zeros = True
        for current_col in range(total_variables):
            if abs(aug[current_row][current_col]) > tol:
                left_side_all_zeros = False
                break

        if left_side_all_zeros:
            # Check the right side (b-value)
            b_value = aug[current_row][total_variables]
            if abs(b_value) > tol:
                return 'no_solution'
            else:
                has_infinite = True
    if has_infinite:
        return 'infinite_solutions'
    else:
        return 'unique'


def back_substitution(aug, tol=1e-12):
    total_rows = len(aug)
    total_variables = len(aug[0]) - 1
    x = [0.0] * total_variables

    for current_row in range(total_rows - 1, -1, -1):
        x[current_row] = aug[current_row][total_variables]
        for known_col in range(current_row + 1, total_variables):
            x[current_row] -= aug[current_row][known_col] * x[known_col]
        if abs(aug[current_row][current_row]) > tol:
            x[current_row] /= aug[current_row][current_row]
        else:
            x[current_row] = 0.0  # Or handle appropriately
    return x


def gaussian_elimination(A, b, tol=1e-12):
    """
        Solve Ax = b using Gaussian elimination with partial pivoting.
        Returns:
            - list: solution vector x if unique solution exists
            - str: 'No solution' if inconsistent
            - str: 'Infinite solutions' if system has free variables
    """
    aug = create_augmented_matrix(A, b)

    aug = forward_elimination(aug, tol)

    consistency = check_consistency(aug, tol)
    if consistency == 'no_solution': # Basically both of them is singular matrix so in numpy they will be same output
        return "No solution"
    elif consistency == 'infinite_solutions':
        return "Infinite solutions"

    return back_substitution(aug, tol)







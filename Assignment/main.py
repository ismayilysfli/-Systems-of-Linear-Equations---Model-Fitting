from gaussian_elimination_func import gaussian_elimination
import numpy as np

n = int(input("Enter matrix size (n for n x n): "))

print(f"Enter {n}x{n} matrix A (one row per line, numbers separated by spaces):")
A = []
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print(f"Enter vector b ({n} numbers separated by spaces):")
b = list(map(float, input().split()))

my_solution = gaussian_elimination(A, b)
print("\nMy solution:", my_solution)

np_A = np.array(A)
np_b = np.array(b)

try:
    np_solution = np.linalg.solve(np_A, np_b)
    print("NumPy solution:", np_solution)

    if isinstance(my_solution, list):
        error = np.linalg.norm(np.array(my_solution) - np_solution)
        print("Difference:", error)

except np.linalg.LinAlgError as e:
    print("NumPy error:", e)
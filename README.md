# 🔢 Gaussian Elimination & Model Fitting

This project implements the **Gaussian Elimination** algorithm from scratch to solve systems of linear equations and verify results using **NumPy**.  
It demonstrates how core linear algebra methods, such as row reduction and back substitution, form the foundation of model fitting and numerical computation in AI.

---

## 📘 Project Overview
The goal was to create a full implementation of Gaussian Elimination with **partial pivoting** to ensure numerical stability and precision.  
The algorithm transforms a given matrix into **row echelon form (REF)**, checks for **system consistency** (unique, infinite, or no solution), and then applies **back substitution** to compute the result.

The implementation was tested against NumPy’s built-in solver (`numpy.linalg.solve`) to validate correctness.

---

## 🧩 Files
| File | Description |
|------|--------------|
| `gaussian_elimination_func.py` | Core implementation of Gaussian Elimination, including functions for row swapping, pivoting, forward elimination, consistency checking, and back substitution. |
| `main.py` | User input interface that reads matrix and vector values, runs the elimination process, and compares results with NumPy. |
| [📄 Assigment 2.pdf](./Assigment/Assigment%202.pdf) | Report detailing the algorithm design, numerical stability improvements, and result analysis. |

---

## ⚙️ How to Run
```bash
python main.py

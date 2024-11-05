# Optimization-Methods

This project showcases several optimization methods implemented in Python. The methods included are:

1. **Golden Ratio Method** - An optimization technique used to find the minimum of a unimodal function using the golden ratio.
2. **Dichotomy Method** - A method that repeatedly halves the interval to locate the minimum of a function.
3. **Newton's Method** - An iterative method that uses derivatives to find the minimum of a function.
4. **Total Enumeration** - A brute-force method that evaluates the function at all points in a specified range.
5. **Gradient Descent** - An optimization algorithm that uses the gradient of the function to find the minimum point.

## Why

The purpose of this project is to provide a practical understanding of different optimization techniques that are widely used in various fields such as machine learning, operations research, and engineering. By implementing these methods, users can learn about:

- **Comparison of Techniques**: Understanding the strengths and weaknesses of different optimization methods, which can be crucial when selecting the appropriate algorithm for specific problems.

- **Practical Applications**: Many real-world problems require optimization solutions. This project serves as a foundational resource for implementing optimization in various applications, from minimizing costs in business to optimizing algorithms in data science.

- **Algorithm Efficiency**: Users can explore the efficiency of each method in terms of convergence speed and accuracy, which is essential for solving large-scale optimization problems.

## Requirements

Ensure you have the following packages installed:

- `numpy` (for numerical operations)
- `time` (for measuring execution time)

You can install the required packages using pip:

```bash
pip install numpy
```

## Usage

Each optimization method is defined as a function and can be executed independently. Below are brief descriptions and examples of how to use each method.

### Golden Ratio Method

This method uses the properties of the golden ratio to reduce the search interval.

```python
from time import time

def func(x):
    return x ** 4 + 8 * x ** 3 - 6 * x ** 2 - 72 * x

# Call the method
start_time = time()
print(golden_ratio(x_1, x_2, E_n))
end_time = time()
print("Execution time:", end_time - start_time)
```

### Dichotomy Method

This method halves the search interval until the desired accuracy is achieved.

```python
start_time = time()
print(min_dichotomy())
end_time = time()
print("Execution time:", end_time - start_time)
```

### Newton's Method

This method uses the first and second derivatives to find the minimum.

```python
start_time = time()
print(newton_min(1.5, 2))
end_time = time()
print("Execution time:", end_time - start_time)
```

### Total Enumeration

This method evaluates the function at all specified points to find the minimum.

```python
start_time = time()
print(total_enumeration())
end_time = time()
print("Execution time:", end_time - start_time)
```

### Gradient Descent

This method uses the gradient to iteratively approach the minimum point.

```python
start_time = time()
print(gradient())
end_time = time()
print("Execution time:", end_time - start_time)
```

## Acknowledgments

This project is inspired by various optimization techniques commonly used in mathematical and engineering applications.

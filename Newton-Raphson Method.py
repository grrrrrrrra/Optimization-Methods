from time import time

def f(x):
    return x ** 4 + 8 * x ** 3 - 6 * x ** 2 - 72 * x

def num_diff(x, h: float = 0.0001):
    return (f(x + h) - f(x)) / h

def second_num_diff(x, h = 0.0001):
    return (num_diff(x + h) - num_diff(x)) / h

e = 0.001
a, b = 1.5, 2

def newton_min(a, b, e: float = 0.001):
    x = (a + b) / 2
    delta = 1 
    while delta > e:
        x_old = x
        delta = abs(num_diff(x_old) / second_num_diff(x_old)) 
        x = x_old - delta  
    return x, f(x)

print('newton_min')
start_time = time()
print(newton_min(1.5, 2))
end_time = time()
print("time:",end_time - start_time)
print('-' * 20)


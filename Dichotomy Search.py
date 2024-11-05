from time import time

def func(x):
    return x ** 4 + 8 * x ** 3 - 6 * x ** 2 - 72 * x

def min_dichotomy():
    e, delta = 0.00000000001, 1 
    x_0, x_1 = 1.5, 2
    
    while delta > 2 * e:
        x_sr = (x_1 + x_0) / 2
        x_left, x_right = x_sr - e, x_sr + e
        if func(x_left) < func(x_right):
            x_1 = x_sr
        else:
            x_0 = x_sr
        delta = abs(x_1 - x_0)
    
    x_min = (x_0 + x_1) / 2  
    return x_min, func(x_min)

print('min_dichotomy')
start_time = time()
print(min_dichotomy())
end_time = time()
print("time:",end_time - start_time)
print('-' * 20)
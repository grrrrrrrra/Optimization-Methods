from time import time

def func(x):
    return x ** 4 + 8 * x ** 3 - 6 * x ** 2 - 72 * x

e = 0.00000000001
a, b = 1.5, 2

x_1 = a + ((3 - 5 ** 0.5) / 2) * (b - a)
x_2 = a + ((5 ** 0.5 - 1) / 2) * (b - a)

E_n = ((5 ** 0.5 - 1) / 2) * (b - a)
 
def golden_ratio(x_1, x_2, E_n):
    while E_n > e:
        if func(x_1) < func(x_2):
            b, x_2 = x_2, x_1
            x_1 = x_2 + ((3 - 5 ** 0.5) / 2) * (b - x_2)
        if func(x_1) > func(x_2):
            a, x_1 = x_1, x_2
            x_2 = a + ((5 ** 0.5 - 1) / 2) * (x_1 - a)
        E_n = abs(x_2 - x_1)
        
        x_min = x_1
        return x_min, func(x_min)

print('golden_rat') 
start_time = time()
print(golden_ratio(x_1, x_2, E_n))
end_time = time()
print("time:",end_time - start_time)
print('-' * 20)
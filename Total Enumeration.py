from time import time

def func(x):
    return x ** 4 + 8 * x ** 3 - 6 * x ** 2 - 72 * x

def total_enumeration():
    points = []
    start_value = x_0
    while start_value <= x_1:
        points.append((start_value, func(start_value)))
        start_value += e
    return min(points, key=lambda x: x[1])

e, delta = 0.00000000001, 1
x_0, x_1 = 1.5, 2

print('total_enumeration')
start_time = time()
print(total_enumeration())
end_time = time()
print("time:",end_time - start_time)
print('-' * 20)



    


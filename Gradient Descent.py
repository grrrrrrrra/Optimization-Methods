from time import time
import numpy as np

def func(coords):
    return coords[0] ** 2 + 2 * coords[1] ** 2 + np.exp(1) ** (coords[0] + coords[1])

def neg_pd(x_1, x_2):
    d_x_1 = np.array(2 * x_1 + np.exp(x_1 + x_2))
    d_x_2 = np.array(4 * x_2 + np.exp(x_1 + x_2))
    return np.array([-d_x_1, -d_x_2])

def gradient():
    lrn_rate = 1
    e = 0.005
    x_1, x_2 = 0, 0
    new_coord = np.array([x_1, x_2]) + lrn_rate * neg_pd(x_1, x_2) # -1, -1
    
    while (neg_pd(x_1, x_2)[0] ** 2 + neg_pd(x_1, x_2)[1] ** 2) ** 0.5 > e:
        if func([x_1, x_2]) < func(new_coord):
            lrn_rate /= 2
            new_coord = np.array([x_1, x_2]) + lrn_rate * neg_pd(x_1, x_2)
        else:
            x_1, x_2 = new_coord
            new_coord = np.array([x_1, x_2]) + lrn_rate * neg_pd(x_1, x_2)
    return new_coord

print('gradient')
start_time = time()
print(gradient())
end_time = time()
print("time:",end_time - start_time)
print('-' * 20)

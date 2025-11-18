import math
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return y * (1 - x)

# Метод Эйлера
def euler_method(f, x0, y0, a, b, n):
    h = (b - a) / n
    x_values = [x0]
    y_values = [y0]
    
    x = x0
    y = y0
    
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

# Метод Рунге-Кутта 4-го порядка
def runge_kutta_method(f, x0, y0, a, b, n):
    h = (b - a) / n
    x_values = [x0]
    y_values = [y0]
    
    x = x0
    y = y0
    
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

# Параметры
a, b = 0, 1
x0, y0 = 0, 1
n = 10

# Решение методами
x_euler, y_euler = euler_method(f1, x0, y0, a, b, n)
x_rk, y_rk = runge_kutta_method(f1, x0, y0, a, b, n)

# Точное решение (аналитическое)
def exact_solution(x):
    return math.exp(x - x**2/2)

x_exact = np.linspace(a, b, 100)
y_exact = [exact_solution(xi) for xi in x_exact]

# Вывод результатов
print("Метод Эйлера:")
print("x\t\ty")
for i in range(len(x_euler)):
    print(f"{x_euler[i]:.1f}\t\t{y_euler[i]:.6f}")

print("\nМетод Рунге-Кутта:")
print("x\t\ty")
for i in range(len(x_rk)):
    print(f"{x_rk[i]:.1f}\t\t{y_rk[i]:.6f}")

# Сравнение точности
print("\nСравнение точности:")
print("x\t\tЭйлер\t\tРунге-Кутта\tТочное\t\tОшибка Эйлера\tОшибка Р-К")
for i in range(len(x_euler)):
    exact_val = exact_solution(x_euler[i])
    error_euler = abs(y_euler[i] - exact_val)
    error_rk = abs(y_rk[i] - exact_val)
    print(f"{x_euler[i]:.1f}\t\t{y_euler[i]:.6f}\t{y_rk[i]:.6f}\t{exact_val:.6f}\t{error_euler:.6f}\t{error_rk:.6f}")

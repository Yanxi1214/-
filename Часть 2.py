def f2_system(x, y, z):
    # y' = z
    # z' = -z/x - y
    return z, -z/x - y

def solve_second_order_euler(f, x0, y0, z0, a, b, n):
    h = (b - a) / n
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]
    
    x = x0
    y = y0
    z = z0
    
    for i in range(n):
        dy, dz = f(x, y, z)
        y = y + h * dy
        z = z + h * dz
        x = x + h
        
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)
    
    return x_values, y_values, z_values

def solve_second_order_rk(f, x0, y0, z0, a, b, n):
    h = (b - a) / n
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]
    
    x = x0
    y = y0
    z = z0
    
    for i in range(n):
        # k1 для y и z
        k1y, k1z = f(x, y, z)
        k1y *= h
        k1z *= h
        
        # k2 для y и z
        k2y, k2z = f(x + h/2, y + k1y/2, z + k1z/2)
        k2y *= h
        k2z *= h
        
        # k3 для y и z
        k3y, k3z = f(x + h/2, y + k2y/2, z + k2z/2)
        k3y *= h
        k3z *= h
        
        # k4 для y и z
        k4y, k4z = f(x + h, y + k3y, z + k3z)
        k4y *= h
        k4z *= h
        
        y = y + (k1y + 2*k2y + 2*k3y + k4y) / 6
        z = z + (k1z + 2*k2z + 2*k3z + k4z) / 6
        x = x + h
        
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)
    
    return x_values, y_values, z_values

# Параметры
a, b = 1, 1.5
x0, y0, z0 = 1, 0.77, -0.44
n = 5

# Решение
x_euler2, y_euler2, z_euler2 = solve_second_order_euler(f2_system, x0, y0, z0, a, b, n)
x_rk2, y_rk2, z_rk2 = solve_second_order_rk(f2_system, x0, y0, z0, a, b, n)

# Вывод результатов
print("ДУ второго порядка - Метод Эйлера:")
print("x\t\ty\t\ty'")
for i in range(len(x_euler2)):
    print(f"{x_euler2[i]:.1f}\t\t{y_euler2[i]:.6f}\t{z_euler2[i]:.6f}")

print("\nДУ второго порядка - Метод Рунге-Кутта:")
print("x\t\ty\t\ty'")
for i in range(len(x_rk2)):
    print(f"{x_rk2[i]:.1f}\t\t{y_rk2[i]:.6f}\t{z_rk2[i]:.6f}")
